path = "C:/test/test.txt"

# In generale per leggere e scrivere su un file:
# Leggere un file
# Uso di strip()    --> elimina gli spazi tra una riga e l'altra
def readFile(path):
    file = open(path,"r")

    for line in file:
      print(line.strip())
    file.close()

# Scrivere su un file
def writeOnFile(path):
    file = open(path,"w")
    file.write(" Scrivo qualcosa nelfile")
    file.close()
    readFile(path)

# writeOnFile(path)

path = "C:/test/test.txt"



# L'esercizio 1 proprosto viene spiegato nel file spiegazione-esercizi

prov = "Le bugie hanno le gambe corte. Le menzogne si scoprono subito, hanno le gambe corte e non possono andare lontano."

#@param path: String
#@param st: String
#@param mode: mode open file String
def writeOnFile(path,st, mode="w"):
    file = open(path,mode)
    file.write(st)
    file.close()
    pari = "C:/test/pro-pari.txt"
    disp = "C:/test/pro-dispari.txt"
    readOnFile(path,pari,disp)

#@param path: String
#@param pathPari: String
#@param pathDisp:  String 
def readAndWriteOnFile(path,pathPari,pathDisp):
    file = open(path,"r")
    pari = open(pathPari,"w")
    disp = open(pathDisp,"w")

    row =0
    for line in file:
      for i in range(0,len(line)):
        if i % 2 == 0:
          pari.write(line[i])
        else:
          disp.write(line[i])
      row +=1
    pari.close()
    disp.close()
    file.close()

# writeOnFile(path,prov)


# Esercizio 2, spiegazione nel file esercizi
# @param path : String
 def myInput(path):
    file = open(path,"w")
    s = ""
    while s != "fine":
        s = raw_input("Inserire un testo: ")          # --> Stiamo memorizzando ciò che viene inserito da terminale
        if s != "fine":
            file.write( str(s +" "))                                               # scriviamo sul file
    file.close()

# myInput(path)


# La funzione,  a partire da un filepath che viene come parametro, apre una connessione con il file in modalità di default(lettura/read)
# inizializza una lista che conterrà il contenuto del file
# strip() elimina righe vuote dal file restituendo tutto il contenuto
# split(",") restituisce per ogni linea una  lista contente il contenuto delle singole linee, ogni volta che termina una riga inserisce il contenuto nella lista
    # la lista è cosi formata per ogni linea lista_splittata = [contenuto_1_riga] , [contenuto_2_riga] e cosi via....
    # Importante notare che split retituisce listE di stringhe
# Infatti per mantenere la coerenza del file (già sappiamo la struttura del file ovvero che i primi 4 elementi sono n reali )
    # allora definiamo una logica che permetta di aggiornare il contenuto della lista splittata quindi della linea in un numero che essendo
    # decimale viene invocata la funzione float
#La funzione restituisce il contenuto delle linee mantenedo la coerenza con numeri e stringhe
def getIris(pathfile):
#@param pathfile: str
    f = open(pathfile)
    list = []

    for line in f:
      l = line.strip()
      s = l.split(",")
      for i in range(4):
        s[i] = float(s[i])
      list.append(s)
    print(list)
    return list
getIris(iris)

# La funzione prende in ingresso la lista precedentemente lavorata, la specie del fiore e un attributo per restituire una media finale
# La logica che ci interessa è calcolare la media:
# 1. per poterlo fare dobbiamo essere in grado di accedere alla lista e filtrarla secondo il parametro specie
# 2. accededere all'attributo che ci interessa recuperandone il valore per ogni fiore e memorizzando
    # la somma in una variabile temporanea chiamata nel file tempMedia
#3. ritornare la media
def average(dataset, specie, attributo):
#@param dataset: List
#@param specie: Stringa
#@param attributo: int
#@ return float
    counterIris = 0
    j = attributo
    tempMedia = 0
    for s in dataset:
      if s[4] == specie:
        tempMedia += s[j]
        counterIris +=1
    return tempMedia