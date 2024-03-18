komunikaty_dla_milusia = ['wstawaj', 'jemy', 'idziemy się myc']
zakończone = []

def wyświetlanie(komunikaty_dla_milusia, zakończone):
    """wyswitla komunikatycz listy komunikatow i zapisuje je na liscie wyswietlonych komunikatów"""
    while komunikaty_dla_milusia:
        polecenie = komunikaty_dla_milusia.pop()
        print(polecenie)
        zakończone.append(polecenie)

wyświetlanie(komunikaty_dla_milusia, zakończone)
print(f'Wszystkie wyświetlone komunikaty {zakończone}')