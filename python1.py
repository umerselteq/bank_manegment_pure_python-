# class class1:
#     __x = 1   #class variable private
#
#     def __init__(self , name ):
#        self.name = name  #instance variable
#
#     def display(self):
#        print(self.x)
#
# obj1 = class1("umer" )
# print(obj1.name)
# obj1.name = "amir"
# print(obj1.name)
import json

# class Alphabet:
#     def __init__(self, value):
#         self._value = value
#
#     # getting the values
#     def getValue(self):
#         return self._value
#
#     # setting the values
#     def setValue(self, value):
#         print('Setting value to ' + value)
#         self._value = value
#
#     # deleting the values
#     def delValue(self):
#         print('Deleting value')
#         del self._value
#
#     value = property(getValue, setValue, delValue, )
#
#
# # passing the value
# x = Alphabet('GeeksforGeeks')
# print(x.value)
# x.value = 'GfG'
# print(x.value)


# import pickle
#
# # initializing data to be stored in db
# Omkar = {'key': 'Omkar', 'name': 'Omkar Pathak',
#          'age': 21, 'pay': 40000}
# Jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak',
#            'age': 50, 'pay': 50000}
#
# # database
# db = {}
# db['Omkar'] = Omkar
# db['Jagdish'] = Jagdish
#
# print(db)
#
# # For storing
# # type(b) gives <class 'bytes'>;
# b = pickle.dumps(db)
# print(b)
#
# # For loading
# myEntry = pickle.loads(b)
# print(myEntry)

# f = open("demofile.txt","a")
# f.write("Hello World\n")
# f.close()

# f = open("demofile.txt","r")
# a = f.read()
# print(a)
# f = open("demofile.txt","w")
#
#
# f.close()

import hashlib

# list = [{"id": 2, "name": "umer", "email": "umer@"}, {"id": 4, "name": "ali", "email": "ali@", 'amount': 100}]
#
#
# print(type(list))
# print(type(list[1]))
# list[1]['history'] = ['deposit : 1000']
# print(list[1])
# list[1]['history'].append('withdraw : 100')
# print(list[1])

a = "1234"
print(type(a))
h = hashlib.sha256()
h.update(a.encode())
b = h.hexdigest()
print(b)
print(a)

c = "1234"
print(type(c))
h = hashlib.sha256()
h.update(c.encode())
d = h.hexdigest()
print(d)
print(c)

if d == b:
    print("equal")





# print(type(list))
# print(list[-1])

# for i in range(0, len(dict)):
#     if dict[i]['id'] == 4:
#         print(dict[i]['name'])
#         print(i)
#         # dict[i]['amount'] = 1000
#         # print(dict[i])
#         if 'amount' in dict[i].keys():
#             dict[i]['amount'] += 100
#         else:
#             dict[i]['amount'] = 100
#         print(dict[i])
#         break
#

# print(dict)
# print(type(dict))
# for i in dict:
#     if dict[i]["email"] == email:
#       print(dict[i]['email'])
#       break
#     else:
#         print("ok")
