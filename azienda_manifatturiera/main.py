class Modello():
    def __init__(self, nome_modello, descrizione):
        self.nome_modello = nome_modello
        self.descrizione = descrizione

    def modifica_descrizione(self, nuova_desc):
        self.descrizione = nuova_desc
        print("\nDescrizione modificata correttamente !")

    def stampa_modello(self):
        print("\nNome: %s\nDescrizione: %s\n" %(self.nome_modello, self.descrizione))

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

    

modello1 = Modello("plastica", "modello utile per creare piccole strutture solide")    
modello2 = Modello("alluminio", "modello utile per creare fili conduttori di elettricità")    


modello1.stampa_modello()
modello1.modifica_descrizione("modello utile per creare piccole strutture geometriche")
modello1.stampa_modello()


dipartimento1 = Dipartimenti("edilizia")


dipartimento1.aggiungi(modello1)
dipartimento1.aggiungi(modello2)
dipartimento1.stampa_dipartimenti()
