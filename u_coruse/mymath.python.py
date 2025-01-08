# Operatori che concenstono le operazioni matematiche:
# + , -, /, //, *, **, %(operatore modulo, controllo sul resto 5%2 stampa 1)

def calculator():
    start = input("Welcome in my calculator, if you start calculator write start in input ")
    while start != "end":
        operation = input("Can you do? sum, difference, product or division?\nSelect one operation ")
        if operation == "sum":
            my_sum()
        elif operation == "difference":
            differecnce()
        elif operation == "product":
            product()
        elif operation == "division":
            division()
        start = input("Stop programm write end")

def my_sum():
    x = float(input("first number "))
    y = float(input("second number "))
    print(x + y)

def differecnce():
    x = float(input("first number "))
    y = float(input("second number "))
    print(x - y)

def product():
    x = float(input("first number "))
    y = float(input("second number "))
    print(x * y)

def division():
    x = float(input("first number "))
    y = float(input("second number "))
    print(x / y)

#calculator()


# Scrivere una funzione che stampi il numero di lettere del tuo nome passato in input al programma:
def printNumberName():
    print("Your name have n° " + str(len(input("Write your name!\n"))) + "char")

#printNumberName()

# Possiamo elevare a potenze con il doppio asterisco (**)
def potenze(n:int,m:int):
    print(n**m)
# potenze(2,3)

def useRound():
    print(100/33)
    print(round(100/32))


def tipCalculator():
    print("Welcome in my custom calculator of tips!")
    total_bill = float(input("Insert the import of total bill "))
    tip = float(input("how much tip would you like to give in €? "))
#Aggiungere la mancia alla spesa finale
    total_bill += tip
    number_person = float(input("How many people to split the bill? "))
    print(f"The total bill plus tip = {round(total_bill / number_person, 2)}€")
#tipCalculator()


print(4 % 2)
