# zahlenraten_random.py

import random

zzahl = random.randint(0,100)
print("Bitte geben Sie eine Zahl zwischen 0 und 100 ein.")
zahl = -1
while zahl != zzahl:
    zahl = int(input("Rate die zufällige Zahl: "))
    if zahl == zzahl:
       print("Herzlichen Glückwunsch! Sie haben die Zahl gefunden!")
    elif  zahl > zzahl:
       print("Zu groß")
    else:
       print("Zu klein")