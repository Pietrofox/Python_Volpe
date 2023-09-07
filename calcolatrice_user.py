import math

class Calcolatrice:
    def somma(self, a, b):
        return a + b
    
    def sottrazione(self, a, b):
        return a - b
    
    def moltiplicazione(self, a, b):
        return a * b
    
    def divisione(self, a, b):
        if b == 0:
            return "Impossibile dividere per zero"
        return a / b
    
    def potenza(self, base, esponente):
        if (isinstance(base, (int, float)) and isinstance(esponente, (int, float))) or (isinstance(base, str) and isinstance(esponente, str)):
            base = float(base)
            esponente = float(esponente)
            return base ** esponente
        else:
            return "Entrambi i parametri devono essere numeri (int o float) o stringhe numeriche"
    
    def radice(self, base, esponente):
        if (isinstance(base, (int, float)) and isinstance(esponente, (int, float))) or (isinstance(base, str) and isinstance(esponente, str)):
            base = float(base)
            esponente = float(esponente)
            if base < 0 and esponente % 2 == 0:
                return "Impossibile calcolare la radice di un numero negativo con esponente pari"
            return base ** (1 / esponente)
        else:
            return "Entrambi i parametri devono essere numeri (int o float) o stringhe numeriche"
    
    def modulo(self, a, b):
        return a % b
    
    def conversione_base(self, numero, base_origine, base_destinazione):
        try:
            numero_intermedio = int(numero, base_origine)
            numero_convertito = format(numero_intermedio, f'0{base_destinazione}b')
            return numero_convertito
        except ValueError:
            return "Errore di conversione"

# Richiedi all'utente di inserire i due valori
valore1 = input("Inserisci il primo valore: ")
valore2 = input("Inserisci il secondo valore: ")

# Richiedi all'utente di scegliere l'operazione
print("Scegli l'operazione:")
print("1. Somma")
print("2. Sottrazione")
print("3. Moltiplicazione")
print("4. Divisione")
print("5. Potenza")
print("6. Radice")
print("7. Modulo")
print("8. Conversione di base")

scelta = input("Inserisci il numero dell'operazione scelta: ")

# Esempi di utilizzo della classe Calcolatrice
calc = Calcolatrice()

# Effettua l'operazione scelta con i valori inseriti
try:
    valore1 = float(valore1)
    valore2 = float(valore2)

    if scelta == "1":
        risultato = calc.somma(valore1, valore2)
    elif scelta == "2":
        risultato = calc.sottrazione(valore1, valore2)
    elif scelta == "3":
        risultato = calc.moltiplicazione(valore1, valore2)
    elif scelta == "4":
        risultato = calc.divisione(valore1, valore2)
    elif scelta == "5":
        risultato = calc.potenza(valore1, valore2)
    elif scelta == "6":
        risultato = calc.radice(valore1, valore2)
    elif scelta == "7":
        risultato = calc.modulo(valore1, valore2)
    elif scelta == "8":
        risultato = calc.conversione_base("1010", 2, 10)
    else:
        risultato = "Scelta non valida"
    
    print("Risultato:", risultato)

except ValueError:
    print("Inserisci valori numerici validi.")
