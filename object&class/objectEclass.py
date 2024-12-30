class MyClass:
    # Attributi
    localname = "codice1"
    listArgs = []
    counter = 0

# Costruttore __init__()
    # -self assegna il parametro passato quando viene invocata la funzione di istanza di classe e assegna
    # a listArgs il valore del parametro (self fà riferimento alla classe stessa) un pò come this in java
    # ma in python dev'essere sempre esplicitato.
    def __init__(self,*args):
        MyClass.counter +=1
        self.listArgs = args



# Metodi di istanza
    def printList(self):
        for arg in self.listArgs:
            print(arg)

# Il metodo getCounter dovrebbe avere il decoratore di classe e non essere definito in questo modo,
# non è logico usare questo metodo sulle istanze poichè servirebbe a ben poco mentre
 # se applicato alla classe stessa e non all'istanza ha più senso.
 #    def getCounter(self):
 #        return self.counter

 # Metodi di classe:
    @classmethod
    def get_my_counter(cls):
        return cls.counter -1


# Non è la miglior cosa da fare ma può essere fatta giusto per saperlo
# puoi creare n classi e n metodi usabili solo se importando il file.
class MyClass2:
    name = ""

    def __init__(self,name):
        self.name = name






