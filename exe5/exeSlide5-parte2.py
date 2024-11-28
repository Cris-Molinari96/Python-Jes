#### Linee

# La funzione crea una linea di un certo spessore definito dai parametri x,y.
# I parametri oltre a definire lo spessore della linea, definisce anche la posizione
# In realtà vediamo un effetto di linea ma è dato sempicilemente dal cambiare il colore dei pixel
def lineSpesse(picture, xMin, xMax, yMin,yMax):
    for x in range(xMin,xMax):
      for y in range(yMin,yMax):
        setColor(getPixel(picture, x,y), makeColor(0,0,0))
    show(picture)

# Viene dato l'effetto di una linea orizzontale che divide l'immagine in due
# In questo modo possiamo vedere come viene divisa l'immagine in due parti
def lineaOrizCentro(picture, xMin, xMax):
    y = getHeight(picture)/2
    blackC = makeColor(0,0,0)
    for x in range(xMin, xMax):
      setColor(getPixel(picture, x, y), blackC)
    show(picture)

#@param picture: Picture
#@param2 y: int
def lineaVerticale(picture,nextStep):
    h = getHeight(picture)
    spacing = nextStep
    whiteC = makeColor(0,255,0)
    for x in range (0, getWidth(picture), spacing ):
      for y in range(0, h, spacing):
        setColor(getPixel(picture, x, y), whiteC)
    show(picture)


lineaVerticale(makePicture(pickAFile()),2)


def lineaOrizzontale(picture, y):
    #@param1: Picture
    #@param2 y: int
    #@return: void
    for x in range(getWidth(picture)):
      pix = getPixel(picture, x,y)
      blackC = makeColor(0,0,0)
      setColor(pix, blackC)
    show(picture)




