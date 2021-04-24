# Snake Water Gun Game
# Snake win over Water : Water win over gun : Gun win over Snake
# Players : Kaptan and Computer
import random
kaptan_point =0
computer_point =0
elem = ["water", "snake", "gun"]

for i in range(1,11):
    kaptan_choice = input("Enter your choice, among 'water' , 'snake' and 'gun' : ")
    computer_choice = random.choice(elem)
    if kaptan_choice == "snake" and computer_choice == "water" :
        print(f"Kaptan Won this round as computer choice is {computer_choice}")
        kaptan_point = kaptan_point + 1
        # print(f"Kaptan's point = {kaptan_point} and computer's point = {computer_point} ")
    elif kaptan_choice == "water" and computer_choice == "snake":
        print(f"Computer Won this round as computer choice is {computer_choice}")
        computer_point = computer_point +1
    elif kaptan_choice == "water" and computer_choice == "gun" :
        print(f"Kaptan Won this round as computer choice is {computer_choice}")
        kaptan_point = kaptan_point + 1
    elif kaptan_choice == "gun" and computer_choice == "water":
        print(f"Computer Won this round as computer choice is {computer_choice}")
        computer_point = computer_point +1
    elif kaptan_choice == "gun" and computer_choice == "snake" :
        print(f"Kaptan Won this round as computer choice is {computer_choice}")
        kaptan_point = kaptan_point + 1
    elif kaptan_choice == "snake" and computer_choice == "gun":
        print(f"Computer Won this round as computer choice is {computer_choice}")
        computer_point = computer_point +1
    elif kaptan_choice == computer_choice :
        print("Both Enter same choice, so it is a draw")
    else:
        print("Some Wrong input by kaptan !! Try again")
        print("As Kaptan break the rule of game, 1 point will be withdrown from his score points")
        kaptan_point = kaptan_point -1
    print(f"Kaptan's point = {kaptan_point} and computer's point = {computer_point} ")
    print(f"Game played {i} out of 10\n")

if kaptan_point > computer_point :
    print(f"Kaptan win the game, with points {kaptan_point} and the points of computer are {computer_point} ")
elif kaptan_point < computer_point :
    print(f"Computer win the game, with points {computer_point} and the points of Kaptan are {kaptan_point} ")
else :
    print(f"Game Draw with points {kaptan_point} of each")




