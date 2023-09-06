import os


if os.path.exists('textfil.txt'):
    f = open('textfil.txt', 'w')
else:
    f = open('textfil.txt', 'x')




def print_sign(message):
    print("| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |")
    print("|  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  |")
    print(f"| ### | {message.center(18)} | # ### | - - - - - - - - - - - - - - - - - - - - - - - - - |")
    print("| ### - - - - - - - - - - - - - - - - - - - - - - - - - - - ### ### - - - - - - - - - - |")
    print("|  | - - - - - - - - - - - - - - - - - - - - - - - - - - - - | - | - - - - - - - - -  # |")
    print("| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |")
    print("| C | Change sign message")
    print("| E | Exit program")
    print("| - - - - - - - - - - - - - - - - - - - - - - - -")

message = "Welcome to Västerås"

while True:
    print_sign(message)
    choice = input("Enter your choice (C/E): ").upper()

    if choice == "C":
        new_message = input("Enter new sign message: ")
        message = new_message[:18]  # Truncate message to fit on the sign
    elif choice == "E":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 'C' or 'E'.")