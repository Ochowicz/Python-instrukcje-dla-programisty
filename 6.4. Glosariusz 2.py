# Słownik pojęć związanych z programowaniem i pythonem
Glosariusz = {
    'ciąg tekstowy': 'Seria znaków zamkniętych znakami cytowania',
    'lista': 'zbiór elementów ułożonych w określonej kolejności którą możemy edytować, \
zamknięty nawiasami kwadratowymi i rozdzielony przecinkami',
    'pętla for': 'pozwala wykonać konkretną serię zadań na wszystkich elementach',
    'krotka': 'lista, której nie można edytować, zamknięta nawiasami okrągłymi',
    'konstrukcja if': 'konstrukcja warunkowa, która pozwala na wykonanie konkretnych \
    działań, jeśli zostaną spełnione zapisane w niej warunki'
}

for key in Glosariusz:
    print(f'''{key}:
    {Glosariusz[key]}\n''')
