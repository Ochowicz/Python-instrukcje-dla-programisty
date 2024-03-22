from random import randint

class Die():
    """Modelowanie kości do gry"""
    def __init__(self, sides=6):
        """Inicjalizacja atrybutu liczba ścian kości"""
        self.sides = sides

    def roll_die(self):
        """symulacja jednego rzutu kością"""
        print(f'Wyrzucono {randint(1, self.sides)}')

    def roll_die_10(self):
        """symulacja 10 rzutów kością"""
        for i in range(10):
            print(f'Wyrzucono {randint(1, self.sides)}')
        print('\n')

kość_6_ścianek = Die()
kość_6_ścianek.roll_die_10()

kość_10_ścianek = Die(10)
kość_10_ścianek.roll_die_10()

kość_20_ścianek = Die(20)
kość_20_ścianek.roll_die_10()

