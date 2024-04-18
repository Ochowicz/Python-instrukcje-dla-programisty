print('Jest to prosty program, który po podaniu przez Ciebie 2 liczb doda je do siebie')
while True:
    try:
        liczba_1 = int(input('Podaj pierwszą liczbę do dodania:\n'))
    except ValueError:
        print('Niestety liczba została napisana w niewłaściwym formacie')
    else:
        break
while True:
    try:
        liczba_2 = int(input('Podaj drugą liczbę do dodania:\n'))
    except ValueError:
        print('Niestety liczba została napisana w niewłaściwym formacie')
    else:
        break
print(liczba_1 + liczba_2)