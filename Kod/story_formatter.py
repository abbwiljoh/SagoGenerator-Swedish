"""
Program för att formattera om sagor.txt till JSON för att kunna användas i GPT-3.
Format: {"prompt": "<Titel>", "completion": "<Saga>"}
"""

import json
from time import time

# This code was taken from PogFish 🐟😎💪🤤🍔💦💨🤘🖖💣 # Det var den faktiskt inte, men är kul att ha kvar
print("The program is now starting!")
time1 = time()

dataset = []

with open("texter\sagor.txt", "r", encoding="utf-8") as txt:
    stories = txt.read().split("\n\n\nTitel: ")
    for story in stories:
        lines = story.split("\n")
        prompt = " " + lines[0] + "\n\n###\n\n"
        completion = " "
        for line in lines[1:]:
            completion += line
        completion += "###"
        dataset.append({'prompt': prompt, 'completion': completion})

json_string = ""

for entry in dataset:
    json_string += json.dumps(entry) + "\n"

with open("texter/sagor.jsonl", "w", encoding="utf-8") as f:
    f.write(json_string[:-1])

time2 = time()
print("The program is now finished (" + str((time2-time1)*1000) + " milliseconds)")
