#1. Data una stringa la splittiamo creando una lista contente sottostringhe,
#2. Impostare il while definendo un counter il quale scansiona tutta la sequenza.
#3. Controllo su ogni elemento della sequenza, se contiene un numero/i o se non contiene un numero rispettivamente puliamo la stringa altrimenti
# memorizziamo la stringa in una nuova stringa.
#4. Se l'elemento ovvero la stringa contiene caratteri numerici allora iteriamo sui singoli caratteri.
#5. Impostiamo la condizione che se il carattere non è numerico lo vogliamo inserire in una varabile temporanea scartando il numero
#6. Viene restituita la stringa pulita dai caratteri e mantenedo gli spazi
#@param s: String
def cleanString(s):
    listSplit = s.split()
    c1=0
    sequence =""
    while c1 < len(listSplit):
      if not listSplit[c1].isdigit():
        subString = listSplit[c1]
        lSub = len(listSplit[c1])
        c2 = 0
        newSubString = ""
        while c2 < lSub:
          char = subString[c2]
          if not char.isdigit():
            newSubString = newSubString+char
          c2 +=1

        newSubString = newSubString + " "
        sequence = sequence + newSubString
        c1 +=1
      else:
        newSubString = ""
        newSubString = newSubString + " "
        sequence = sequence + newSubString
        c1 +=1
    return " ".join(sequence.split())

cleanSeq = cleanString("Peppe sei un folleeee2342   renfu2    2r3")
print(cleanSeq)

# Pulire una stringa da caratteri alfabetici
def cleanStringToAlpha(s):
    listSplit = s.split()
    sequence = ""
    c1 =0
    while c1 != len(listSplit):
      subString = listSplit[c1]
      l2 = len(subString)
      c2 = 0
      while c2 < l2:
        if subString[c2].isalpha() != true:
          sequence = sequence + subString[c2]
        c2 +=1
      c1 += 1
    return sequence

# la funzione rimuove dalla stringa passata in ingresso tutti i caratteri numerici
def clearNum(s):
    temp = ""
    for i in s:
      if not i.isdigit():
        temp = temp + i
    return temp

print clearNum(sn)

# La funzione usa un while per rimuovere caratteri
def removeAlpha3WithWhile(s):
    newString = "".join(s.split())
    c1= 0
    c2= 0
    sequence= ""
    l = len(newString)

    while  c1 != l:
      char = newString[c1]
      if char.isdigit():
        sequence = sequence + char

      c1 +=1
    return sequence


# La funzione usa un for per rimuovere caratteri
def removeAlpha2(s):
    mysplit = s.split()
    sequence = ""
    for i in range(0,len(mysplit)):
      for j in mysplit[i]:
        if j.isdigit() == true:
          sequence = sequence + j
    return sequence

# La funzione è una variante base del funzionamento del for e accesso ai caratteri
def removeAlpha(s):
    mysplit = s.split()
    sequence = ""
    for i in range(0,len(mysplit)):
      checkElement(mysplit[i])
      if mysplit[i].isalpha() != true:
        sequence = sequence + mysplit[i]
    return sequence


# Come rimuovere spazi da una stringa?
#Split()!
def removeSpace(s1,s2):
    splitS2 = s2.split()
    print splitS2
    s1.replace(" ","")
    print s1
    stringaSenzaSpazi = ":".join(s2.split())
    print stringaSenzaSpazi


# La funzione data una stringa in ingresso come primo parametro e come secondo un carattere verifica attraverso il counter
# quante volte il carattere è contenuto nella stringa
#@param s: String
#@param ch: Char
#@return counter: Int
def checkChar(s,ch):
    c = 0
    counter = 0
    while c < len(s):
      if ch == s[c]:
        counter +=1
      c +=1
    return counter

# Or
def onlyVowels(s):
    sequence = ""
    for i in range(0,len(s)):
      if((s[i]=="a")or(s[i]=="e")or(s[i]=="i")or(s[i]=="o")or(s[i]=="u")):
        sequence = sequence +s[i]
    return sequence

# And
#@param s = str
#@param newSequence = str
def removeVocal(s):
    newSequence = ""
    for i in range(0,len(s)):
      if((s[i]!="a")and(s[i]!="e")and(s[i]!="i")and(s[i]!="o")and(s[i]!="u")):
        newSequence = newSequence + s[i]


