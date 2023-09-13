nummer = []
# Nummer listan

while True:
  try:
      tal = float(input("Ange ett hel tal (ett negativ tal avlustar programmet:"))
      if tal < 0:
        break
      nummer.append([])
  except ValueError:
    print("Oglitigt värde, ange ett heltal:")

if not nummer:
  print("Inga giltiga nummer har matats in")
else:
  minsta = min(nummer)
  max = max(nummer)
  summan = sum(nummer)
  medelvärde = sum / len(nummer)


  print("Minsta talet:", minsta)
  print("Största talet:", max)
  print("Summan:", summan)
  print("Medelvärdet:", medelvärde)  


