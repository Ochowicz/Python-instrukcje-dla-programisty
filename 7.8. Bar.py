sandwich_orders = ['kanapka z tuńczykiem', 'kanapka z pomidorem', 'kanapka z szynką']
finished_sandwitches = []
while sandwich_orders:
    current_sandwitch = sandwich_orders.pop()
    print("Przygotowujemy dla Ciebie kanapkę")
    finished_sandwitches.append(current_sandwitch)
    print(f'{current_sandwitch} jest gotowa\n')
print('Wszystkie zamówione kanapiki zostały zrobione i wymienione poniżej:')
for sandwitch in finished_sandwitches:
    print(f'- {sandwitch}')