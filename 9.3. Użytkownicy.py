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

jorge = User('jorge', 'michael', 80, 'piosenkarz')
thomas = User('thomas', 'jonhson', 40, 'policjant')

jorge.describe_user()
jorge.greet_user()
thomas.describe_user()
thomas.greet_user()