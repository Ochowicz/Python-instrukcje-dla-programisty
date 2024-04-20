from pathlib import Path
import json
path = Path('ulubiona_liczba.txt')
content = path.read_text()
liczba = json.loads(content)
print(f'Znam Twoją ulubioną liczbę! Twoją ulubioną liczbą jest {liczba}')