# mathe_funktionen.py

import random
from math import *

random1 = random.randint(0,10)
print("Erzeuge eine zufällige Zahl zwischen 0 und 10.")
print("Die zufällige Zahl ist: ", random1)
print("\n")

print("Berechne die Quadratwurzel auf zwei Nachkommastellen genau.")
squere1 = sqrt(random1)
print("Die Quadratwurzel ist: ",round(squere1,2))
print("\n")

print("Berechne den natürlichen Logarithmus von der anfänglichen zufälligen Zahl.")
if random1 > 0:
    natural_logarithms = log(random1)
    print("Der natürliche Logarithmus ist: ",round(natural_logarithms,2))
else:
    print("Der natürliche Logaritmus von null ist nicht definiert.")
print("\n")

print("Berechne den Logarithmus zur Basis 10 von der anfänglichen zufälligen Zahl.")
if random1 > 0:
    logarithms_10 = log10(random1)
    print("Der Logarithmus zur Basis 10 ist: ", round(logarithms_10,2))
else:
    print("Der natürliche Logaritmus von null ist unabhängig von der Basis nicht definiert.")
print("\n")

print("Berechne die Fakultät der zufälligen Zahl.")
fakultät = factorial(random1)
print("Die Fakultät ist: ", fakultät)
print("\n")

print("Berechne (r hoch r) + r """
      "und gib den größten gemeinsamen Teiler zwischen r und der neuen Zahl aus.")
if random1 > 0:
    result = int(pow(random1,random1) + random1)
    print("Das Ergebnis ist: ", result)
    g_g_teiler = gcd(result, random1)
    print("Der größte gemeinsame Teiler zwischen r und der neuen Zahl ist: ", g_g_teiler)
else:
    print("0 hoch 0 ist nicht definiert.")
print("\n")
