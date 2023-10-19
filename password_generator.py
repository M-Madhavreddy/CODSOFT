import random
import string

def generate_password(length):
    
    characters = string.ascii_lowercase
    password = [random.choice(characters)]
    
    characters = string.ascii_uppercase
    password.append(random.choice(characters))
    
    characters = string.digits
    password.append(random.choice(characters))
    
    characters = string.punctuation
    password.append(random.choice(characters))
    
    characters = string.ascii_letters + string.digits 
    if length > 4 :
        for _ in range(length - 4):
            random_char = random.choice(characters)
            password.append(random_char)
    
    random.shuffle(password)
    return ''.join(password)

try:
    password_length = int(input("Enter the desired password length (atleast 4 characters): "))
    if password_length < 4:
        print("Password length must be atleast 4 characters.")
    else:
        password = generate_password(password_length)
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid integer for the password length.")

