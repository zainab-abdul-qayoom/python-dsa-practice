
import math

temp_cel = input("Enter Temp in Celcius: ")
temp_feh = int(temp_cel) * 9/5.0 + 32
res =  f' Temperature in Fehrenheit = {temp_feh}'
print(res)


num_1 = input("Enter Number 1: ")
num_2 = input("Enter Number 2: ")
print( int(num_1) + int(num_2))
print(int(num_1) - int(num_2))
print(int(num_1) * int(num_2))
print(int(num_1)/int(num_2))

num = input('Enter a number: ')
# return ans in float
print(int(num) / 2)
# return ans in int
print(int(num) // 2)

sen = input("Enter a sentence: ")
print(len(sen))

sent = input("Enter a sentence: ")
print(sent.upper())
print(sent.lower())

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = f' Your Last name is {last_name} and First name is {first_name}'
print(full_name)

number = input("Enter a number: ")
print(math.sqrt(int(number)))

sentence = input('Enter a sentence with extra spaces: ')
cleaned = sentence.strip()
print(f"' {cleaned}'")