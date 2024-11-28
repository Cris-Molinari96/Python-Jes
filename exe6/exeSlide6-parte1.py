picture = makePicture(pickAFile())


# La funzione decrementa la componente rossa per ogni pixel
#@param picture: Picture
def decreaseRed(picture):
    pixList = getPixels(picture)
    for i in range(0, len(pixList)):
      pix = pixList[i]
      newRed = getRed(pix) * 0.5
      setRed(pix, newRed)

# funzione che azzera la componente blu dall'immagine
# ed è un esempio di funzione componibile perché ritorna un valore.
#@param picture: Picture
def clearBlue(picture):
    pixList = getPixels(picture)
    for i in range(0, len(pixList)):
      pix = pixList[i]
      setBlue(pix, 0)
    return picture

#Vengono invocate le funzioni che
def modifyComponent(picutre):
    decreaseRed(picture)
    show(clearBlue(picture))


def infoPictHeightWidth(picture):
#param1: Picture
    h = getHeight(picture)
    w = getWidth(picture)
    print(str(h) + "x" + str(w))
