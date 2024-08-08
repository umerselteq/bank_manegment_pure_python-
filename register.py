from admin import admin
import json
import hashlib

#before creating the user checking unique
def before_creating(func):
    def wrapper(self, name, password, email):
        #print('creating')
        try:
            f = open('users.json' , 'r')
            a = json.load(f)
            dict = a
            for i in range(0,len(dict)):
                if dict[i]['email'] == email:
                    print('Email already registered')
                    return
            func(self, name, password, email)
        except Exception as e:
         print(e)
         func(self, name, password, email)
    return wrapper

#geting unique id
def unique_id():
    #print('in Unique ID')
    try:
        f = open('users.json','r')
        a = json.load(f)
        dict=a[-1]
        return dict['id'] + 1
    except Exception as e:
        print(e)
        return 1



class register(admin):

    #__id = None #id for every user

    def __init__(self):
        self._name = None
        self._password = None
        self._email = None
    @before_creating
    def create_account(self, name, password, email):
        id = unique_id()
        password = hashlib.sha256(password.encode()).hexdigest()
        print(password)
        try:
          f = open('users.json', 'r')
          users = json.load(f)
          #print(users)
        except json.JSONDecodeError:
            users = []

        dict = {
            'id': id,
            'name': name,
            'password': password,
            'email': email,
            'history': [],
            'amount': 0,
            'freeze': False
        }
        #print(dict)
        users.append(dict)
        f = open("users.json", 'w')
        json.dump(users, f)
        f.close()
        print("user registered")