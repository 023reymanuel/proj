import random

userwins = 0
computerwins = 0
options = ["rock", "scissors", "paper"]


while True:
    useer_input  = input("Type rock/paper/scissors or press Q to quit:").lower()
    if useer_input == "q":
        break
    
    if useer_input not in options:
        continue
    random_no = random.randint(0, 2)
    # rock is 0, paper is 2, scissors is 1  
    computer_pick = options[random_no]
    print("computer picked", computer_pick +"." )
    if useer_input == "rock" and computer_pick == "scissors":
        print("You won!")
        userwins += 1
        continue

    elif useer_input == "paper" and computer_pick == "rock":
        print("You won!")
        userwins += 1
        continue

    elif useer_input == "scissors" and computer_pick == "paper":
        print("You won!")
        userwins += 1
        continue

    else:
        print("you lost!")
        computerwins += 1

print("You won",userwins, "times" )
print("The computer wins",computerwins, "times" )
print("Goodbye")
    