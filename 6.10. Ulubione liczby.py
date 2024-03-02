#Ulubione liczby
Ulubione_liczby = {'wiki': [1,2,3], 'krzysia': [2,3,4], 'popa': [3,4,5], 'milana': [4,5,6],}
for imię, liczby in Ulubione_liczby.items():
    print(f'\nUlubionymi liczbmi {imię.title()} są:')
    for liczba in liczby:
        print(f'- {liczba}')
