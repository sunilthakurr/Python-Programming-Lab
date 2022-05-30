def string_list_to_tuple(str1):
    result = tuple(x for x in str1 if not x.isspace()) 
    return result
str1 = "python 3.0"
print("Original string:")
print(str1)
print(type(str1))
print("Convert the said string to a tuple:") 
print(string_list_to_tuple(str1))
print(type(string_list_to_tuple(str1)))
