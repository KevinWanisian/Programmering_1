def raknautolder(age):
  if  age == 1:
    return "Sova minst 14 timmar per natt per natt"
  elif age == 2:
    return "Sova minst 13 timmar per natt"
  elif age == 3:
    return "Sova minst 12 timmar per natt"
  elif age == 4:
    return "Sova minst 11.5 timmar per natt"
  elif age == 7:
    return "Sova minst 10.5 timmar per natt"
  elif age == 11:
    return "Sova minst 9.5 timmar per natt"
  elif age == 16:
    return "Sova minst 8.5 timmar per natt"
  elif age >= 17:
    return "Sova minst 8 timmar per natt"
  elif age == 5 or 6:
    return "Sova minst 11 timmar per natt"
  elif age <= 10:
    return "Sova minst 10 timmar per natt"
  else:
    return "Osäker!"

namn = input("Vad är ditt namn?:")
age = int(input("Hur gammal är du?:"))
dubehover = raknautolder(age)


if dubehover != "osäker":
   meeddela = f"Hej {namn}! Enligt Vårrdguidensrekommendationer behöver individer i din ålder {age} {dubehover}"
   print(meeddela)
else:
  print("ålrdern du gav stämmer inte med våran tabell")
