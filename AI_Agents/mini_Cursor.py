from openai import OpenAI
# import requests
import os
import json


client = OpenAI(
    api_key="AIzaSyAEYzqTJbunMkDp2MRImHAz0CaXlov8Nt8",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def run_command(command):
    result = os.system(command=command)
    return result


avaiable_tools = {
    "run_command": {
        "fn": run_command,
        "description": "Takes a command as input to execute on system and returns ouput"
    }
}

system_prompt = f"""
    You are an helpfull AI Assistant who is specialized in resolving user query.
    You are a master in programming and write good and structured code. 
    You work on start, plan, action, observe mode.
    For the given user query and available tools, plan the step by step execution, based on the planning,
    select the relevant tool from the available tool. and based on the tool selection you perform an action to call the tool.
    Wait for the observation and based on the observation from the tool call resolve the user query.

    Rules:
    - Follow the Output JSON Format.
    - Always perform one step at a time and wait for next input
    - Carefully analyse the user query

    Output JSON Format:
    {{
        "step": "string",
        "content": "string",
        "function": "The name of function if the step is action",
        "input": "The input parameter for the function",
    }}

    Available Tools:
    - run_command: Takes a command as input to execute on system and returns ouput
    
    Example:
    User Query: Create a file in my current directory in python for a simple calculator
    Output: {{ "step": "plan", "content": "The user is interseted in creating a file in current directory" }}
    Output: {{ "step": "plan", "content": "From the available tools I should call run_command" }}
    Output: {{ "step": "action", "function": "run_command", "input": "command" }}
    Output: {{ "step": "observe", "output": "file created successfully" }}
    Output: {{ "step": "output", "content": "As per you request file created successfully." }}
"""

messages = [
    { "role": "system", "content": system_prompt }
]

while True:
    user_query = input('> ')
    messages.append({ "role": "user", "content": user_query })

    while True:
        response = client.chat.completions.create(
            model="gemini-2.0-flash",
            response_format={"type": "json_object"},
            messages=messages
        )
        parsed_output = json.loads(response.choices[0].message.content)
        messages.append({ "role": "assistant", "content": json.dumps(parsed_output) })

        if parsed_output.get("step") == "plan":
            print(f"🧠: {parsed_output.get("content")}")
            continue
        
        if parsed_output.get("step") == "action":
            tool_name = parsed_output.get("function")
            tool_input = parsed_output.get("input")

            if avaiable_tools.get(tool_name, False) != False:
                output = avaiable_tools[tool_name].get("fn")(tool_input)
                messages.append({ "role": "assistant", "content": json.dumps({ "step": "observe", "output":  output}) })
                continue
        
        if parsed_output.get("step") == "output":
            print(f"🤖: {parsed_output.get("content")}")
            break








