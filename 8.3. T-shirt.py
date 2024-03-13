def make_shirt(size, text):
    print(f'\nYour ordered T-shirt in {size} size and with text on it: "{text}"')

size = input('Please type in whith size You want to order t-shirt\n')
text = input('Please type the text whitch You wanna to be print on T-shirt\n')

make_shirt(size, text)
make_shirt(text=input('Please type the text whitch You wanna to be print on T-shirt\n'), \
           size=input('Please type in whith size You want to order t-shirt\n'))