class Modello():
    def __init__(self, nome_modello, descrizione):
        self.nome_modello = nome_modello
        self.descrizione = descrizione

    def modifica_descrizione(self, nuova_desc):
        self.descrizione = nuova_desc
        print("\n Descrizione modificata correttamente !")

    def stampa_modello(self):
        print("Nome: %s\nDescrizione: %s\n\n" %(self.nome, self.descrizione))

class Dipartimenti():
    def __init__(self, nome_dipartimento):
        self.nome_dipartimento = nome_dipartimento
        self.modelli = []

    def aggiungi(self, modello):
        self.modelli.append(modello)
        print("\nModello aggiunto correttamente !")

    def elimina(self, modello):
        if modello in self.modelli:
            self.modelli.remove(modello)
            print("\nModello rimosso con successo !")
        else:
            print("\nModello non presente !")

    def stampa_dipartimenti(self):
        for modello in self.modelli:
            modello.stampa_modello()

    

    