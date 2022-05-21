import numpy as np 
numbers_str = "1 2 3.2 4 5"
numbers_list =[]
for num_str in numbers_str.split ():
    num_float = float (num_str)
    numbers_list.append (num_float)
arr = np.array (numbers_list)
out = np.around (arr) 
print (out)
