import random


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  # 5
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # 4
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']  # 2

    password = []
    for i in range(0, 5, 1):
        letter = letters[random.randint(0, len(letters) - 1)]

        password.append(letter)

    for i in range(0, 4, 1):
        number = numbers[random.randint(0, len(numbers) - 1)]

        password.append(number)

    for i in range(0, 2, 1):
        symbol = symbols[random.randint(0, len(symbols) - 1)]

        password.append(symbol)

    random.shuffle(password)
    result = ''.join(password)

    return result
