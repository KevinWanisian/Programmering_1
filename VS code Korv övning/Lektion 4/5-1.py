
try:
    tal = (int(input("ange ett heltal:")))
    resultat = (tal * 2)
    print("Det dubbla värdet blir", resultat)
except ValueError:
        print("FEL:\nKan inte dubbleras!")