def city_country(city, country):
    "Sformatowana nazwa miasta i państwa w którym ono leży"
    sformatowane = f'{city.title()}, {country.title()}'
    return sformatowane

Wrocław = city_country('Wrocław', 'Polska')
Londyn = city_country('Londyn', 'Anglia')
Berlin = city_country('Berlin', 'Niemcy')

print(Wrocław)
print(Londyn)
print(Berlin)


