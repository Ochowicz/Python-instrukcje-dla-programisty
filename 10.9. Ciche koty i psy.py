from pathlib import Path
def odczytywacz(file_name):
    """Odczytywanie zawartości plików tekstowych i wyświetlający ją na ekranie"""
    try:
        path = Path(file_name)
        content = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(content)
odczytywacz('dogs.txt')
odczytywacz('cokolwiekkkk.txt')
odczytywacz('cats.txt')