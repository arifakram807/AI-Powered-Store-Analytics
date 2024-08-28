import openai
from config import config

openai.api_key = config.OPENAI_API_KEY

def generate_insights(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access to it
        messages=[
            {"role": "system", "content": "You are a data analyst."},
            {"role": "user", "content": f"Analyze the following data and provide insights: {text}"}
        ]
    )
    return response['choices'][0]['message']['content']
