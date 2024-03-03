# trzy wyjscia
    # 7.4. dodatki do pizzy
        # użycie tekstu warunkowego
pizza = []
składnik = ''
while składnik != 'koniec':
    składnik = input('Proszę o podanie składnika pizzy.\n\
Gdy zakończysz dodawanie składników napisz słowo "koniec"\n')
    if składnik == "koniec":
        print(f'Twoja pizza będzie przygotowana z następujących składników {pizza} Smacznego!')
    else:
        pizza.append(składnik)
        print(f'{składnik} został dodany do pizzy')

        # zmienna active - flaga
pizza = []
active = True
while active:
    składnik = input('Proszę o podanie składnika pizzy.\n\
Gdy zakończysz dodawanie składników napisz słowo "koniec"\n')
    if składnik == "koniec":
        active = False
        print(f'Twoja pizza będzie przygotowana z następujących składników {pizza} Smacznego!')
    else:
        pizza.append(składnik)
        print(f'{składnik} został dodany do pizzy')

        # brake
pizza = []
while True:
    składnik = input('Proszę o podanie składnika pizzy.\n\
Gdy zakończysz dodawanie składników napisz słowo "koniec"\n')
    if składnik == "koniec":
        print(f'Twoja pizza będzie przygotowana z następujących składników {pizza} Smacznego!')
        break
    else:
        pizza.append(składnik)
        print(f'{składnik} został dodany do pizzy')

    # 7.5. Bilety do kina
        # użycie tekstu warunkowego
wiek = int(input('Proszę o podanie wieku:\n'))
if wiek < 3:
    print('Bilet jest bezpłatny')
elif wiek > 12:
    print('Bilet kosztuje 15zł')
else:
    print('Bilet kosztuje 10zł')

        # zmienna active - flaga
wiek = int(input('Proszę o podanie wieku:\n'))
active = True
while active:
    if wiek < 3:
        print('Bilet jest bezpłatny')
        active = False
    elif wiek > 12:
        print('Bilet kosztuje 15zł')
        active = False
    else:
        print('Bilet kosztuje 10zł')
        active = False

        # brake
wiek = int(input('Proszę o podanie wieku:\n'))
while True:
    if wiek < 3:
        print('Bilet jest bezpłatny')
        break
    elif wiek > 12:
        print('Bilet kosztuje 15zł')
        break
    else:
        print('Bilet kosztuje 10zł')
        break
