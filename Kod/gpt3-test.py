
import openai
from decouple import config
import json

title = ""

with open("Kod\information.json") as info:
    data = json.loads(info.read())

openai.organization = config("ORGANIZATION")
openai.api_key = config("OPENAI_API_KEY")

result = openai.Completion.create(
    model=data["fine-tune"]["fine_tuned_model"],
    prompt=title,
    max_tokens=275,
    temperature=0.81,
)

print(result)
print(result["choices"][0]["text"])
