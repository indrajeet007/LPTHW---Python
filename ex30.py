people = 30
cars = 40
buses = 15

if cars > people:
    print("So many cars, so less people!")
elif cars < people:
    print("There's still time for optimus to arise!")
else:
    print("Can't decide what's with this..")

if buses > cars:
    print("That's a lot of buses..")
elif buses < cars:
    print("We need to use buses regularly..")
else:
    print("Let's walk to work, can we?")

if people > buses:
    print("Alright! Let's march with the buses..")
else:
    print("I prefer no machines today, i'll rather just be at home..")
