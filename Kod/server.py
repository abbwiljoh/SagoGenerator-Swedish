"""
@brief: Program att agera API för webbapplikationen, där sagor ska kunna genereras. Kör denna fil för att starta API:n, och starta sedan hemsidan i sagogenerator-mappen
`pip install flask` och `pip install flask-cors`
"""

import openai
from decouple import config
import json
from flask import Flask, request
from flask_cors import CORS


def get_text(title: str) -> str:
    text = ""
    result = openai.Completion.create(
        model=data["fine-tune"]["fine_tuned_model"],
        prompt=title,
        max_tokens=400,
        temperature=0.83,
    )

    result_text = result["choices"][0]["text"]
    print(result)

    if result_text[-1] != ".":
        result_text += "..."

    space_indices = []
    index_0 = 0

    c = 0
    for char in result_text:
        if char in {".", ",", ":", ";", "?", "!"}:
            if c < len(result_text) - 1 and result_text[c + 1] != " ":
                space_indices.append(c + 1)
        c += 1

    for idx in space_indices:
        text += result_text[index_0:idx] + " "
        index_0 = idx
    text += result_text[index_0:len(result_text)]

    return text


title = "Den stora dagen."

with open("Kod\information.json") as info:
    data = json.loads(info.read())

openai.organization = config("ORGANIZATION")
openai.api_key = config("OPENAI_API_KEY")

app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app)


@app.route("/text", methods=['POST', 'GET'])
def return_text():
    if "title" not in request.args:
        return "Error: No title field provided. Please specify a title."

    try:
        title = request.args["title"]
        if title[len(title) - 1] != ".":
            title += "."

    except Exception as e:
        return "Error: No title field provided. Please specify a title."

    text = get_text(title)

    return {
        "title": title,
        "text": text
    }


app.run()
