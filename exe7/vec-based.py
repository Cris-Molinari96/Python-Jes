def scacchiera():
    p = makeEmptyPicture(320,320)
    quadrato = 80
    color=white
    for x in range(0,getWidth(p),quadrato):
      for y in range(0,getHeight(p),quadrato):
        if (( x // quadrato) + (y // quadrato)) % 2 == 0:
          color = white
        else:
          color = black
        addRectFilled(p,x,y,quadrato,quadrato,color)


# Il punto è la formula altezza * indice della x // larghezza
def diagonalePrincipale(p):
    p = makeEmptyPicture(120, 100, white)

    # Disegno della diagonale principale
    for x in range(getWidth(p)):
      y = (getHeight(p) * x) // getWidth(p)
      setColor(getPixel(p, x, y), makeColor(0, 0, 0))

    show(p)

# Disegniamo metà della diagonale
def diagonaleInversa(p):
    p = makeEmptyPicture(120, 100, white)
    w = getWidth(p)/2
    h = getHeight(p)/2
    for x in range(w):
      y = (h * x)// w
      setColor(getPixel(p,x,y), makeColor(255,0,0))
    show(p)