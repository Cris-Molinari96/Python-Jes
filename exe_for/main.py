#  Esercizi iterazione
import random
list = ["A","B","C","D"]
l2=[["item"],["name"]]

# for item in enumerate(list):
#     print(item)


# Stampa tutti gli item della lista tranne il primo
def func(sequence:list):
        for indice, item in enumerate(sequence):
            if indice != 1:
                print(f"{indice}, {item}")

def func2(sequence:list):
    for i,item in enumerate(sequence):
        if i == 1:
            continue
        print(f"{i}, {item}")

def a(seq:list):
    for i in range(len(seq)):
        for j in range(len(seq[i])):
            for char in seq[i][j]:
                print(char)

# Pari o dispari?
def evenOrNot():
    for i in range(21):
        if i % 2 == 0:
            print(f"numero pari --> {i}")
        else:
            print(f"numero dispari --> {i}")

def sum():
    x = 0
    sum = 0
    while x < 200:
        sum += x
        x+=1
        if x >= 100:
            break
    return sum

# Il fattoriale di un numero
def factorialNumber(n:int):
    c  = 0
    fact = 1
    number = n
    if n == 1:
        return 0
    while c <= n:
        if number == 0:
            break
        fact *= number
        number -=1
        c+=1
    return fact

# Ciclo annindato per moltiplicare per ogni iterazione di i ogni incremento di j da 1 a 10
def tav_pitagorica():
    list =[]
    for  i in range(1,11):
        tempList = []
        for j in range(1,11):
            sum = i * j
            tempList.append(sum)
            if j == 10:
                list.append(tempList)
    return list

# dato un numero in input stampa il numero di cifre del numero
def countCifra():
        num = input("inserisci un numero: " )
        print(f"il numero che hai inserito ha: {len(num)} cifre")

# stampa n trinagoli
def triangoli(n:int):
    for i in range(0,(n+1)):
        print("*" * i)

# random() la funzione genera un numero randomico float a 18 cifre compreso tra 0 e 1
# è possibile trasofrmare in un numero intero int(1<x<10) molptiplicando il ritorno per 10,
# ciò che restituisce è sempre un numero double quindi dobiamo castare in intero il risultato
def populateLista():
    lista = []
    for i in range(11):
        n = int(random.random() * (random.random()*10))
        lista.append(n)
    list_num_string = map(str,lista)
    for i in list_num_string:
        print(type(i))


    print(lista)
populateLista()


