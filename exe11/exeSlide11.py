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
#@param path : String
 def myInput(path):
    file = open(path,"w")
    s = ""
    while s != "fine":
        s = raw_input("Inserire un testo: ")          # --> Stiamo memorizzando ciò che viene inserito da terminale
        if s != "fine":
            file.write( str(s +" "))                                               # scriviamo sul file
    file.close()

# myInput(path)