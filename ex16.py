# Reading and writing files

from sys import argv

script, filename = argv

print("We're going to erase content's of this file %r, type yes/no to continue!" % filename)
choice = input("> ")

if(choice == 'yes' or choice == 'YES'):
    print("\nOpening file %r" % filename)
    target = open(filename, 'w')

    print("\nTruncating the file, Goodbye past!")
    target.truncate()

    print("\nNow enter three lines to truncate in the file: ")

    line1 = input("Line 1: ")
    line2 = input("Line 2: ")
    line3 = input("Line 3: ")

    print("\nI'm going to write these to the file")

    # target.write(line1)
    # target.write("\n")
    # target.write(line2)
    # target.write("\n")
    # target.write(line3)
    # target.write("\n")

    target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

    print("\nFinally, we close the file for good!\n")
    target.close()
elif(choice == 'no' or choice == 'NO'):
    print("Please make a valid choice dumbass!")
else:
    print("Enter yes/no, easy!")
