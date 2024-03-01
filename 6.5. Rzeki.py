# Rzeki i kraje przez które one przepływają
rzeki = {'nil': 'egipt', 'amazonka': 'kolumbia', 'jangcy': 'chiny'}
for rzeka in rzeki:
    print(f'{rzeka.title()} przepływa przez {rzeki[rzeka].title()}.')
print('\nNazwy najdłuższych rzek na świecie:')
for rzeka in rzeki:
    print(rzeka.title())
print('\nNazwy państw przez które przepływają te rzeki:')
for rzeka in rzeki:
    print(rzeki[rzeka].title())