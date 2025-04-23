from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()

client = OpenAI(
      api_key=os.getenv("KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system_prompt = """
You are an AI Assistant who is specialized in convert user query to 3 diffrent querys

"""

result = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[
        { "role": "system", "content": system_prompt },
        { "role": "user", "content": "Why we need Oxigen" }
    ]
)

print(result.choices[0].message.content)

'''1.  What is the role of oxygen in human survival and bodily functions?
 2.  How do living organisms, including plants and animals, utilize oxygen for respiration and energy production?
3.  What are the consequences of oxygen deprivation or deficiency in the human body?'''