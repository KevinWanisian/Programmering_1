ui = 30
bilar = ["Mercedes", "Volvo", "Toyota", "Kia"]
while True:
    try:
        num = 1
        print(".: STACKMASTER v1 .33.7 :.".center(ui))
        print("-" * ui)
        for i in bilar:
            print(num, "-", i)
            num += 1
        print("-" * ui)
        print("| Menu |".center(ui))
        print("push |","Push element to stack" )
        print("pull |","Pull element from stack")
        print("exit |","Exit program")
        print("-" * ui)
        meny = input("MENU >")

        if meny == "push":
            val = input("Vilken märke vill du lägga till? ")
            bilar.append(val)
        elif meny == "pull":
            val_id = int(input("Vilken ID vill du ta bort? "))
            bilar.pop(val_id-1)
        elif meny == "exit":
            break
        else:
            print("Ogiltigt val!")
            input("Tryck retur för att köra igen")
    except ValueError:
        print(i, "är inte giltigt heltal!")
    except IndexError:
        print(val_id, "är inte giltigt index")



