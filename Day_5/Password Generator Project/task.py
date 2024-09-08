import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#easy level
# password = ""
# for l in range(1, nr_letters+1):
#     choice = random.choice(letters)
#     password += choice
#
# for s in range(1, nr_symbols+1):
#     choice = random.choice(symbols)
#     password += choice
#
# for n in range(1, nr_numbers+1):
#     choice = random.choice(numbers)
#     password += choice


# print(password)


password = []
for l in range(1, nr_letters+1):
    choice = random.choice(letters)
    password.append(choice)

for s in range(1, nr_symbols+1):
    choice = random.choice(symbols)
    password.append(choice)

for n in range(1, nr_numbers+1):
    choice = random.choice(numbers)
    password.append(choice)

generate_pass = ""

for i in range(1, len(password)+1):
    choice = random.choice(password)
    generate_pass += choice
    password.remove(choice)

print(generate_pass)