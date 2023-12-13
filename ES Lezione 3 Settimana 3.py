import math

def calcPerimetroQuad(lato):
    return 4 * lato

def calcPerimetroCerc(raggio):
    return 2 * math.pi * raggio

def calcPerimetroRett(base, altezza):
    return 2 * (base + altezza)    

while True:
    print("Scegli una figura geometrica:")
    print("1. Quadrato")    
    print("2. Cerchio")
    print("3. Rettangolo")

    scelta = input("Inserisci il numero che corrisponde alla figura desiderata:")

    if scelta == "1":
       lato = float(input("Inserisci la lunghezza del lato del quadrato:"))
       perimetroQuad = calcPerimetroQuad(lato)
       print(f"Il perimetro del quadrato è: {perimetroQuad}")
    elif scelta == "2":
       raggio = float(input("Inserisci il raggio del cerchio:"))
       perimetroCerc = calcPerimetroCerc(raggio)
       print(f"Il perimetro del cerchio è: {perimetroCerc}")   
    elif scelta == "3":
       base = float(input("Inserisci la base del rettangolo:"))
       altezza = float(input("Inserisci l'altezza del rettangolo:"))
       perimetroRett = calcPerimetroRett(base, altezza)
       print(f"Il perimetro del rettangolo è: {perimetroRett}")  
    else:
       print("Arrivederci")
       break

   