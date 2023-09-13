# Skapa en dictionary med rubriker och meddelanden
rubrik_dictionary = {
    "Anteckning": "Kom ihåg!",
    "Ta bilen till verkstad": "Bilen måste till verkstaden.",
}

# Låt användaren ange rubrik
rubrik = input("Ange rubrik: ")

# Kolla om rubriken finns i dictionaryn och skriv ut meddelandet
if rubrik in rubrik_dictionary:
    print(rubrik_dictionary[rubrik])
else:
    print(f"FEL: {rubrik} finns inte.")
