from pathlib import Path
path = Path('guest_book.txt')
content = ''
while True:
    user = input('Please input Your name. When evryone inputs their names type "q" to quit\n')
    print(f'Hello {user}! Nice to meet You!')
    if user == 'q':
        break
    content += f'{user}\n'
path.write_text(content)
