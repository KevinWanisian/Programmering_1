ui = 30

print((".:Mathlete:.").center(ui))
print((ui * "-").center(ui))

times = 0
summan = 0

while True:
    try:
        tal = input("Ange ett hel tal:")
        times += 1
        summan += int(tal)

    except ValueError:
        if tal == "exit".lower():
            print("-" * ui)
        else:
            print("Fel: Oglitigt nummer!")
    if tal == "exit".lower():
        break
print("Försök:",times)
print("Summan:", summan)
print("Medelvärde:", summan / times)

