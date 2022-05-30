# Removing elements from dictionary

dictionary = {'Name' : 'Sunil','Adress': 'Downtown','Height':179}

# using pop
out = dictionary.pop('Name')
print(out)
print(dictionary)


# using popitem

out = dictionary.popitem()
print(out)
print(dictionary)


# using clear

dictionary.clear()
print(dictionary)


# using del

del dictionary
print(dictionary)                      # give NameError     : dictionary is not defined


