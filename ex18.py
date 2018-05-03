# scripts with asterisk args
def print_two(*args):
    arg1, arg2 = args
    print("arg1: {0}, arg2: {1}".format(arg1, arg2))

# another way for above so as to ignore *args
def print_two_again(arg1, arg2):
    print("arg1: {0}, arg2: {1}".format(arg1, arg2))

# this takes only one argument
def print_one(arg1):
    print("arg1: {}".format(arg1))

# this one takes no argument
def print_none():
    print("I got nothin' man!")

print_two("Indrajit", "Chavan")
print_two_again("Python", "Rocks..")
print_one("One argument!")
print_none()
