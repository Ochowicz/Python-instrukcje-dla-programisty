class Restaurant():
    """Modelowanie restauracji"""
    def __init__(self, restaurant_name, cuisine_type):
        """Inicjalizacja atrybutów restaurant_name i cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """wyswietla nazwe restauracji i rodzaj kuchni"""
        print(f'Restauracja nazywa się {self.restaurant_name.title()}')
        print(f'Restauracja specjalizuje się w {self.cuisine_type.title()}')

    def open_restaurant(self):
        """wyswietla informacje o godzinach pracy restauracji"""
        print(f'Restauracja {self.restaurant_name.title()} otwarta jest w'
        'godzinach od 10.00 do 22.00')

    def set_number_server(self, numeber_served):
        """ustawia wartość liczby klientów"""
        self.number_served = numeber_served

    def incremnt_number_served(self, number_served):
        """zwiększa dodatychczasową wartość liczby clientów o zadaną wartość"""
        self.number_served += number_served

restaurant = Restaurant('restaurant', 'restauracyjna')
print(f'Liczba klientów restauracji to {restaurant.number_served}')
restaurant.number_served = 5
print(f'Liczba klientów restauracji to {restaurant.number_served}')

restaurant.set_number_server(8)
print(f'Liczba klientów restauracji to {restaurant.number_served}')
restaurant.set_number_server(9)
print(f'Liczba klientów restauracji to {restaurant.number_served}')

restaurant.incremnt_number_served(1)
print(f'Liczba klientów restauracji to {restaurant.number_served}')
restaurant.incremnt_number_served(10)
print(f'Liczba klientów restauracji to {restaurant.number_served}')