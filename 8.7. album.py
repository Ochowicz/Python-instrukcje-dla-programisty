def make_album(wykonawca, album):
    """Funkcja tworzy słownik z wykonawcą i nazwą albumu"""
    słownik = {'wykonawca': wykonawca.title(), 'album': album.title()}
    return słownik

hybryda = make_album('Linkin Park', 'hybryd theory')
print(hybryda)
meteora = make_album('Linkin Park', 'metoera')
print(meteora)
minutes_to_midnight = make_album('Linkin Park', 'minutes to midnight')
print(minutes_to_midnight)