import string
import random

def passwordgenerator(length: int):
    
    password = []
    for i in range(length):
        randomchar = ''.join(random.choices(string.ascii_letters + string.digits + string.printable))
        password.append(randomchar)
        
    return ''.join(password)

print(passwordgenerator(8))