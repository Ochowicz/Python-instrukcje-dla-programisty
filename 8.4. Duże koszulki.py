def make_shirt(size='L', text='Uwielbiam Pythona'):
    # Wyświetla rozmiar i tekst koszulki
        print(f'\nYour ordered T-shirt in {size} size and with text on it: "{text}"')

size = input('Please type in whith size You want to order t-shirt\n')
if size == '' or size.lower() == 'l':
    make_shirt()
elif size.lower() == 'm':
    make_shirt(size='M')
else:
    text = input('Please type the text whitch You wanna to be print on T-shirt\n')
    make_shirt(size, text)

