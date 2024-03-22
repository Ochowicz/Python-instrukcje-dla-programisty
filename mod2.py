from mod1 import User
class Privileges():
    """Modelujemy uprawnienia jako osobną klasę"""
    def __init__(self):
        """Inicjacja atrybutu privileges"""
        self.privileges = ['może dodać post',
                           'może usunąć post',
                           'może zbanować użytkownika']

    def show_privileges(self):
        print('Uprawnienia administratora:')
        for i in self.privileges:
            print(f'- {i}')

class Admin(User):
    """Modelowanie administratora"""
    def __init__(self, first_name, last_name, age, job):
        """Inicja atrybutów klasy nadrzędnej, następnie
        inicjacja atrybutów administratora"""
        super().__init__(first_name, last_name, age, job)
        self.privileges = Privileges()
