import random

print(""
     " _\n"
     "| |\n"
     "| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __\n"
     "| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ \n"
     "| | | | (_| | | | | (_| | | | | | | (_| | | | | \n"
     "|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n"
     "                   __/  |\n"
     "                  |___/" )


list_words = ["Ingegneria", "Analisi", "Geometria"]



#print(f"{underscore},   {word}")
#input("inserisci una lettera")

# Devo sfruttare una lista temporanea.
# quindi

def main():
    life = 10
    word = list_words[random.randint(0, len(list_words) - 1)]
    temp_list_contain_char_and_underscore = []
    you_lose=False

    for i in range(len(word)):
        temp_list_contain_char_and_underscore.append("_ ")


    while (life > 0) and ("".join(temp_list_contain_char_and_underscore) != word):
        #print(f"Hai {life} vite,\nparola da indovinare --> {underscore}")
        print(f"Hai {life} vite,\nparola da indovinare --> {"".join(temp_list_contain_char_and_underscore)}")
        char = input("Inserisci un carattere! :)\n")
        x = check_char(word,char)
        if x[0] == False:
            print(f"Non è presente questo carattere = {x[1]}")
            life -=1
            if life == 0:
                you_lose = True
                break
        else:
            string =""
            list_index = x[0]
            for n in list_index:
                temp_list_contain_char_and_underscore[n] = char

    if you_lose == True:
        print("You lose!!")
    else:
        print(f"You win!! the word is{word}")


def check_char(word:str, char):
    # la lista conterrà gli indici delle lettere indovinate
    # le lettere che sono state indovinate allora devono comparire a schermo nella posizione indicata
    temp_list =[]
    counter = 0
    for i in range(len(word)):
        if word[i] == char:
            counter +=1
            temp_list.append(i)

    if counter > 0:
        return temp_list, char
    else:
        return False,char

    # Ho ottenuto la lista contente gli indici delle parole a questo punto dovrei far ritornare la lista e il carattere
    # posso dire che nella posizione n accade questo _ _ _ A _ _ A _ _ _ in loop


main()












