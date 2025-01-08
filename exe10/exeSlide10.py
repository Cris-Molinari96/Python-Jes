
# Le liste partono da un indice che ha posizione 0 ciò significa che il primo elemento della lista
# è in posizione 0 e terminano con un intero sempre positivo.
# Oppure possono partire da -(len(lista)) ad esempio Strawberries è in posizione 0 e in posizione -7

fruit_list = ["Strawberries", # -7
              "Nectarines", # -6
              "Apples", # -5
              "Grapes",  # -4
              "Peaches", # -3
              "Cherries", # -2
              "Pears"] # -1

print(fruit_list[-1])

# Sequenze(Liste,Tuple,Stringhe), Set e Dizionari

# L'esercizio proprosto ci chiede di tornare una lista di tutte
# le persone che sono nate in uno stesso posto
#persons = [{x
#'name':'peppe',
#'surname':'MagicoPepp',
#'email':'peppeilmagic@ep.it',
#'city':'Sicilia',
#},{
#'name':'Mario',
#'surname':'Rossi',
#'email':'rossiMario@mario.com',
#'city':'Sicilia',
#},{
#'name':'nero',
#'surname':'Giardini',
#'email':'giardini@ne.it',
#'city':'Sicilia',
#}]





# { *****
#Aggiunta dinamica di elementi alla lista:
myList = []

# Aggiunge dinamicamente elementi alla lista
def addList(l):
    for i in range(0,11):
        l.append(i)
    return l

# La funzione restituisce una lista riordinata inversamente
def algReverse(l):
    reverseList = []
    for i in range(len(l)-1,-1,-1):
        reverseList.append(l[i])
    return reverseList

def combinaLePrimeDue(l):
    list = algReverse(addList(l))
    print(list)

combinaLePrimeDue(myList)
# ***** }


