from pathlib import Path
import json
path = Path('ulubiona_liczba.txt')
if path.exists():
    content = path.read_text()
    liczba = json.loads(content)
    print(f'Znam Twoją ulubioną liczbę! Twoją ulubioną liczbą jest {liczba}')
else:
    liczba = input('Podaj swoją ulubioną liczbę:\n')
    content = json.dumps(liczba)
    path.write_text(content)
    print('Twoja ulubiona liczba została zapisana w pliku "ulubiona_liczba.txt"')