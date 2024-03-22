from random import randint, choice

def losowanie(n=4):
    """Modeluje wylosowanie n liczb z dostępnej puli"""
    pula = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')
    wylosowane = []
    while len(wylosowane) < n:
        wylosowane.append(choice(pula))
    return wylosowane
    print(wylosowane)

mój_kupon = losowanie()
wygrany = []

def anazlia(kupon, wygrany):
    """analiza wygrywalnośći w losowaniu"""
    n = 0
    while kupon != wygrany:
        n += 1
        wygrany = losowanie()
        if kupon == wygrany:
            print(f'Wybrane przez Ciebie liczby zostały wylosowane w {n} losowaniu')

anazlia(mój_kupon, wygrany)