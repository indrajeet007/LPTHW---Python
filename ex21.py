def add(a, b):
    print("Adding {0} & {1}".format(a, b))
    return a + b

def subtract(a, b):
    print("Subtracting {0} & {1}".format(a, b))
    return a - b

def divide(a, b):
    print("Dividing {0} & {1}".format(a, b))
    return a / b

def multiply(a, b):
    print("Multiplying {0} & {1}".format(a, b))
    return a * b

print("Maths with functions:\n")

age = add(30, 5)
height = subtract(70, 3)
weight = multiply(90, 2)
iq = divide(100, 2)

print("\nAge: {0}, Height: {1}, Weight: {2}, IQ: {3}\n".format(age, height, weight, iq))

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("\nThat calculates to: {}. Can you do it by hand ? Hmm..!".format(what))
