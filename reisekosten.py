# reisekosten.py

# print("Kostenplan für eine Reise")
print("---------------------------")
kosten = input("Kosten für den Reisebus: ")
hotelk = input("Hotelkosten pro Person: ")
gkosten = input("Gesamtkosten für touristische Events: ")
teilnr = input("Anzahl der Teilnehmer: ")

# Berechung der Reisekosten
ggkosten = int(kosten) + int(hotelk) * int(teilnr) + int(gkosten) 
print("Die Gesamtkosten betragen " + str(ggkosten) + " EUR. ")
ggkostenPerTeilnr = round(int(ggkosten) / int(teilnr),2)
print("Die Kosten pro Person sind "+ str(ggkostenPerTeilnr) + " EUR. ")
