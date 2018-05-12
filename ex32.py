the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'pears', 'oranges', 'custard-apples', 'mangoes']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this for-loop goes through the list
for number in the_count:
    print("This is the count: %d" % number)
    # print("This is the count: {}".format(number))
print("\n")

# same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit)
    # print("A fruit of type: {}".format(fruits))
print("\n")

# also we can do through a mixed list
# here we have to use %r as we don't know the type of content in the list
for i in change:
    print("I got: %r" % i)
    # print("I got: {}".format(i))
print("\n")

# we can also build a list, first create an empty list and then populate entries using the append function
elements = []

for i in range(0, 10):
    print("Adding %d to the list" % i)
    # print("Adding {} to the list".format(i))
    # now append the elements into the list 'elements'
    elements.append(i)
print("\n")

# now we can print them out
for i in elements:
    print("Element was: %d" % i)
    # print("Element was: {}".format(i))
