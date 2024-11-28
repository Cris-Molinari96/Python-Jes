
pict = makePicture(pickAFile())


# La funzione crea dei rettangoli neri oscurando gli occhi
#@ param picture: Picture
#@param: xMin,xMax, yMin, yMax : int
def functionPrivacy(picture,xMin, xMax, yMin, yMax):
    for x in range(xMin, xMax):
      for y in range(yMin, yMax):
        pixel = getPixel(picture, x,y)
        blackC = makeColor(0,0,0)
        setColor(newPixel, blackC)
    show(picture)


# Effetto mirror verticale, dividiamo a metà la larghezza della matrice
# accedendo ai px sia nella parte sx che dx
def mirrorVerticale():
    w = getWidth(pict)
    for y in range(getHeight(pict)):
      for x in range(w/2):
        pixel = getPixel(pict, x,y)
        newPixel = getPixel(pict, getWidth(pict)-x-1,y)
        setColor(newPixel, getColor(pixel))
    show(pict)

mirrorOrizzontale()


# function decrementa la componente rossa di tutti i px
#@ return void
def functionGeneralToChangeColor():
    picture = makePicture(pickAFile())
    sequencePixels = getPixels(picture)
    for i in range(0, len(sequencePixels)):
      setRed(sequencePixels[i], 255 - getRed(sequencePixels[i]))
    show(picture)


# Questa funzione oltre a dare un effetto di ribaltamento verticale crea un effetto negativo.
# l'effetto negativo si ottiene facendo la differenza, 255 - la componente rgb per ogni px

def varianteMirrorRibaltatoVerticale(picture):
    middle = getWidth(picture)/2

    for y in range(getHeight(picture)):
      for x in range(middle):
        pixelLeft = getPixel(picture, x,y)
        pixelRight = getPixel(picture, getWidth(picture)-x-1,y)
        rLeftColor = getRed(pixelLeft)
        rColorLeftNew = 255 - rLeftColor
        gLeftColor = getGreen(pixelLeft)
        gColorLeftNew = 255 - gLeftColor
        bLeftColor = getBlue(pixelLeft)
        bColorLeftNew = 255 - bLeftColor
        rRightColor = getRed(pixelRight)
        rColorRightNew = 255 - rRightColor
        gRightColor = getGreen(pixelRight)
        gColorRightNew = 255 - gRightColor
        bRightColor = getBlue(pixelRight)
        bColorRightNew = 255 - bRightColor

        leftNegativeColor = makeColor(rColorLeftNew,gColorLeftNew,bColorLeftNew)
        rightNegativeColor = makeColor(rColorRightNew,gColorRightNew,bColorRightNew)

        setColor(pixelRight,rightNegativeColor)
        setColor(pixelLeft, leftNegativeColor)


    show(picture)


varianteMirrorRibaltatoVerticale(picture)


# La funzione vuole consolidare il ragionamento logico:
# Recuperiamo i pixel di sinistra e i pixel di destra e poi di questi pixel recuperiamo il colore
# il colore dei pixel della parte dx sovrascrive il colore dei px di sx e quelli di sx sovrascrivono quelli di dx
# abbiamo ancora un effetto specchio ma al contrario
# p : Picture
def mirrorRibaltato(p):
# divedere verticalmente in due l'immagine
    middlePoint = getWidth(p)/2
    for y in range(getHeight(p)):
      for x in range(middlePoint):

        pixLeft = getPixel(p,x,y)
        #Questo passaggio è essenziale per accedere alla parte di destra che è stata dimezzata
        pixRight = getPixel(p, getWidth(p)-x-1,y)
        colorPixRight = getColor(pixRight)
        colorPixLeft = getColor(pixLeft)
        setColor(pixLeft, getColor(pixRight))
        setColor(pixRight, getColor(pixLeft))
    show(p)


# Effetto specchio orizzontale
#@param picture: Picture
def mirrorOrizzontale(picture):
    h = getHeight(pict)
    for x in range(getWidth(pict)):
      for y in range(h/2):
        pixel = getPixel(pict, x,y)
        newPixel = getPixel(pict, x, getHeight(pict)-y-1)
        setColor(newPixel, getColor(pixel))

    show(pict)