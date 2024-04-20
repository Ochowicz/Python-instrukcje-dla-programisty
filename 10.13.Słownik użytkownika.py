from pathlib import Path
import json

def greet_user():
    """Przywitanie użytkownika z użyciem jego imienia."""
    path = Path('name_forename_age.json')
    if path.exists():
        content = path.read_text()
        dictionary = json.loads(content)
        print(f'Witaj ponownie, {dictionary['name'].title()} {dictionary['forname'].title()}. Masz {dictionary['age']} więc ucz się skoro masz czas!')
    else:
        name = input('Please write Your name:\n')
        forname = input('Please write Your forname:\n')
        age = input('Please Write Your age:\n')
        dictionary = {'name': name, 'forname': forname, 'age': age}
        content = json.dumps(dictionary)
        path.write_text(content)
        print(f'Twoje imię, nazwisko oraz wiek zostały zapisane i będą używane później, {dictionary['name']}')
greet_user()