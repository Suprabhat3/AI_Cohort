from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

system_prompt = """
You are a helpful assistant that thinks step by step.
Example-
Alex have 12 banana, he give 2 to John 3 to Jyuli haw much now Alex have,
do it step by step 
1. Alex have 12 Banana
2. He give 2 to John (12-2)=10
3. He give 3 to Jyuli (10-3)=7
4. Alex have 7 Banana have
"""


client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.0-flash",
    n=1,
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": "Ram have 100 rupees he give 10 to rahul 20 to rohan 15 to hitesh how much ram left"
        }
    ]
)

print(response.choices[0].message.content)

'''Input -
Ram have 100 rupees he give 10 to rahul 20 to rohan 15 to hitesh how much ram left
 Output -
1.  Ram starts with 100 rupees.
2.  He gives 10 rupees to Rahul (100 - 10 = 90).
3.  He gives 20 rupees to Rohan (90 - 20 = 70).
4.  He gives 15 rupees to Hitesh (70 - 15 = 55).

So, Ram is left with 55 rupees.
'''