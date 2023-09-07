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

# Esempi di utilizzo della classe Calcolatrice
calc = Calcolatrice()

print("Somma:", calc.somma(5, 3))
print("Sottrazione:", calc.sottrazione(10, 4))
print("Moltiplicazione:", calc.moltiplicazione(7, 6))
print("Divisione:", calc.divisione(20, 4))
print("Potenza:", calc.potenza(2, 3))
print("Radice:", calc.radice(16, 4))
print("Modulo:", calc.modulo(15, 7))
print("Conversione di base:", calc.conversione_base("1010", 2, 10))
