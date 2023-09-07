import random

class Automa:
    def __init__(self):
        self.biancheria = None
        self.calzini = None
        self.maglia = None
        self.pantaloni = None
        self.calzatura = None
        self.test = 0

    def indossa_biancheria(self):
        # Simulazione di indossare la biancheria
        print("Automate: Sto indossando la biancheria.")
        self.biancheria = True
        self.test = self.test + 1

    def indossa_calzini(self):
        # Simulazione di indossare i calzini
        print("Automate: Sto indossando i calzini.")
        self.calzini = True
        self.test = self.test + 1

    def indossa_maglia(self):
        # Simulazione di indossare la maglia
        print("Automate: Sto indossando la maglia.")
        self.maglia = True
        self.test = self.test + 1

    def indossa_pantaloni(self):
        # Simulazione di indossare i pantaloni
        print("Automate: Sto indossando i pantaloni.")
        self.pantaloni = True
        self.test = self.test + 1

    def indossa_calzatura(self):
        # Simulazione di indossare la calzatura
        print("Automate: Sto indossando la calzatura.")
        self.calzatura = True
        self.test = self.test + 1

    def main(self):
        while not(self.biancheria and self.calzini and self.maglia and self.pantaloni and self.calzatura):
            azione = random.choice([
                self.indossa_biancheria,
                self.indossa_calzini,
                self.indossa_maglia,
                self.indossa_pantaloni,
                self.indossa_calzatura
            ])
            azione()

        print("Automate: Mi sono vestito con successo!")
        print("test sbagliati= ", self.test)

if __name__ == "__main__":
    automa = Automa()
    automa.main()


#tutti gli automate che escono sono i test falliti, lultimo che uscirà per forza solo il "Automate:mi sono vestito con successo" è corretto 
#ho inizializzato self.test a 0 per vedere quanti test sono necessari per far vestire correttamente l'automa