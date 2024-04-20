from pathlib import Path
import json

path = Path('ulubiona_liczba.txt')
liczba = input('Podaj swoją ulubioną liczbę:\n')
content = json.dumps(liczba)
path.write_text(content)
print('Twoja ulubiona liczba została zapisana w pliku "ulubiona_liczba.txt"')