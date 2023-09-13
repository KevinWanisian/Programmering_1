kön = input("Vad har du för kön? M/K:").lower()
hår = input("Ange hårfärg:").lower()
ögon = input("Vad har du för ögonfärg?").lower()



kända_personer = [
    {"Namn": "Daniel Radcliffe", "Kön": "man", "Hårfärg": "brun", "Ögonfärg": "brun"},
    {"Namn": "Rupert Grint", "Kön": "man", "Hårfärg": "röd", "Ögonfärg": "blåa"},
    {"Namn": "Emma Watson", "Kön": "kvinna", "Hårfärg": "brun", "Ögonfärg": "brun"},
    {"Namn": "Selena Gomez", "Kön": "kvinna", "Hårfärg": "brun", "Ögonfärg": "brun"},
    {"Namn": "Scarlett Johnhansson", "Kön": "kvinna", "Hårfärg": "blond", "Ögonfärg": "blåa"},

]

matchandepersoner = []
for person in kända_personer:
    if (
        person["Kön"].lower() == kön and
        person["Hårfärg"].lower() == hår and
        person["Ögonfärg"].lower() == ögon
    ):
        matchandepersoner.append(person["Namn"])
if matchandepersoner:
    print("Egenskaperna matchar med", ",".join(matchandepersoner))
else:
    print("Känner inte egen den personen")
