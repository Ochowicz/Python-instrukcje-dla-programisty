from pathlib import Path
def odczytywacz(file_name):
    """Odczytywanie zawartości plików tekstowych i wyświetlający ją na ekranie"""
    try:
        path = Path(file_name)
        content = path.read_text()
    except FileNotFoundError:
        print('Wybrany plik nie istnieje')
    else:
        print(content)
odczytywacz('dogs.txt')
odczytywacz('cats.txt')