# In tanto random in python è un modulo, possiamo dire che è un file contente n funzioni che generano un numero(intero,float) randomico.
# Possiamo sfruttare il modulo e le funzioni importando il modulo e accedendo ai metodi della classe Random con la dotnotation quindi
# es --> import random, random.random()
import random

# La seguente riga di codice genera un numero randomico da 1 a 100
random_number = random.random()*100

# La funzione round permette di, a partire da un numero ottenere un numero con n cifre decimali.
print(round(random_number,0))

# Si può certamente generare un qualsiasi numero compreso in un intervallo
number_uniform_number = random.uniform(1,4)
print(round(number_uniform_number,2))

# Random list First option
#choice, il metodo ti permette di applicare il concetto di randomizzazione sfruttanto il metodo definito nel modulo.
list_ex = ["Peppe","Franco","Claudio","Gaetano"]
name = random.choice(list_ex)
print(name)
# Random list Second option
# Un'alternativa sarebbe stata quella di generare un numero randomico compreso tra 0 e la len della lista e poi sfruttare
# le square brakets per accedere all'elemento della lista.
print(list_ex[random.randint(0,len(list_ex))])