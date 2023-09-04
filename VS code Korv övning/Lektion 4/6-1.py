ui = 30

print((".:Bokstavsräknare:.").center(ui))
print((ui * "-").center(ui))


t1 = 0
t2 = 0
summa = 0

t1 = input("Ange din text här:").lower()
length = len(t1)
t2 = input("Ange bokstav här:").lower()


for i in range(length):
    if t1[i] == t2: # range(length) = längden, "i" höjs med 1 tills den når range(length)
        summa += 1
print("Bokstaven", t2.upper(), "förekommer", summa, "gånger i texten")


