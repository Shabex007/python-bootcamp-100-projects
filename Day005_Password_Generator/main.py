import string
import random

lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)

# Combine lowercase and uppercase letters into one list
letters = lowercase_letters + uppercase_letters

numbers = list(string.digits)
symbols = list(string.punctuation)

print("Welcome to the password generator!\n")

l = int(input("How many letters do you want? "))
n = int(input("How many numbers do you want? "))
s = int(input("How many symbols do you want? "))

password_list = []

# Add letters
for _ in range(l):
    password_list.append(random.choice(letters))

# Add numbers
for _ in range(n):
    password_list.append(random.choice(numbers))

# Add symbols
for _ in range(s):
    password_list.append(random.choice(symbols))

# Shuffle the password list
random.shuffle(password_list)

# Convert list to string
password = ''.join(password_list)

print("Your generated password is:", password)
 