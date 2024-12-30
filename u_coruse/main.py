list = [10,2,5,1,4,9,23,84]


# Dividiamo a metà un array,
# Ottenuto il numero intero derivato dalla divisione len(sequenza) // 2 accediamo alle parti divise con lo slicing
def divide(l:list):
    arr = len(l) // 2
    print(f" parte sinistra {l[:arr]}, parte destra --> {l[arr:]}")
    right = divide()


# slicing
# print(list[1:])
# divide(list)

# Una funzione ricorsiva segue una strategia precisa:
# 1. Caso base ovvero il problema è cosi semplice che può essere risolto direttamente
# 2. La funzione chiama sè stessa per ottenere input del problema più piccoli
def fattoriale(n:int):
    print()
    if n <= 1:
        return 1
    return n * fattoriale(n-1)

print(fattoriale(5))


# Scrivere una funzione ricorsiva in 3 step:
# Sequenza di Fibonacci e come funziona:
#       Dato un numero n, la funzione decrementa quel numero dopo ogni chiamata
#   1. Individuare il problema è programmare un caso base che è la risoluzione poi delle chiamate dallo "stack"

def fibRicorsiva(n:int):
    if 1 < n:
        return n



# Come possiamo vedere con un ciclo è possibile ottenere lo stesso risultato di una funzione ricorsiva
def fib(n:int):
    sum = 0
    c = 0
    while c <= n:
        sum += c
        print(f"{sum} + {c}")
        c+=1
    print(sum)
fib(5)