pic = makePicture(pickAFile("path"))

#Picture: è un oggetto in python, restituito dalla funzione makePicture la quale a partire da un immagine restituisce
# una matrice bidimensionale di pixel, bidimensionale perché ha una x larghezza e y lunghezza.

# La funzione vuole invocare diverse funzioni per incrementare o decrementare
# la quantità di un determinato colore
#@param pic: Picture
def sunsetVarianteGerarchica(pic):
    encreaseRed(pic,2)
    reduceGreen(pic,0.7)
    reduceBlue(pic, 0.7)
    show(pic)

# La funzione accede a tutti i pixel del bitmap per incrementare il valore rosso di n volte
#@param image: Picture
#@param nEncrease: Int
def encreaseRed(image, nEncrease):
    listPixel = getPixels(image)
    for px in listPixel:
      r = getRed(px) * nEncrease
      setRed(px,r)

# La funzione decrementa la componente vedere accedendo a tutti i pixel del bitmap
#@param image: Picture
#@param nDecrease: Int
def reduceGreen(image, nDecrease):
    listPixel = getPixels(image)
    for px in listPixel:
      g = getGreen(px) * valDecrease
      setGreen(px,g)

# La funzione decrementa la componente blu accedendo a tutti i pixel del bitmap
#@param image: Picture
#@param nDecrease: Int
def reduceBlue(image, valDecrease):
    listPixel = getPixels(image)
    for px in listPixel:
      g = getBlue(px) * valDecrease
      setGreen(px,g)

# La funzione viene invocata
sunsetVarianteGerarchica(pic)


# Effetto sunset
# Accedere alle singole componenti di ciascun pixel e modificarne i valori per un colore dell'immagine rossastro
#@param picture: Picture
def sunset(picture):
    listPixel = getPixels(picture)
    for px in listPixel:
      r = getRed(px) * 2
      g = getGreen(px) * 0.7
      b = getBlue(px) * 0.7
      color = makeColor(r,g,b)
      setColor(px,color)
    show(picture)

# Effetto grayScale / scala di grigi
# l'effetto si ottiene moltipilicando per 1.3 ciascuna componente (r,g,b)
# repaint salverà l'immagine modificata
#@param picture: Picture
def grayScale(picture):
    pixelList = getPixels(picture)
    for px in pixelList:
      r = getRed(i)
      g = getGreen(i)
      b = getBlue(i)
      myGray = 1.3*r+1.3*g+1.3*b
      grayColor = makeColor(myGray, myGray,myGray)
      setColor(i,grayColor)
    show(picture)
    repaint(picture)

# Vediamo una variante per accedere ai pixel di una matrice, la differenza è che usiamo la funzione range
# spiegazione di range nel file di testo della cartella
# decrementa il valore di ogni componente
#@param picture: Picture
def negativePicture(picture):
    sequencePixel = getPixels(picture)
    for i in range(0, len(sequencePixel)):
      orRed = getRed(sequencePixel[i])
      orBlue = getBlue(sequencePixel[i])
      orGreen = getGreen(sequencePixel[i])
      newRed = 255 - orRed
      newGreen = 255 - orGreen
      newBlue = 255 - orBlue
      color = makeColor(newRed,newGreen,newBlue)
      setColor(sequencePixel[i], color)
    repaint(imgDecresed) # la funzione repatin salva l'immagine modificata
    show(imgDecresed)

# Variante funzionante e simile a quella proposta di spora
#@param picture: Picture
def negativePictureVariante(picture):
    sequencePixel = getPixels(picture)
    for px in sequencePixel:
      r= getRed(i)
      g = getGreen(i)
      b = getBlue(i)
      setRed(i, 255-r)
      setGreen(i, 255-g)
      setBlue(i, 255-b)
    repaint(imgDecresed)
    show(imgDecresed)

# Variante, di come possiamo utilizzare funzioni componibili all'interno di altre funzioni
#@param picture: Picture
def apllicaFiltroDecreaseRedVariante2(picutre):
    sequence = getPixels(picutre)
    for i in range(0, len(sequence)):
      setRed(sequence[i], getRed(sequence[i]) * 0.5) # getRed() ad esempio è una funzione componibile -->
      #--> perchè ritorna la componente do Rosso di un dato pixel
    show(pict)

# Variante e modi diversi per accedere e manipolare i pixel di una matrice
#@param picture: Picture
def decreaseRedVariante1(picutre):
    listPixel = getPixels(picutre)
    for i in range(len(listPixel)):
      originalRed = getRed(listPixel[i])
      newRed = originalRed * 0.5
      setRed(listPixel[i], newRed)
    show(img)


# Variante e modi diversi per accedere e manipolare i pixel di una matrice
#@param picture: Picture
def apllicaFiltroDecreaseColorVariante(picture):
    listPixel = getPixels(picture)
    for i in range(0, len(listPixel)):
      color = makeColor(getRed(listPixel[i]) * 1.5,getGreen(listPixel[i]) * 1.5,getBlue(listPixel[i]) * 0.5)
      setColor(listPixel[i],color)
    show(img)

