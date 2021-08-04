# rock paper scissors game
from rpc_game_art import rock, paper, scissors
import random

elements = [rock, paper, scissors]
random_choice = random.choice(elements)

user_choice = input("[+] Make a choice (1 for rock 2 for paper 3 for scissors) >")

def print_choices():
    print(f"[+] The computer's choice:\n{random_choice}")
    print(f"[+] Your choice: \n{elements[int(user_choice) - 1]}")

def play():
    if user_choice == "1":
        if random_choice == elements[0]:
            print_choices()
            print("[+] No one wins.")
        elif random_choice == elements[1]:
            print_choices()
            print("[-] You lose the game:(")
        else:
            print_choices()
            print("[+] You won :D")

    elif user_choice == "2":
        if random_choice == elements[0]:
            print_choices()
            print("[+] You won :D")
        elif random_choice == elements[1]:
            print_choices()
            print("[+] No one wins.")
        else:
            print_choices()
            print("[-] You lose the game:(")

    elif user_choice == "3":
        if random_choice == elements[0]:
            print_choices()
            print("[-] You lose the game:(")
        elif random_choice == elements[1]:
            print_choices()
            print("[+] You won :D")
        else:
            print_choices()
            print("[+] No one wins.")

if user_choice != "1" or user_choice != "2" or user_choice != "3" :
    while user_choice != "1" or user_choice != "2" or user_choice != "3":
        print("[-] Please choose one option to play.")
        user_choice = input("[+] Make a choice (1 for rock 2 for paper 3 for scissors) >")
        if user_choice == "1" or user_choice == "2" or user_choice == "3":
            play()
            break

