# Skapa en dictionary med rubriker och meddelanden
rubrik_dictionary = {
    "Meddelande från skolan": "Innehåll för meddelande från skolan",
    "Kom ihåg!": "Innehåll för kom ihåg!",
    "Inför tentamen": "Innehåll för inför tentamen",
}


print(".: ANTECKNINGAR :.")
print("******************")

# Loopa genom dictionaryn och skriv ut titlarna
for rubrik in rubrik_dictionary:
    print("-", rubrik)

print("------------------")
