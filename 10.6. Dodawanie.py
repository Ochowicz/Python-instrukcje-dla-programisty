print('Jest to prosty program, który po podaniu przez Ciebie 2 liczb doda je do siebie')
try:
    liczba_1 = int(input('Podaj pierwszą liczbę do dodania:\n'))
except ValueError:
    print('Niestety liczba została napisana w niewłaściwym formacie')
try:
    liczba_2 = int(input('Podaj drugą liczbę do dodania:\n'))
except ValueError:
    print('Niestety liczba została napisana w niewłaściwym formacie')
print(liczba_1 + liczba_2)