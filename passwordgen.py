import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

while 1:
    pass_length = int(input("what length do you want your password to be : "))
    pass_count = int(input("how many passwords would you like : "))
    for x in range(0,pass_count) :
        password = ""
        for x in range(0,pass_length) :
            password_chars = random.choice(chars)
            password       = password + password_chars
            print("your password is : ", password)

