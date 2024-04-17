from pathlib import Path
path = Path('users.txt')
user = input('Proszę o podanie imienia:\n')
path.write_text(user)