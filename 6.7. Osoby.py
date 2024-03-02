# Słownik o Wiki
Wiki = {'imię': 'Michalina',
        'nazwisko': 'Adamska',
        'imię pupila': 'Popi',
        'wiek': 30,
        'miejsce zamieszkania': 'Wrocław',
        }

Krzyś = {'imię': 'Krzysztof',
         'nazwisko': 'Ochowicz',
         'imię pupila': 'Popi',
         'wiek': 32,
         'miejsce zamieszkania': 'Wrocław',
         }

Milan = {'imię': 'Milan',
         'nazwisko': 'Ochowicz',
         'imię pupila': 'Popi',
         'wiek': 2,
         'miejsce zamieszkania': 'Wrocław',
         }

people = [Wiki, Krzyś, Milan]

for imię in people:
    for v, k in imię.items():
        print(f'{v}: {k}')
    print('\n')
