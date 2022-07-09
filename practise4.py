# using different dictionary methods


from webbrowser import get


dictionary = {'Name' : 'Sunil','Adress': 'Downtown','Height':179}


# 1. using copy                  : It returns a shallow copy of dictionary

new_dictionary = dictionary.copy()
print(new_dictionary)



# 2. using fromkeys

marks = {}.fromkeys(['Physics','Mechanical','Python','Electrical'],49)
print(marks)




# using get(key[,-1])

print(marks.get('Physics',-1))
print(marks.get('Chemistry',-1))
