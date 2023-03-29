import random
import string

# How to generate a random password in Python
# You can generate as long password as you want!
def generate_password(digits, lowercase_letters, uppercase_letters, punctuations, length):
    chars = digits + lowercase_letters + uppercase_letters + punctuations
    password = ''.join(random.choice(chars) for i in range(length))
    # if len(password) > 
    print(password)
    return password


digits = string.digits
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
punctuations = string.punctuation

# you can set the length manually like below:
# length = 0

length = len(string.digits)

generate_password(digits, lowercase_letters, uppercase_letters, punctuations, length)

    