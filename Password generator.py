import random
length = int(input("how many characters? "))
characters = ["!", "@", "#", "$", "%"]
password = ""
for i in range(length):
    password += random.choice(characters)
print(password)