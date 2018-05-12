## Animal is-a object
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## what is this below ?
        ## super here refers to the above immediate object 'Person'
        ## ensures running the __init__ method of a parent class reliably
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("satan")

## mary is-a Person
mary = Person("mary")

## mary has a attribute 'pet' which is now assigned to 'satan'
mary.pet = satan

## frank is-a Employee with 'Frank' and '120000' as parameters
frank = Employee("Frank", 120000)

## frank has a attribute 'pet' which is assigned to 'rover'
frank.pet = rover

## set 'flipper' to an instance of 'Fish'
flipper = Fish()

## set 'crouse' to an instance of 'Salmon'
crouse = Salmon()

## set 'harry' to an instance of 'Halibut'
harry = Halibut()
