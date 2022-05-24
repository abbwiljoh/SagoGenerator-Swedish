
# Kommandon att köra:
#   pip install openai
#   pip install python-decouple
# Skapa en fil ".env" där OPENAI_API_KEY=key och ORGANIZATION=org_id //// Man får nyckeln och org_id om man skapar ett konto hos OpenAI - Nyckeln måste hållas hemlig!!!


import openai
from decouple import config
import json

# Babbage är en billig men bra modell som fungerar bra i demonstrationssyfte.
model = "babbage"
custom_name = "william-test-alfa"

with open("Kod\information.json") as info:
    data = json.loads(info.read())

openai.organization = config("ORGANIZATION")
openai.api_key = config("OPENAI_API_KEY")

# Ladda upp fil (om man är i Kod/ är det "../texter/sagor.jsonl"), men bara om det inte finns en fil uppladdad redan.
if data["file"] == {}:
    file_data = openai.File.create(
        file=open("texter\sagor.jsonl"),
        purpose="fine-tune"
    )
    data["file"] = file_data

else:
    print("Showing old file info:")
    file_data = data["file"]

print(file_data)

# FINE-TUNING:
# training-file är filen som vi nyss laddat upp med all träningsdata
# model är den modell vi vill fine-tune:a
# n_epochs är antalet epoker som kommer köras (rekommenderat 2 epoker för effektivitet och pris).
# suffix är ett namn som kan läggas till i färdigtränade modellens nammn

if data["fine-tune"] == {}:
    fine_tune = openai.FineTune.create(
        training_file=file_data["id"], model=model, n_epochs=2, suffix=custom_name)
    data["fine-tune"] = fine_tune

else:
    # Om fine-tune redan finns men inte är klar, vill vi kolla informationen om fine-tuningen, för att se till att allt går rätt till.
    if data["fine-tune"]["status"] != "succeeded":
        print("Updating fine-tune information.")
        fine_tune = data["fine-tune"]
        fine_tune_info = openai.FineTune.retrieve(id=data["fine-tune"]["id"])
        data["fine-tune"] = fine_tune_info


print(fine_tune)

with open("Kod\information.json", "w") as info:
    info.write(json.dumps(data))
