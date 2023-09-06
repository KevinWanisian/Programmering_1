ui = 30

Post1 = "Ange något nytt här:"
Post2 = "Ange något nytt här:"
Post3 = "Ange något nytt här:"
e = 1
c = -1
meny = 0

while True:
    print((".:Basic Billboard:.").center(ui))
    print((ui * "*").center(ui))
    if meny != c:
        Post1 = input("P1:")
        Post2 = input("P2:")
        Post3 = input("P3:")
        print(ui * "-")
        print("c | Ändra post")
        print("e | Stäng program")
        print(ui * "-")
        meny = input("Meny >")
        continue
    else:
        ValueError:(
            print("Nu är programmet avslutat!"))
        break




