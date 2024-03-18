komunikaty_dla_milusia = ['wstawaj', 'jemy', 'idziemy się myc']
sent_messages = []

def send_messages(komunikaty_dla_milusia, sent_messages):
    """wyswitla komunikatycz listy komunikatow i zapisuje je na liscie
    wyswietlonych komunikatów"""
    while komunikaty_dla_milusia:
        polecenie = komunikaty_dla_milusia.pop()
        print(polecenie)
        sent_messages.append(polecenie)

send_messages(komunikaty_dla_milusia, sent_messages)
print(f'Wszystkie wyświetlone komunikaty {sent_messages}')