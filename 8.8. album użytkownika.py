def make_album(wykonawca, album):
    """Funkcja tworzy słownik z wykonawcą i nazwą albumu"""
    słownik = {'wykonawca': wykonawca.title(), 'album': album.title()}
    return słownik

while True:
    print('Podaj nazwę wykonawcy i jego albumu')
    print('W każdej chwili będziesz mógł zakończyć wpisując "q"')
    wykonawca = input('Wpisz nazwę wykonawcy albumu\n')
    if wykonawca == 'q':
        break
    album = input('Wpisz nazwę albumu\n')
    if album == 'q':
        break
    gotowy_album = make_album(wykonawca, album)
    print(gotowy_album)