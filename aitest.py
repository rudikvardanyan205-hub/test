from openai import OpenAI
from pydantic import BaseModel

class Movie(BaseModel):
    title: str
    rating: int


client = OpenAI()
completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Review Inception, rating it 9 out of 10."}],
    response_format=Movie,
)

result = completion.choices.message.parsed
print(result.title)  
print(result.rating)