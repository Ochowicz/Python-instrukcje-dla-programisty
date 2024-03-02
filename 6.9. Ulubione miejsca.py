# Ulubione miejsca
ulubione_miejsca = {
    'Piotr': ['Wenecja', 'Paryż', 'Mediolan'],
    'Szymon': ['Hamburg', 'Wrocław', 'Berin'],
    'Anita': ['Park Staromiejski', 'Starówka', 'Hala Stulecia']
}

for imię, miejsca in ulubione_miejsca.items():
    print(f'\n{imię} w śród swoich ulubionych miejsc ma:')
    for miejsce in miejsca:
        print(f'- {miejsce}')