# Il file è creato con lo scopo di esplorare la logica e sperazione delle responsabilità
# in particolare contiene metodi statici non legati ad una classe ma benì al file stesso e metodi che potrebbero esserci utili

@staticmethod
def somma(a,b):
    return a+b

@staticmethod
def checkEven(n):
    if n % 2 == 0:
        return 0
    else:
        return 1