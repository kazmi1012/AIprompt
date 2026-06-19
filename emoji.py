import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("API key not found! Check your .env file.")
    exit()

client = OpenAI(api_key=api_key)

model = "gpt-4o-mini"

system_prompt = (
    "You will be provided with text, and your task is to translate it into emojis. "
    "Do not use any regular text. Use emojis only."
)

while True:
    user_prompt = input("Enter a prompt (or 'exit' to quit): ")

    if user_prompt.lower() == "exit":
        print("Bye!")
        break

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]

    response = client.responses.create(
        model=model,
        input=messages
    )

    print(response.output_text)