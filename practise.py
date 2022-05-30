dictionary = {'Name':'Sunil kumar','Roll Number':49,'Section':'F','College':'GLA'}
print(dictionary['Name'])                         # used to get the value of given key
print(dictionary.get('Name'))                     # same as above but it will not throw error when key is not found
print(dictionary.get('Village'))                   # give None as output if key is not found
#print(dictionary['village'])                       # give key error if key is not found in dictionary



my_dict = dict([(1,'apple'), (2,'ball')])
print(my_dict.get(1))