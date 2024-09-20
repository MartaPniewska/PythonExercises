# listen_operationen.py

liste = ["Hallo", 3.2, True, 47, 65.343]

#  Gib eine Liste mit den ersten beiden Elementen dieser Liste aus.
print(liste[:2])
# Gib eine Liste mit allen Elementen der obigen Liste ab dem 4. Element aus.
print(liste[3:])

# Gib den Datentyp des 3. Elements aus.
print(type(liste[2]))

# Wandle das letzte Element der Liste in einen Integer um.
print(int(liste[4]))

# Bestimme die Summe der Zahlen in der Liste und wandle sie in einen Integer um.
summe = float(liste[1]) + float(liste[3]) + float(liste[4])
print(int(summe))

#Tupel, Dictionary 4Ü05
tupel1 = ("Alter", 25)
tupel2 = ("Planet","Erde")
tupel3 = ("Mensch", True)
tupel4 = ("Bereiste Länder", ["DE", "Panama", "Schottland"])

#Definiere eine leere Liste.
liste = []
            
# Füge jedes Tupel dieser leeren Liste bei und gib die Liste aus.
liste = [tupel1, tupel2, tupel3, tupel4]
print(liste)
          
# Wandle die Liste in ein Dictionary um und gib es aus.
dictionar = dict(liste)
print(dictionar)

# Füge dem Dictionary-Eintrag „Bereiste Länder“ die Länder Schottland, Guatemala und Kongo
# hinzu und gib diesen Eintrag aus.
dictionar["Bereiste Länder"].append("Schottland")
dictionar["Bereiste Länder"].append("Kongo")
dictionar["Bereiste Länder"].append("Guatemala")

print(dictionar["Bereiste Länder"])

# Schottland kommt nun doppelt vor. Wandle die Liste in eine Liste um,
# in der jedes Element nur einmal vorkommt, und erneuere den Eintrag im Dictionary. Gib das Ergebnis dann aus.
countries = list(set(dictionar["Bereiste Länder"]))
dictionar["Bereiste Länder"] = countries
print(dictionar["Bereiste Länder"])
print(dictionar)
