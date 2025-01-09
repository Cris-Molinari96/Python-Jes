import random

 # L'opzione 1 è quella più randomica, permette di generare una password sulla base di tre domande:
 # Inserisci la lunghezza della password che vuoi ottenere
 # Inserisci il numero di simboli che vuoi ottenere
 # Inserisci il numero di numeri che vuoi ottenere

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*']
ALL_LIST = [LETTERS, NUMBERS, SYMBOLS]

# Option1
def main():
    LEN_PASSWORD = int(input("Insert you length fianl password\n"))
    NUMBER_SYMBOL = int(input("How many symbol do you want?\n"))
    NUMBER_NUMBER = int(input("How many number do you want?\n"))

    password_list = []
    counter_symbols = 0
    counter_number = 0

    while len(password_list) < LEN_PASSWORD:
        # Per ogni volta che viene generato un numero randomico
        n_random = random.randint(0,2)

        if n_random == 2:
            if counter_symbols < NUMBER_SYMBOL:
                x_list = ALL_LIST[n_random]
                char = x_list[random.randint(0,len(x_list)-1)]
                password_list.append(char)
                counter_symbols +=1
            else:
                x_list = ALL_LIST[random.randint(0,1)]
                char = x_list[random.randint(0,len(x_list)-1)]
                password_list.append(char)
        else:
            x_list = ALL_LIST[n_random]
            char = x_list[random.randint(0,len(x_list)-1)]
            password_list.append(char)

    for i in range(len(password_list)):
        if password_list[i].isdigit():
            counter_number +=1

# A questo punto abbiamo la lista che contiene la password, appare in questo modo ['2','!','a' .... ]
    # Ora vogliamo controllare quanti numeri e quanti simboli ci sono
    n=0
    while counter_symbols < NUMBER_SYMBOL:
        if password_list[n].isalpha():
            password_list[n] = ALL_LIST[2][random.randint(0, len(SYMBOLS)-1)]
            counter_symbols +=1
            n+=1
        else:
            n+=1
    n=0
    while counter_number < NUMBER_NUMBER:
       if password_list[n].isalpha():
            password_list[n] = LETTERS[random.randint(0,len(LETTERS)-1)]
            counter_number +=1
            n+=1
       else:
           n+=1
    n=0
    while counter_number > NUMBER_NUMBER:
        if password_list[n].isdigit():
            password_list[n] = LETTERS[random.randint(0,len(LETTERS)-1)]
            counter_number -=1
            n +=1
        else:
            n+=1
# non devo cambiare tutti gli elementi della lista ma solo quelli necessari affichè ci sono il numero di simboli richiesti


    password = ""
    for c in password_list:
        password += c

    return password

print(main())

# Option 2
def main2():
    temp_list = []
    # Potremmo applicare dei controlli se il numero passato è un numero o un carattere o stringa
    LEN_PASSWORD = int(input("Insert your length password in number please!\n"))
    string = input("Insert dei char, symbol random digit on keyboard n char\n")
    password = ""

    for c in string:
        temp_list.append(c)

    while len(password) < LEN_PASSWORD:
        char = str(temp_list[random.randint(0,len(temp_list)-1)])
        password += char

    return password

#print(main2())

# Option 3
# Per poter creare un generatore ranodmico di password su caratteri e simbolo indicati dobbiamo seguire una serie di passi:
# L'obiettivo è ottenere la lunghezza della password desiderata e ottenere caratteri o simboli che si vogliono nella password.
# legth password e i simboli ora qui dobbiamo prevedere che i simboli che si vogliano inserire nella pass, non superino la lunghezza finale della password
def main3():
    char_list = []
    start = True
    LEN_PASSWORD = ""
    n = ""
# Quindi chidere la lunghezza della password che si vuole
    LEN_PASSWORD = int(input("Say me you length passowrd in number!\n"))
    print(type(LEN_PASSWORD), LEN_PASSWORD)

    len_char_list = len(char_list)
    while start != False:
        char = input("Insert a charcater or symbol for generate a password\n")
        if char == "end":
            break
        char_list.append(char)
        # Fare un controllo se la lista supera la lunghezza della password che si vuole
#        if len_char_list < len_passowrd:
#            if len(char) == 1:
#                char_list.append(char)
#            else:
#                while len(char) > 1:
#                    char = input("You can insert only one charcater or symbol for generate your password\n")
#                    char_list.append(char)
#        else:
#            print("You can't insert another char,symbol!")
#            start = true
    print(f"Generazione della password {char_list}")
    password_generator3(char_list,LEN_PASSWORD)

def password_generator3(char_list: list,LEN_PASSWORD:int):
    temp_list = []
    password = ""
    while len(password) < LEN_PASSWORD:
        char = char_list[random.randint(0,len(char_list)-1)]
        password += char
        print(password)
#main3()

