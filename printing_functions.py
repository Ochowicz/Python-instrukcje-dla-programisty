def print_models(unprinted_designs, completed_models):
    """
    Symulujemy wydruk poszczególnych projektów, dopóki pozostał jakikolwiek
    projekt na liście. Każdy wydrukowany model zostaje przeniesiony na
    listę completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Wydruk modelu: {current_design}")
        completed_models.append(current_design)