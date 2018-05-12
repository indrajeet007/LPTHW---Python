numbers = []

element = int(input("Range level: "))
increment_point = int(input("Incremental level: "))

def number_append(element):
    i = 0
    while i < element:
        print("At the top is %d" % i)
        # print("At the top is {}".format(i))
        numbers.append(i)

        i += increment_point

        print("Numbers now: ", numbers)
        print("\nAt the bottom is %d" % i)
        # print("At the bottom is {}".format(i))

def show_numbers():
    print("\nThe numbers: ")

    for num in numbers:
        print(num)

number_append(element)
show_numbers()
