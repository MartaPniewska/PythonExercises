#Kreditberechnung

import time

kredit = float(input("Kreditsumme in Euro: "))
zins = float(input("Zinsatz in % "))
rückzahlung = float(input("Jährliche Rückzahlung in Euro: "))
jahr = time.localtime()[0]

while kredit > rückzahlung:
    jahr += 1
    zinsen = round(zins*kredit/100)
    tilgung = round(rückzahlung - zinsen)
    kredit = round(kredit - tilgung)
    print(jahr, " Zinsen:  ", zinsen,  "EUR Tilgung: ", tilgung, " EUR Restschulden: ", kredit, " EUR")
print("Restforderung: ", kredit, " EUR")

