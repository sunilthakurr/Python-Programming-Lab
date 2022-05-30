# dictionary comprehension : It is  a way to create a dictionary using iterables

dictionary = {}

for i in range(6):
    if(i % 2 ==0 ):
        dictionary[i] = i*i 

print(dictionary)


