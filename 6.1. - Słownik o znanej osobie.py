# Słownik o Wiki
Wiki = {'imię': 'Michalina',
        'nazwisko': 'Adamska',
        'imię pupila': 'Popi',
        'wiek': 30,
        'miejsce zamieszkania': 'Wrocław',
        }

Krzyś = {'imię': 'Krzysztof',
         'nazwisko': 'Ochowicz',
         'imię dziecka': 'Milan',
         'marzenie': 'móc pracować z domu',
         'wiek': 32,
         }

for v, k in Wiki.items():
    print(f"{v}: {k}")

print('\n')

for v, k in Krzyś.items():
    print(f"{v}: {k}")