class Modello():
    def __init__(self, nome, descrizione):
        self.nome = nome
        self.descrizione = descrizione

    def modifica_descrizione(self, nuova_desc):
        self.descrizione = nuova_desc
        print("\n Descrizione modificata correttamente !")

    def stampa_modello(self):
        print("Nome: %s\nDescrizione: %s\n\n" %(self.nome, self.descrizione))


