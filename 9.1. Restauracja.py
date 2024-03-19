class Restaurant():
    """Modelowanie restauracji"""
    def __init__(self, restaurant_name, cuisine_type):
        """Inicjalizacja atrybutów restaurant_name i cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """wyswietla nazwe restauracji i rodzaj kuchni"""
        print(f'Restauracja nazywa się {self.restaurant_name.title()}')
        print(f'Restauracja specjalizuje się w {self.cuisine_type.title()}')

    def open_restaurant(self):
        """wyswietla informacje o godzinach pracy restauracji"""
        print(f'Restauracja {self.restaurant_name.title()} otwarta jest w'
        'godzinach od 10.00 do 22.00')

pizzeria_bravo = Restaurant('bravo', 'kuchnia włoska')
print(pizzeria_bravo.restaurant_name)
print(pizzeria_bravo.cuisine_type)
pizzeria_bravo.describe_restaurant()
pizzeria_bravo.open_restaurant()
