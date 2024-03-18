def build_profile(first, last, **user_info):
    """Budowa słownika zawierającego wszelkie informacje
    o użytkowniku."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('Krzysztof', 'ochowicz',
                             job='construction mennager',
                             son='milan')
print(user_profile)