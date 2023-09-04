tal = input("Ange ett heltal:")
try:
    tal = int(tal)
    kvadrat = tal * tal
    print(tal,"i kvadrat är", kvadrat)
except:
    print(tal , "är inte ett heltal")