#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password_easy = ""
for let in range(nr_letters):
	index_l = random.randint(0,len(letters)-1)
	password_easy += letters[index_l]

for symb in range(nr_symbols):
	index_s = random.randint(0,len(symbols)-1)
	password_easy += symbols[index_s]

for number in range(nr_numbers):
	index_n = random.randint(0,len(numbers)-1)
	password_easy += numbers[index_n]

print("Your password is: " + password_easy)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_hard = ""
list_of_chars = []
for let in range(nr_letters):
	index_l = random.randint(0,len(letters)-1)
	list_of_chars.append(letters[index_l])

for symb in range(nr_symbols):
	index_s = random.randint(0,len(symbols)-1)
	list_of_chars.append(symbols[index_s])

for number in range(nr_numbers):
	index_n = random.randint(0,len(numbers)-1)
	list_of_chars.append(numbers[index_n])

randomized_list = random.sample(list_of_chars,len(list_of_chars))
for char in randomized_list:
	password_hard += char

print("")
print("A better password would be: " + password_hard)
