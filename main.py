#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

int_letters = int(input("How many letters do you want?"))
int_numbers = int(input("how many numbers do you want?"))
int_symbols = int(input("how many symbols do you want?"))

password=[]
for char in range(1,int_letters+1):
  password += random.choice(letters)
  #print(password)

for i in range(1,int_numbers +1):
  password += random.choice(numbers)
  #print(password)

for s in range(1+int_symbols+1):
  password += random.choice(symbols)
  #print(password)

random.shuffle(password)
#print(password)

password_str =""

for char in password:
  password_str += char

print(f"Your password is {password_str}")














#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P