popi = {
    'imie': 'popi',
    'gatunek': 'pies',
    'kolor': 'biały',
    'przysmak': 'ser',
}

białek = {
    'imię': 'białek',
    'gatunek': 'zabawka',
    'kolor': 'biały',
    'przysmak': 'brak, bo to zabawka!',
}

stefan = {
    'imię': 'stefan',
    'gatunek': 'wymyślony słoń',
    'kolor': 'szary',
    'przysmak': 'marzenia o zostaniu programistą',
}

pets = [popi, białek, stefan]

for pet in pets:
    for v, k in pet.items():
        print(f'{v.title()}: {k.title()}')
    print('\n')