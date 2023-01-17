#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password_letters = random.choices(letters, k = nr_letters)
password_symbols = random.choices(symbols, k = nr_symbols)
password_numbers = random.choices(numbers, k = nr_numbers)

password_string = ""
for letter in password_letters:
  password_string += letter

symbols_string = ""
for symbol in password_symbols:
  #symbols_string += symbol
  password_string += symbol
number_string = ""
for number in password_numbers:
  #number_string += number
  password_string += number
  
#easy_password = password_string + symbols_string + number_string

hard_password = random.sample(password_string, k = len(password_string))
hard_password_string = ""
for letter in hard_password:
  hard_password_string += letter

easy_or_hard = input("Do you want the 'easy' or 'hard' password?\n")
if easy_or_hard == "easy":
  print("The easy password is:\n")
  print(password_string) 
else:
  print("The hard password is:\n")
  print(str(hard_password_string))

input("Press any key, then enter to exit.\n")