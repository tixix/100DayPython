# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


def generate_password():
    # initialize emtpy password
    password = ""

    # 3 for loops for each
    selected_letters = [' ' for i in range(nr_letters)]
    for i in range(nr_letters):
        index_letters = random.randint(0, len(letters) - 1)
        selected_letters[i] = letters[index_letters]

    selected_symbols = [' ' for i in range(nr_symbols)]
    for i in range(nr_symbols):
        index_symbols = random.randint(0, len(symbols) - 1)
        selected_symbols[i] = symbols[index_symbols]

    selected_numbers = [' ' for i in range(nr_numbers)]
    for i in range(nr_numbers):
        index_numbers = random.randint(0, len(numbers) - 1)
        selected_numbers[i] = numbers[index_numbers]

    password = selected_letters + selected_symbols + selected_numbers
    return password


# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
def generate_password_order_randomised():
    password_not_randomised = generate_password()
    password_randomised = ""
    while len(password_not_randomised) != 0:
        char = random.choice(password_not_randomised)
        password_randomised += char
        password_not_randomised.remove(char)
    return password_randomised


password = generate_password_order_randomised()
print(f'Your password is: {password}')
