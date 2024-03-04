sandwich_orders = ['kanapka z pastrami', 'kanapka z tuńczykiem', \
                   'kanapka z pastrami', 'kanapka z pomidorem', 'kanapka z szynką']
finished_sandwitches = []
print('W BARZE SKOŃCZYŁO SIĘ PASTRAMI')
while 'kanapka z pastrami' in sandwich_orders:
    sandwich_orders.remove('kanapka z pastrami')
print(f'Kanapki jakie możemy przygotować:\n {sandwich_orders}')
while sandwich_orders:
    current_sandwitch = sandwich_orders.pop()
    print("Przygotowujemy dla Ciebie kanapkę")
    finished_sandwitches.append(current_sandwitch)
    print(f'{current_sandwitch} jest gotowa\n')
print('Wszystkie zamówione kanapiki zostały zrobione i wymienione poniżej:')
for sandwitch in finished_sandwitches:
    print(f'- {sandwitch}')