from random import randint, choice
pula = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')
wylosowane = []
while len(wylosowane) < 4:
    wylosowane.append(choice(pula))
print(f'Wylosowane liczby lub litery to - {wylosowane.sort()}')
