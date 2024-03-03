wiek = int(input('Proszę o podanie wieku:\n'))
if wiek < 3:
    print('Bilet jest bezpłatny')
elif wiek > 12:
    print('Bilet kosztuje 15zł')
else:
    print('Bilet kosztuje 10zł')
