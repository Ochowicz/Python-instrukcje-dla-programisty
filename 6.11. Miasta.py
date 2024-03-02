cities = {
    'Wrocław': {'country': 'Poland', 'population': 638659, 'fact': 'Kiedyś nazywał się Breslau',},
    'Madryt': {'country': 'Spain', 'population': 3223000, 'fact': 'Znajduje się tu \
najstarsza restauracja świata',},
    'Rzym': {'country': 'Italy', 'population': 2873000, 'fact': 'Częścią tego miasta jest \
państwo Watykan'}
}
print('\nPoniżej przedstawie listę 3 miast i kilka informacji o nich:')
for city, informacje in cities.items():
    print(f'\n- {city}')
    for v, k in informacje.items():
        print(f'* {v}: {k}')