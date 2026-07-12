import random
chars="asdfghjklxcvbnmqwertyuio!@#$%^&*()1234567890"
length=int(input("Enter length:"))
password=""
for a in range(length):
    password+=random.choice(chars)
print(password)
