class User():
    """Modelowanie użytkownika"""
    def __init__(self, first_name, last_name, age, job):
        """Inicjalizacja atrybutów first_name i last_name oraz 2 dodatkowych"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.login_attempts = 0

    def describe_user(self):
        """Wyświetla informacje zebrane o użytkowniku"""
        print(f'{self.first_name.title()} {self.last_name.title()} '
              f'ma {self.age} lat i pracuje jako {self.job.title()}')

    def greet_user(self):
        """Wita użytkownika"""
        print(f'Witaj {self.first_name.title()}!')

    def increment_login_attempts(self):
        """dodaje 1 za każdą próbą logowania"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Zerowanie wartości prób logowania"""
        self.login_attempts = 0

jorge = User('jorge', 'michael', 80, 'piosenkarz')
thomas = User('thomas', 'jonhson', 40, 'policjant')

print(jorge.login_attempts)
jorge.increment_login_attempts()
jorge.increment_login_attempts()
print(jorge.login_attempts)
jorge.reset_login_attempts()
print(jorge.login_attempts)