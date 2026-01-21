import random 

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    user_input = input("type rock / paper / scissors or Q to quit : ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        print("invalid choice . try again. ")
        continue

    computer_pick = random.choice(options)
    print("computer picked",computer_pick )
    
    if user_input == computer_pick:
        print("it is a tie. ")

    elif(user_input == "rock" and computer_pick =="scissors") or \
        (user_input == "paper" and computer_pick =="rock") or \
        (user_input == "scissors" and computer_pick =="paper"):
        print("you won!")
        user_wins += 1

    else:
        print("you lost!")
        computer_wins += 1

print("\n you won", user_wins , "times.")
print("the computer won ", computer_wins , "times.")
print(" good job !")

           