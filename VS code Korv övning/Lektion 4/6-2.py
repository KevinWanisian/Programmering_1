def är_palindrom(mening):
    # Ta bort blanksteg och skiljetecken och konvertera till små bokstäver
    rent_mening = "".join(filter(str.isalnum, mening)).lower()

    # Jämför med baklängesläst version av meningen
    return rent_mening == rent_mening[::-1]


# Läs in en mening från användaren
mening = input("Ange en mening: ")

# Kolla om det är ett palindrom
if är_palindrom(mening):
    print(f"'{mening}' är ett palindrom.")
else:
    print(f"'{mening}' är inte ett palindrom.")

