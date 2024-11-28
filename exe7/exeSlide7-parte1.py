# Luminosità pià alta
# Spezziamo verticalemente l'immagine sommando le componenti di ciascun pixel della parte sx con ogni componente dei pixel della parte dx
def luminance(pic):
    luminancePiuAlta = 0
    xValue = 0
    yValue = 0
    w2 = getWidth(pic)/2 # Dividiamo in due parti l'immagine cosi da avere accesso e confrontare pixel diversi e non gli stessi
    for y in range(0,getHeight(pic)):
      for x in range(0,w2):
        px = getPixel(pic, x,y) # vengono recuperati i px di sx
        pxInverso = getPixel(pic, getWidth(pic)-x-1,y) # vengono recuperati i px di destra
        sumPixColor = (getRed(px)+ getGreen(px)+ getBlue(px))/3
        sumPixColorInverso = (getRed(pxInverso)+ getGreen(pxInverso)+ getBlue(pxInverso))/3

        if sumPixColorInverso > luminancePiuAlta:
          luminancePiuAlta = sumPixColorInverso
          xValue = getX(pxInverso)
          yValue = getY(pxInverso)

        if sumPixColor > luminancePiuAlta:
          luminancePiuAlta = sumPixColor
          xValue = getX(px)
          yValue = getY(px)

    return xValue,yValue # ritora il pixel che ha luminosità più alta


# Vogliamo copiare un immagine più piccola in un'immagine più grande, spiegazione nel file txt
def copyAndCut(pPiccola, pG, xMin,yMin):
    w = getWidth(pG)
    h = getHeight(pG)
    for x in range(0,getWidth(pPiccola)):
      for y in range(0,getHeight(pPiccola)):
        xGMin = xMin + x
        yGMin = yMin + y
        if ( 0 <= xGMin < w) and (0 <= yGMin < h):
          pxG = getPixel(pG, xGMin, yGMin)
          pxP = getPixel(pPiccola, x,y)
          setColor(pxG, getColor(pxP))
    show(pG)


# Effetto griglia disegnare una linea verticale e una orizzontale ogni nValue pixel
# Iteriamo prima sulle colonne volta iteriamo sulle colonne e poi sulle righe
def griglia(p):
    def griglia(p):
    for x in range(0,getWidth(p),2):
      for y in range(0,getHeight(p)):
        px = getPixel(p,x,y)
        setColor(px, makeColor(0,0,0))

    for y in range(0,getHeight(p),10):
      for x in range(0,getWidth(p)):
        setColor(getPixel(p,x,y), makeColor(255,0,0))

    show(p)

# Se la somma delle di x e y è pari allora modifica i pixel
#@param pic: Picture
#@param col: Color
def checkXYEven(pic, col):
    for x in range(0,getWidth(pic)):
      for y in range(0,getHeight(pic)):
        if (x+y) % 2 == 0:
          px = getPixel(pic, x,y)
          setColor(px, col)
#subColorPixel(pic, makeColor(255,0,0))



#Accedere alle righe con la funzione getX e y con la funzione getY
def varianteToAccessWidthAndHeight(picture=chargePicture()):
#@param picture: Picture
    for i in getPixels(picture):
      x = getX(i)
      y = getY(i)
      pix = getPixel(picture,x,y)
      setColor(pix, makeColor(0,0,0))
    show(picture)


#Ritornare una tupla
def returnTrueFalse(picture,color):
    listPixel=getPixels(picture)
    h = getHeight(picture)
    w = getWidth(picture)

    count = 0
    for x in range(0, w):
      for y in range(0,h):
        pixelColor = getColor(getPixel(picture, x,y))
        if pixelColor == color:
          count += 1
          print count
          return (True,x,y)



#Settare al posto dei bianchi un colore arancione o verde
# 1. ottenere l'oggetto Picture
# 2. ottenere la lista dei pixel
# 3. iterare la lista accedendo ai singoli pixel
# Ci sono due modi per accedere ai pixel:
#   -* listPixel[i] -** getPixel(picture,x,y)
#   questo comporta un ciclo con un counter i e il secondo due cicli uno dentro l'altro
# 4. settare il clore dei pixel quindi direi che possiamo farlo anche con un unico ciclo
def orangeIsTheNewWhite(picture, color):
    listPixel=getPixels(picture)

    for i in range(0,len(listPixel)):
      pixelColor = getColor(listPixel[i])
      if pixelColor == white:
        setColor(listPixel[i], color)
    show(picture)

# orangeIsTheNewWhite(chargePicture(), makeColor(0,255,0))
# Ritornare la posizione dei pixel bianchi:
# Soliti passaggi, dalla picture che ?? una matrice di pixel,
# iterarla accedendo ai singoli pixel recuperandone il colore
# per ritornare la posizione c'?? bisogno di creare due for x e y annidati
#@param picture: Picture
#@param color: Color
def returnXYPixelWthite(picture, color):
    count = 0
    listPix = getPixels(picture)
    for x in range(getWidth(picture)):
      for y in range(getHeight(picture)):
        pixel = getPixel(picture, x,y)
        colorPix = getColor(pixel)
        if colorPix == color:
          count += 1
          print(str(x) + " " + str(y) + " " + str(count))


# returnXYPixelWthite(chargePicture(), makeColor(255,255,255))
# Contare i pixel secondo un parametro color
# 1. recuperare tutti i pixel dell'immagine salvandoli in una varabile
# 2. iterare sulla lista
# 3. accedere ai singoli pixel
# 4. recuperare il color dei pixel
# 5. confrontarlo con un color
def countColor(picture, color):
#@param1 picture: Picture obj
#@param2 color: Color obj
    count = 0
    listPix = getPixels(picture)
    for i in range(0, len(listPix)):
      colorPix = getColor(listPix[i])
      if colorPix == color:
        count += 1
    print count

# Contare il numero di pixel bianchi in un'immagine
# 1. iterare su una lista di pixel
# 2. recuperare il singolo colore di ogni pixel
# 3. confrontarlo con il colore bianco precedentemente creato
def countWhite(pict):
    count=0
    listPix = getPixels(pict)
    whiteC = makeColor(255,255,255)
    for i in range(0,len(listPix)):
      pixelColor = getColor(listPix[i])
      if pixelColor == whiteC:
        count += 1
    print count


def countWhiteVariante(pict):
    count=0
    listPix = getPixels(pict)
    for x in range(0,getWidth(pict)):
      for y in range(0, getHeight(pict)):
        pixel = getPixel(listPix[i], x,y)
        colorPixel = getColor(listPix[i])
        if pixelColor == white:
          count += 1
          print(count,x,y)
          return count,x,y


