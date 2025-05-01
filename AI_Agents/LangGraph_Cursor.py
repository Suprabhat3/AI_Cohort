from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from typing import Literal
from langsmith.wrappers import wrap_openai
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
load_dotenv()
# Schema for pydantic

class DetectCallResponse(BaseModel):
    is_question_ai: bool

class CodingAIResponse(BaseModel):
    answer: str


key = os.getenv("KEY")
client = wrap_openai(OpenAI(
    api_key=key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
))


class State(TypedDict):
    user_message: str
    ai_message: str
    is_coding_question: bool

def detect_query(state: State):
    user_message = state.get("user_message")


    SYSTEM_PROMPT = """
    You are an AI assistant. Your job is to detect if the user's query is related
    to coding question or not.
    Return the response in specified JSON boolean only.
    """

    # OpenAI Call
    result = client.beta.chat.completions.parse(
        model="gemini-2.0-flash",
        response_format=DetectCallResponse,
        messages=[
            { "role": "system", "content": SYSTEM_PROMPT },
            { "role": "user", "content": user_message }
        ]
    )    

    state["is_coding_question"] = result.choices[0].message.parsed.is_question_ai
    return state

def route_edge(state: State) -> Literal["solve_coding_question", "solve_simple_question"]:
    is_coding_question = state.get("is_coding_question")

    if is_coding_question:
        return "solve_coding_question"
    else:
        return "solve_simple_question"
    


def solve_simple_question(state: State):
    user_message = state.get("user_message")

    # OpenAI Call (Coding Question gpt-mini)
    SYSTEM_PROMPT = """
    You are an AI assistant. Your job is to chat with user
    """

    # OpenAI Call
    result = client.beta.chat.completions.parse(
        model="gemini-2.0-flash",
        response_format=CodingAIResponse,
        messages=[
            { "role": "system", "content": SYSTEM_PROMPT },
            { "role": "user", "content": user_message }
        ]
    )
    state["ai_message"] = result.choices[0].message.parsed.answer

    return state




def solve_coding_question(state: State):
    user_message = state.get("user_message")

   
    SYSTEM_PROMPT = f"""
    You are an helpfull AI Assistant who is specialized in resolving user query.
    You are a master in programming and write good and structured code.
"""

    # Gemini Call
    result = client.beta.chat.completions.parse(
        model="gemini-2.0-flash",
        response_format=CodingAIResponse,
        messages=[
            { "role": "system", "content": SYSTEM_PROMPT },
            { "role": "user", "content": user_message }
        ]
    )
    state["ai_message"] = result.choices[0].message.parsed.answer

    return state









graph_builder = StateGraph(State)


graph_builder.add_node("detect_query", detect_query)
graph_builder.add_node("solve_coding_question", solve_coding_question)
graph_builder.add_node("solve_simple_question", solve_simple_question)
graph_builder.add_node("route_edge", route_edge)

graph_builder.add_edge(START, "detect_query")
graph_builder.add_conditional_edges("detect_query", route_edge)

graph_builder.add_edge("solve_coding_question", END)
graph_builder.add_edge("solve_simple_question", END)

graph = graph_builder.compile()


# Use the Graph

def call_graph():
    while (True):
        user_message = input("How can i help you: ")
        if(user_message == "exit"):
            break
        # if(state["ai_message"]):
        state = {
            "user_message": user_message,
            "ai_message": "",
            "is_coding_question": False
        }
        
        result = graph.invoke(state)
        print("🤖", result["ai_message"])
    

    

call_graph()