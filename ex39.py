## Dictionaries

# create a mapping of state to abbreviation
states = {
    'Maharashtra'   :   'MH',
    'Goa'           :   'GA',
    'Karnataka'     :   'KA',
    'Madhya Pradesh':   'MP',
    'Punjab'        :   'PB',
    'Haryana'       :   'HR',
    'Telangana'     :   'TS'
}

# create a basic set of states and some cities in them
cities = {
    'MH'    :   'Mumbai',
    'GA'    :   'Panjim',
    'KA'    :   'Mysore',
    'TS'    :   'Hyderabad',
    'HR'    :   'Rohtak'
}

# add some more cities
cities['PB']    =   'Amritsar'
cities['MP']    =   'Indore'
cities['MH']    =   'Pune'
cities['KA']    =   'Bangalore'

# print out some cities
print("-" * 100)
print("MH State has :", cities['MH'])
print("KA State has :", cities['KA'])

# print some states
print("-" * 100)
print("Maharashtra's abbreviation is:", states["Maharashtra"])
print("Karnataka's abbreviation is:", states["Karnataka"])


# do it by using the state then cities dict
print("-" * 100)
print("Goa has : ", cities[states["Goa"]])
print("Punjab has : ", cities[states["Punjab"]])


# print every state abbreviation
print("-" * 100)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")

# print every city in state
print("-" * 100)
for city, abbrev in list(cities.items()):
    print(f"{abbrev} has the city {city}")


# now do both at the same time
print("-" * 100)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")


print("-" * 100)
# safely get a abbreviation by state that might not be there
state = states.get('Gujrat')

if not state:
    print("Sorry, state not there in States DB.")

print("-" * 100)
# get a city with a default value
city = cities.get("GJ","Does not exist in Cities DB.")
print(f"The city for the state 'GJ' is: {city}")


print("-" * 100)
# print(states, cities)