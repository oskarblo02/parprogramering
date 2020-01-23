
def is_valid_PIN():
    pin = input('pin: ')
    if len(pin) == 4:
        print(True)
    elif len(pin) == 6:
        print(True)
    else:
        print(False)

print(is_valid_PIN())