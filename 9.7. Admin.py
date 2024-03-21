class User():
    """Modelowanie użytkownika"""
    def __init__(self, first_name, last_name, age, job):
        """Inicjalizacja atrybutów first_name i last_name"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job

    def describe_user(self):
        """Wyświetla informacje zebrane o użytkowniku"""
        print(f'{self.first_name.title()} {self.last_name.title()} '
              f'ma {self.age} lat i pracuje jako {self.job.title()}')

    def greet_user(self):
        """Wita użytkownika"""
        print(f'Witaj {self.first_name.title()}!')

class Admin(User):
    """Modelowanie administratora"""
    def __init__(self, first_name, last_name, age, job):
        """Inicja atrybutów klasy nadrzędnej, następnie
        inicjacja atrybutów administratora"""
        super().__init__(first_name, last_name, age, job)
        self.privileges = ['może dodać post',
                           'może usunąć post',
                           'może zbanować użytkownika']

    def show_privileges(self):
        print('Uprawnienia administratora:')
        for i in self.privileges:
            print(f'- {i}')

białek = Admin('michal', 'białek', 40, 'administrator')
białek.describe_user()
białek.show_privileges()

