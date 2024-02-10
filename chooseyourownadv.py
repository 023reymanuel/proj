name = input("type your name: ")
print("Welcome", name , "to this adventure!")

answ = input("You are on a dirt road. It has come to and end and you can go left or right. Which way would you go?").lower()

if answ == "left":
    answ = input("You came to a river and you can walk around it or swim across? Type to walk to walk around and swim to swim around:")

    if answ == "swim".lower():
        print("You swam across and were eaten by a crocodile.")
    elif answ == "walk".lower():
        print("You walked for many miles and ran out of water. You loose the gamee.")
    else:
        print("Not a valid option you loose")


elif answ == "right": 
    answ = input("You came to a bridge. It looks wobly, do you want to cross it or head back? (CROSS/BACK)?").lower()

    
    if answ == "back".lower():
        print("You go back where you came from")
    elif answ == "cross".lower():
        answ = input("You cross the bridge and meet a stranger  and talk to them?(YES/NO)")

        if answ == "yes".lower():
            print("YOu talk to the stranger and they give you gold. You win")
        
        elif answ == "no".lower():
            print("Ignore the  stranger they are offendedd and they kill you")

        else:
            print("Not a valid option YOu loose!")
    else:
        print("Not a valid option you loose")
else:
    print("Not a valid option. You loose!")