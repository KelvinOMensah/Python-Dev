import random 

import string

length = int(input("How long do you want your password to be: "))
number_of_letters = int(input("How many letters: "))
number_of_numbers = int(input("How many numbers: "))
number_of_symbols = int(input("How many symbols: "))

if number_of_numbers + number_of_symbols + number_of_letters != length:
    print("Your numbers do not add up to the password length")
else:
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password = " "

    for _ in range(number_of_letters):
        password += random.choice(letters)

    for _ in range(number_of_numbers):
        password += random.choice(numbers)

    for _ in range(number_of_symbols):
        password += random.choice(symbols)


    password = "".join(random.sample(password,len(password)))
    print(f"Your password is {password}")
