country = {
    'Poland': 'PL',
    'Germany': 'DE',
    'Sweden': 'SE',
    'Czech Republic': 'CZ',
    'Slovakia': 'SK'
}

cities = {
    'SK': 'Bratislava',
    'PL': 'Warsaw',
    'DE': 'Berlin'
}

cities['CZ'] = 'Prague'
cities['SE'] = 'Stockholm'

print('-' * 10)
print("PL has: ", cities['PL'])
print("SK has: ", cities['SK'])

print('-' * 10)
print("Sweeden ISO is: ", country['Sweden'])
print("Czech Republic ISO is: ", country['Czech Republic'])

print('-' * 10)
print("Germany has: ", cities[country['Germany']])
print("Slovakia has: ", cities[country['Slovakia']])

print('-' * 10)
for country, abbrev in list(country.items()):
    print(f"{country} is abbreviated {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('-' * 10)
for country, abbrev in list(country.items()):
    print(f"{country} country is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
country = country.get('France')

if not country:
    print("Sorry, no France")

city = cities.get('FR', 'Does not exist')
print(f"The city for the country 'FR' is {city}")
