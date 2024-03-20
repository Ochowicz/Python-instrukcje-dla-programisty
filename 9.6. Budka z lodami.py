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

class IceCreamStand(Restaurant):
    """Modelowanie budki z lodami"""
    def __init__(self, restaurant_name, cuisine_type):
        """
        Incjalizacja atrybutów klasy nadrzędnej.
        Następnie inicjalizacja atrybutów charakterystycznych
        dla budki z lodami"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['truskawkowe', 'czekoladowe', 'śmietankowe']

    def show_flavours(self):
        for flavour in self.flavours:
            print(f'- {flavour}')

polish_lody = IceCreamStand('polish lody', 'lodziarnia')
print('Lody dostępne są w poniżej wymienionych smakach:')
polish_lody.show_flavours()