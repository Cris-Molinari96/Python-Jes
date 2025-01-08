import random



def start_game():
    num = int(random.randrange(0,3))
    print(num)
    list = ["Paper","Rock","Scissors"]

    start_game = "start"
    while start_game != "end":
        choice = str.lower(input("Insert your choice beetwen: Paper, Rock, Scissors\n"))
        random_choice = list[num]

#Regole del gioco:
        if (choice == "paper") and (random_choice == "Scissor"):
            start_game = print(input(f"Game over... {choice, random_choice} \nIf you stop the game, write stop"))
        elif (choice == "rock") and (random_choice == "Paper"):
            start_game = print(input(f"Game over...{choice, random_choice} \nIf you stop the game, write stop"))
        elif (choice == "rock") and (random_choice == "Scissor"):
            start_game = print(input(f"You win :) {choice, random_choice} \nIf you stop the game, write stop"))
        elif (choice == "paper") and (random_choice == "Rock"):
            start_game = print(input(f"You win :) {choice, random_choice} \nIf you stop the game, write stop"))
        elif (choice == "scissor") and (random_choice == "Rock"):
            start_game = print(input(f"You win :){choice, random_choice}\nIf you stop the game, write stop"))
        elif choice != "paper" and choice != "rock" and choice != "paper":
            print(input(f"The choice is not valid :( {choice}  \nIf you stop the game, write stop"))
        else:
            print(input(f"Parity :( {choice, random_choice}  \nIf you stop the game, write stop"))

start_game()