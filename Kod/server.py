"""
@brief: Program att agera API för webbapplikationen, där sagor ska kunna genereras.
"""

import openai
from decouple import config
import json
from flask import Flask, request


def get_text(title: str) -> str:
    text = ""
    result = openai.Completion.create(
        model=data["fine-tune"]["fine_tuned_model"],
        prompt=title,
        max_tokens=400,
        temperature=0.83,
    )

    if result[-1] != ".":
        result += "..."

    space_indices = []
    index_0 = 0

    c = 0
    for char in result:
        if char in {".", ",", ":", ";", "?", "!"}:
            if c < len(result) - 1 and result[c + 1] != " ":
                space_indices.append(c + 1)
        c += 1

    for idx in space_indices:
        text += result[index_0:idx] + " "
        index_0 = idx
    text += result[index_0:len(result)]

    return text


title = "Den stora dagen."

with open("Kod\information.json") as info:
    data = json.loads(info.read())

openai.organization = config("ORGANIZATION")
openai.api_key = config("OPENAI_API_KEY")

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def return_text():
    if "title" not in request.args:
        return "Error: No title field provided. Please specify a title."

    try:
        title = request["title"]
        if title[-1] != ".":
            title += "."
    except Exception as e:
        return "Error: No title field provided. Please specify a title."

    text = get_text(title)

    return {
        "title": title,
        "text": text
    }
