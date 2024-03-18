def make_car(brand, model, **car_info):
    """Tworzy słownik zawierający informacje o samochodzie"""
    car_info['brand'] = brand
    car_info['model'] = model
    return car_info
my_father_car = make_car('daewo', 'lanos', color='cherry', owner='my father')
print(my_father_car)