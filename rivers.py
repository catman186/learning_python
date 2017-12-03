rivers = {
    'nile': 'egypt',
    'yangzte': 'china',
    'mississippi': 'america',
    'amazon': 'brazil',
    'mekong': 'china',
    'huang he': 'china',
    'ishim': 'kazakhstan',
    'ural': 'russia',
    }

# sentence with items
print("The longest rivers in the world: ")
for river, country in rivers.items():
    print(" The " + river.title() + " river, located in " + country.title() + ".")

# print all the rivers
print("\nThe rivers names are: ")
for river in rivers.keys():
    print(" "  + river.title() + " river.")

# print all the countries
print("\nThe countries are: ")
for country in rivers.values():
    print(" " + country.title() + ".")
