print("You enter a dark room with two doors. Do you go through door #1 or #2?")

door = input("Enter your choice: ")

if door == "1":
    print("\nThere's a giant bear eating a delicious cheese cake. What do you do?")
    print("1. Snatch the cake.")
    print("2. Scream at the bear!")

    bear = input("\nEnter your choice: ")

    if bear == "1":
        print("The bear eats your face off! Boo Hoo..")
    elif bear == "2":
        print("The bear screams back at you and hurls the cheese cake in your face. So much for the cake, hush!")
    else:
        print("Well, doing {} is probably better. Bear runs away!".format(bear))

elif door == "2":
    print("\nYou stare into the endless abyss of a black hole approaching towards you! There's very less that you could do, wanna try something?")
    print("1. Try to swim away from event horizon..")
    print("2. Say your prayers and drive into the black abyss!")

    insanity = input("\nEnter your choice: ")

    if insanity == "1" or insanity == "2":
        print("""Little attention into the astrophysics class might have helped you to
        realise that the task you choose is impossible. Well still worth a try! RIP..""")
    else:
        print("You get sucked in and maybe thrown into a puddle of scotch. Who knows! Cheers..")

else:
    print("\nWell, doing {} is probably better. At least it made you snap out of this weird dream !".format(door))
