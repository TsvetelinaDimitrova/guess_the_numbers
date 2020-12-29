#erraten.py
print("Erraten Sie eine Zufallszahl zwischen 1 und 100 in so weniger Versuchen wie möglich.")
from random import randint
def spiel():
    secretNumber = randint(1, 100)
    #print(secretNumber)
    myZahl = int(input("Wie lautet Ihr Ratenversuch? : "))
    i = 0
    while myZahl != secretNumber:
        if myZahl < secretNumber:
            print("Versuch", i+1, ": Die zu erratende Zahl ist größer")
            myZahl = int(input("Wie lautet Ihr Ratenversuch? : "))
        else:
            print("Versuch", i+1, ": Die zu erratende Zahl ist klein")
            myZahl = int(input("Wie lautet Ihr Ratenversuch? : "))
        i = i + 1
    print("Sie haben die Zahl in", i+1, "Versuchen erraten")
spiel()

nochmal = input("Wollen Sie nochmal spielen? (ja oder nein) : ") 
while nochmal == "ja":
    spiel()
print("Vielen Dank fürs Spielen")
input("Beenden mit Eingabetaste")