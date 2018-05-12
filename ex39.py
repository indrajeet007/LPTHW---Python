# create a mapping of state to abbreviation
states = {
    'Maharashtra': 'MH',
    'TamilNadu': 'TN',
    'Karnataka': 'KA'
}

# create a basic set of states and some cities in them
cities = {
    'MH': 'Pune',
    'TN': 'Chennai',
    'KA': 'Hampi'
}

# add some more cities
cities['KA'] = 'Bangalore'
cities['MH'] = 'Mumbai'

# print out some cities
print('-' * 10)
print("KA State has: ", cities['KA'])
print("MH State has: ", cities['MH'])

# print some more states
print('-' * 10)
print("Maharashtra's abbreviation is: ", states['Maharashtra'])
print("Karnataka's abbreviation is: ", states['Karnataka'])

# do it by using the state then cities dict
print('-' * 10)
print("Maharashtra has: ", cities[states['Maharashtra']])
print("TamilNadu has: ", cities[states['TamilNadu']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
    print("%s is abbreviated as %s" % (state, abbrev))

# print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

# now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))

print('-' * 10)
# safely get an abbreviation by state that might not be there
state = states.get('Nagpur', None)

if not state:
        print("Sorry, no Nagpur!")

# get a city with a default value
city = cities.get('MH', 'Does Not Exist!')
print("The city for the state 'MH' is: %s" % city)
