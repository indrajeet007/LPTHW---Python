from sys import exit

def gold_room():
    print("This room is full of gold. How much do you fancy taking with you?")

    next = input("> ")

    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print("This gentleman ain't greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")

    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey":
            dead("The bear looks at you and slaps your face off!")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now!")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed of and kills you instantly. RIP!")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I have no idea what to do!")

def vampire_room():
    print("Here you see the mighty, Vladimir the \'Great Vampire\'!")
    print("He is a 500 year old vampire.")
    print("He offers you a drink saying it will give you anythin\' you want!")
    print("Do you drink the drink or decide to flee?")

    next = input("> ")

    if "flee" in next:
        start()
    elif "drink" in next:
        dead("Well that was tasty and made me drowsy! Next thing i remember is being hung upside down in a cave. Yikesss!!!")
    else:
        vampire_room()

def dead(why):
    print("{}, Good Job !".format(why))
    exit(0)

def start():
    print("You are in a dark room!")
    print("There is a door at the right and the left. Choose wisely!")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        vampire_room()
    else:
        dead("You stumbled to find the doors, you died in vain. RIP!")

start()
