# names = ['John', 'Mosh', 'Sarah', 'Mary', 'Bob']
# print(names[-1])
# print(names[2:])
# print(names[2])
# print(names[2: 4])
# print(names[:])

# names[0] = 'Jon'
# print(names)

# write a program to find the largest number in the list
list = [10, 38, 5, 89, 76, 54]
largest = list[0]
for item in list:
    if(item > largest):
        largest = item
print(f'Largest Number in list is {largest}')        