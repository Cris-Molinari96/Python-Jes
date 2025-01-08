def menu():
    list = []
    print("Welcome in Python Pizza Deliveries! \n "
          "Ours pizza: \n "
          "1: Menu Margherita: 8€, 2: Menu Napoletana 10€, 3: Menu Diavola 12€, 4: Menu Pizza Special 15€, 5: Menu Custom pizza 18€")
    menu_customer = input("Which pizza do you want, write the number? ")

    if int(menu_customer) == 1:
        print(menu_1())
    elif int(menu_customer) == 2:
        print(menu_2())
    elif int(menu_customer) == 3:
        print(menu_3())
    elif int(menu_customer) == 4:
        print(menu_4())
    elif int(menu_customer) == 5:
        list = []
        size = input("S price 5€,\nM price 7€,\nL price 9€ ")
        dough = input("Insert your dough: The choice is wholemeal or organic flour ")
        color = input("White or Red? ")
        exit = "start"
        while exit != "end":
            extra_addition = input("Do you want added more product? \nIf you don't want other product write end please. ")
            if extra_addition == "end":
                print(menu_5(size,dough,color,list))
                exit = extra_addition
                break
            list.append(extra_addition)



def menu_1():
    return "This menu offers pizza Margherita + coca cola and chips"

def menu_2():
    return "This menu offers pizza Napoletana + coca cola and chips"

def menu_3():
    return "This menu offers pizza Diavola + coca cola and chips"

def menu_4():
    return "This menu offers pizza Pizza Special with product... + coca cola and chips"

def menu_5(siz, dough, color, *args):
    price_menu = 18
    number_product = len(args)
    price_menu += number_product

    return f"Custom menu pizza:{siz, dough, color}, additional product: {args} and the price {price_menu}"

#menu()