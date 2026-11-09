# numbers = [2, 7, 3, 4, 7, 8]

# numbers.append(20) # add the number in last of list
# numbers.insert(2, 30) # add/insert number in b/w the list
# numbers.remove(3)
# # numbers.clear() # to remove all the items from list
# numbers.pop() # remove the last item or number from the list

# print(numbers)

# print(numbers.index(7)) # returns the index of the number from list 
# # or
# print(50 in numbers) # return boolean True if the valur exists in list else False

# print(numbers.count(7)) # returns 2 bec there are 2 7ns are in list  

# numbers.sort() # sorts the list in increasing order
# print(numbers)
# numbers.reverse() # sorts the list in descending order
# print(numbers)

# numbers2 = numbers.copy() # copy the numbers list  
# numbers.append(6) # but if we make change in original list it doesn't effect our copied list
# print(numbers)
# print(numbers2)

# challenge: remove the duplicates in the list
nums = [2, 4, 5, 7, 9, 10, 4, 3, 2, 4]
unique = []
for num in nums:
    if num not in unique:
        unique.append(num)
print(unique)