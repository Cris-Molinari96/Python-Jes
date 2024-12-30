#  objectEclass import di tutto il il contenuto del file assegnando un alias
import objectEclass as c
# importiamo dal file la classe specifica
from objectEclass import MyClass as c1
# un file contente solo metodi statici
import staticmethod.staticmethod as static
# import sotto classe
import inheritance as s

# Creando istanze della classe diverse obj1 != obj2
obj1 = c.MyClass("Code1018")
obj2 = c.MyClass2("Peppe")

# Accedere ad un metodo della classe
print(c.MyClass().get_my_counter())
# Accedere ad un'attributo della classe
print(obj2.name)

#Inovcare metodi statici
print(static.somma(2,4))
print(static.checkEven(2173))

# Super e sotto classi

#New example
class Item:
    list_item = []

#La funzione init viene richiamata ogni volta che si crea un istanza di un oggetto
    def __init__(self,name:str,price:int,quantity:int = 0):

        # validations to the received arguments
        assert price >= 0, f"You can't set a negative price {price}"
        assert quantity >= 0,f"You can't set a negative price {quantity} "

        # assign to self object
        self.name = name
        self.price= price
        self.quantity = quantity

        # self fa riferimento all'istanza stessa quando è stata creata e quindi
        # ha superato i controlli di validations e assegnazione
        Item.list_item.append(self)



    def calculate_total_price(self, x,y):
        return x * y

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity}"

item = Item("Iphone4",200, 2)
print(Item.list_item)


