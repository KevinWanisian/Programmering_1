#reg = regristerad
reg = ["Anna", "Eva", "Erik", "Lars", "Karl"]
# av = avanmälningar
av = ["Anna", "Erik", "Karl"]

# i = variabel
for i in reg:
    if i in av:
        reg.remove(i)

print(reg)
