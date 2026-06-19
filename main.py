import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

model = "gpt-4o-mini"

user_prompt = input("Ask the Question: ")

response = client.responses.create(
    model=model,
    input=user_prompt
)

print(response.output_text)