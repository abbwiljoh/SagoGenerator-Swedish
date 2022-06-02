# SagoGenerator-Swedish
*AI-genererade historier och sagor på svenska!*

## Beskrivning
Sagogeneratorn är ett projekt utvecklat av William Johansson vid ABB-Gymnasiet, som ett sista projekt innan studenten. Tanken var att det här projektet skulle kombinera kunskaper inom AI, API:er och webbutveckling; kunskaper som vi fått under olika programmeringskurser över de tre år vi spenderat på spetsen. 

Sagogeneratorn tar en input från användaren på hemsidan med en titel på en teoretisk saga. Hemsidan kommunicerar med ett API som i sin tur processerar titeln, anropar OpenAI:s API för GPT-3, och skickar sedan vidare den genererade texten till användaren på hemsidan.

Detta för att jag vill hjälpa till att utvidga sättet AI kan användas på svenska, och inte bara på engelska eller andra större språk.

## Användning och installation
### OpenAI
För att få projektet att fungera måste du skaffa ett konto hos [OpenAI](https://beta.openai.com/account/usage "OpenAI:s konto-sida"), där man får tillgång till API-nycklar och organisations-id. I [Kod](Kod/)-mappen lägger du in en fil döpt `.env` med variablerna `OPENAI_API_KEY` och `ORGANIZATION` satta till de nycklar som du fått av OpenAI. Viktigt är att du inte läcker dessa, då kan du förlora ditt konto!

Du får fine-tune:a din egen modell, med hjälp av programmet [gpt3-tuning.py](Kod/gpt-3-tuning.py), som använder sig av `.jsonl`-filen som finns i samma mapp. Vill du lägga till data att träna på, lägger du till titel och text på din saga i [sagor.txt](./sagor.txt), och kör sedan filen [story_formatter.py](Kod/story_formatter.py) för att få en ny `.jsonl`-fil.

Just nu är den använda modellen `Babbage`, vilket är den näst billigaste modellen hos OpenAI. Ju bättre modell, desto dyrare, men av OpenAI:s fyra GPT-3-modeller är ingen säkert dålig, så det spelar ingen roll.

### Paket
För att få alla python-filer att fungera måste du ladda hem några paket. Med hjälp av pip är kommandon

```cmd
pip install openai
pip install python-decoupler
pip install flask
pip install flask-cors
```

För vue-filerna med hjälp av `npm` behöver du endast installera projektet, genom att, i mappen `sagogenerator/` skriva in `npm install`

### Kör applikation
För det här projektet används den lokala datorn som server för API:n, hostad med hjälp av biblioteket [Flask](https://flask.palletsprojects.com/en/2.1.x/). För att starta denna, kör filen [server.py](Kod/server.py), och API:n kommer starta på `http://177.0.0.1:5000` med textgenerering vid routen `/text`. För att manuellt kalla API:n, kör `http://177.0.0.1:5000/text?title=HÄR HAR DU DIN TITEL` och skriver din egen titel efter `?title=`.

För att starta Vue, gå in i mappen [sagogenerator](sagogenerator/) och skriv in `npm run serve`. 

Nu har du en fullt fungerande hemsida kopplad till AI-tjänsten, förutsatt att du fortfarande har krediter att använda hos OpenAI.

## Reflektioner
Jag är väldigt nöjd med detta projekt, jag har fått lära mig hur man skapar sin egen API med flask, och också fått hitta egna resurser för att lära mig använda GPT-3. Dessutom har jag fått programmera i väldigt olika stilar, för olika syften, och i olika språk. 

Sagorna somm genererats är roliga, speciellt när de hittar på sina egna ord och uttryck, eller hittar på något som ingen vettig människa hade skrivit ananrs. Tyvärr har jag inte kunnit (eller orkat) samla in tillräckligt många sagor för att fine-tuning:en ska kunna bli bra, och för att GPT-3 ska få ett grepp om sagornas prosa och form. Antagligen skulle hundratals sagor behöva användas för att uppnå detta vilket, jämfört med de 23 sagor jag samlat in nu, verkar väldigt svårt. Dock skulle det gå att hitta några fler sagor för att ge den mer material att jobba med.

Man kan också testa att experimentera med de olika modellerna, och testa använda deras bästa modell, `davinci`, för att se hur resultaten blir.