import json

attendants = ['Åsa','Kalle', 'Olivia', 'Johan']


with open('data.json', 'w') as myFile:
    myFile.write(json.dumps(attendants))

with open('data.json') as myFile:
    data = json.loads(myFile.read())
    print(data[0])