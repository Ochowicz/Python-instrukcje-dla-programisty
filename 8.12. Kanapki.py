def kanapka(*składniki):
    print(f'Przygotujemy Ci kanapkę z:')
    for składnik in składniki:
        print(f'- {składnik}')

kanapka('ser', 'szynka', 'pomidor')