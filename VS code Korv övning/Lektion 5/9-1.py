# Heltal = variabel. Range= innebär att den startar från 1 och avslutar på 1 miljon.
#
summa = 0
summa_udda = 0

for heltal in range(1,1000001):
    summa += heltal
print(summa)
print()
# 2an innebär hur många gånger den hoppar mellan nummer
# heltal_udda är en ny variabel
for heltal_udda in range(1,500,2):
    summa_udda += heltal_udda
print(summa_udda)

