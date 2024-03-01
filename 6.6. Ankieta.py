# Ankieta o językach programowania
favorite_languages = {
    'janek': 'pyhon',
    'sara': 'c',
    'edward': 'rust',
    'paweł': 'python',
}
participians = ['krzyś', 'janek', 'sara', 'milan', 'edward', 'paweł']
for person in participians:
    if person in favorite_languages.keys():
        print(f'Thank You {person.title()} for taking part in this query.')
    else:
        print(f'{person.title()} please fulfill the query.')
