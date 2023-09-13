print("Välkommen till Geografi")
print("-------------------------")


norden = ["sverige", "danmark", "norge","island", "finland"]
uk = ["england","wales","nordirland","skottland"]

land = input("Skriv in ett land som finns i antingen Norden eller United kingdom:").lower()

if land in norden:
    print("Du är från Skandinavien")
elif land in uk:
    print("Du är från United kingdom")
else:
    print("Du är inte från någon av delarna.")