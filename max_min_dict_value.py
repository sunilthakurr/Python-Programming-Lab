# Write a Python program to get the maximum and minimum value in a dictionary.


dictionary = {1:1,2:4,3:9,4:16}

max = list(dictionary.items())[0][1]
min = max

for i in (dictionary):
    if max < dictionary[i]:
        max = dictionary[i]
    if min > dictionary[i]:
        min = dictionary[i] 

print(f"Maximum value is {max} while the minimum value is {min}")           