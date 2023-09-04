ui = 30

print((ui *"*").center(ui))
print("* The Great Diveder *".center(ui))
print((ui *"-").center(ui))

print("Beräkna uttrycket a / b = c")

print((ui *"-").center(ui))

while True:
    try:
        a = float(input("Ange ett tal:")) #Skriver in ett nummer till A
        b = float(input("Ange ett tal:")) #Skriver in ett nummer til B
        resultat = a / b
        print("Resutlat blir:", resultat)
        if a == 0:
            print("Fel går inte att dela på 0!")
        elif b == 0:
            print("Fel går inte att dela på 0!")
        else:
            print(resultat)


    except ValueError:
        print("FEL: Det är inget tal")
    except ZeroDivisionError:
        print("Fel: Går inte att dela med 0!")




