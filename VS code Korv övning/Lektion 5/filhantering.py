import os
if os.path.exists('textfil.txt'):
    myFile = open('textfil.txt', 'a')
else:
    myFile = open('textfil.txt', 'x')


myFile.close()

with open('textfil.txt',"r+") as myFile:
    myFile.write("Rad4\n")
    text = myFile.read()
    print(text)