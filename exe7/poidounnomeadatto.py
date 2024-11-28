## Logica di ripasso:
# iterare si una matrice

emptyPic = makeEmptyPicture(100, 100, white)

# La funzione dimostra come è possibile accedere all'ultimo valore della riga
# arrivati a metà cambia il colore
def coloraLaPrimaRiga(p):

    h = getHeight(p)
    for x in range(getWidth(p)-1,-1,-1):
      setColor(getPixel(p,x,0), makeColor(0,0,0))
      if(x >= 0 and x <= 50):
        setColor(getPixel(p,x,0), makeColor(255,0,0))
    show(p)


# La funzione dimostra che accediamo alla prima colonna quindi x = 0 partendo dall'ultima riga y = 99
def coloraLaPrimaColonna(p):
    p = makeEmptyPicture(100, 100, white)
    h = getHeight(p)
    for y in range(getHeight(p)-1,-1,-1):
      setColor(getPixel(p,0,y), makeColor(0,0,0))
      if(y >= 0 and y <= 50):
        setColor(getPixel(p,0,y), makeColor(255,0,0))
    show(p)

# Bisogna accedere alla prima colonna muoverci verso destra la x incrementa
# Bisogna accedere alla prima riga e muoverci verso il basso la y incrementa e sfruttare questa formula
# getHeight(p) * x // getWidth(p) --> // restituisce sempre un intero
def diagonalePrincipale():
    p = makeEmptyPicture(100,120)
    for x in range(0,getWidth(p)):
      print"e"
      y=(getHeight(p) * x) // getWidth(p)
      if y < getHeight(p):
        setColor(getPixel(p,x,y), makeColor(0,255,255))

# Bisogna accedere all'ultima colonna e muoverci verso sinistra qunidi la x decrementa
# Bisogna accedere alla prima riga e muoverci verso il basso la y incrementa e sfruttare questa formula
# getHeight(p) * (getWidth(p)-1-x) // getWidth(p) --> // restituisce sempre un intero
def diagonaleSecondaria(p):
    print getHeight(p)
    for x in range(getWidth(p)-1,-1,-1):
      y = (getHeight(p) * (getWidth(p)-1 -x)) // getWidth(p)
      setColor(getPixel(p,x,y), makeColor(255,0,0))
    show(p)


# Unione delle due funizoni sopra proposte
def diagonalePrincipaleESecondaria():
    p = makeEmptyPicture(120,100)
    for x in range(0,getWidth(p)):
      print"e"
      y=(getHeight(p) * x) // getWidth(p)
      if y < getHeight(p):
        setColor(getPixel(p,x,y), makeColor(0,255,255))

    for x in range(getWidth(p)-1,-1,-1):
      y = (getHeight(p) *(getWidth(p)-1-x)) // getWidth(p)
      if y < getHeight(p):
        setColor(getPixel(p,x,y), makeColor(255,0,0))
    show(p)


# Recupera dai pixel in cui la diagonale è passante la quantità di rosso
# Recupera da una riga della seconda immagine la componente di rosso pezr ogni px e sommali
# Verifica sè la media della somma delle componenti di rosso dei pixel è presente nella prima immagine
def checkRedInDiagonale(p1,p2):
    tempList = []
    sum = 0
    counter =0
    for x in range(0,getWidth(p1)):
      y = (getHeight(p1) * x) // getWidth(p1)
      if y < getHeight(p1):
        tempList.append(getRed(getPixel(p1,x,y)))

    for x in range(0,getWidth(p2)):
      r = getRed(getPixel(p2,x,0))
      sum = sum + r
      counter += 1
    sum = sum // counter

    if sum in tempList:
      return True


# Somma le componenti g,b di un pixel e verifica se Esiste almeno un pixel che sia = alla somma
# Uso di liste temporenee o set per migliorare l'efficienza evitando duplicati inutili
def checkOnlyOneR(p):
    pxL = getPixels(p)
    for px1 in pxL:
      r = getRed(px1)
      for px2 in range(len(pxL)-1,-1,-1):
        if r == (getGreen(pxL[px2])+getBlue(pxL[px2])):
          return true
    return false



# Somma le componenti g,b di un pixel e verifica se Per ogni pixel è = alla somma
# Uso di liste temporenee o set per migliorare l'efficienza evitando duplicati inutili
def checkAllPxR(p):
    tempLR = set()
    tempLGB = set()
    pxL = getPixels(p)

    for px in pxL:
      tempLR.add(getRed(px))
      tempLGB.add(getGreen(px)+getBlue(px))
    for r in tempLR:
      if r not in tempLGB:
        return false
    return true
