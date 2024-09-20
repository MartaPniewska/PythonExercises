# geld.py

# Zerlegung eines Geldbetrages (ganze Zahlen) in Scheine und Münzen
geld = input("Geldbetrag in Euro: ")
geld = int(geld)
hunderter = geld // 100
geld = geld % 100
fünfziger = geld // 50
geld = geld % 50
zwanziger = geld // 20
geld = geld % 20
zehner =geld // 10
geld = geld % 10
fünfer = geld // 5
geld = geld % 5
zweier = geld // 2
einer = geld % 2

# Ergebnis
print("Der Betrag setzt sich wie folgt zusammen:")
print(hunderter, "mal 100 Euro")
print(fünfziger, "mal 50 Euro")
print(zwanziger, "mal 20 Euro")
print(zehner, "mal 10 Euro")
print(fünfer, "mal 5 Euro")
print(zweier, "mal 2 Euro")
print(einer, "mal 1 Euro")