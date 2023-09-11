#classi by PietroVolpe

class Persona:
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome
    def bonjour(self):
        print(self.ruolo, ":", self.nome, self.cognome)

class Studente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Sudente UNITS", nome, cognome)
        self.corsi = corsi
    def bonjour(self):
        super().bonjour()
        for corso in corsi:
            print("> Frequenta :", corso)

class Docente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Docente UNITS", nome, cognome)
        self.corsi = corsi
    def bonjour(self):
        super().bonjour()
        for corso in corsi:
            print("> Docente del corso :", corso)

def coperto(Studente, docenti):
    lista_corsi = Studente.corsi
    for docente in docenti:    
        for corso in docente.corsi:
            if corso in lista_corsi:
                lista_corsi.remove(corso)
    if lista_corsi:
        for corso in lista_corsi:
            print("Corso non coperto:", corso)
    else:
        print("Tutti i corsi sono coperti.")

docenti = []
studenti = []
corsipietro = ["Programmazione", "Laboratorio", "Analisi", "Geometria", "Geostoria"]
corsimati = ["Storia", "Laboratorio", "Analisi", "Fisica"]
corsigefra = ["Programmazione", "Laboratorio", "Analisi", "Geometria"]

pi_obj = Studente("Pietro", "Volpe", corsipietro)
studenti.append(pi_obj)
first_doc = Docente("Matilde", "Nosei", corsimati)
docenti.append(first_doc)
second_doc = Docente("Francesco", "Gennario", corsigefra)
docenti.append(second_doc)

coperto(pi_obj, docenti)