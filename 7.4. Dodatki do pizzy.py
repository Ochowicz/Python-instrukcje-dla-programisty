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
