import random
dice = random . randint (1 , 6)


print("---Välkommen till Dice!---")
print(".:---------------------:.")

play = input("Skriv play när du är redo!:")

dice_art = [
    "+-------+",
    "|       |",
    "|   {}   |".format(dice),
    "|       |",
    "+-------+"
]
for line in dice_art:
    print(line)




