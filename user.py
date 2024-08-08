import json
import hashlib

class user:
    _select = None

    def __init__(self):
        self._email = None
        self._password = None

    def login(self, email, password):
        f = open('users.json', 'r')
        data = json.load(f)
        dictt = data


        #hashing the password
        password = hashlib.sha256(password.encode()).hexdigest()
        #verifying email and password
        for i in range(0, len(dictt)):
            if dictt[i]['email'] == email:
                if dictt[i]['password'] == password:
                    user._select = i
                    if dictt[i]['freeze'] == True:
                        print("your account is freezed")
                        return False
                    print(dictt[i]['name'], 'Login Successful')
                    return True
                else:
                    print("wrong password")
                    return False
        print("no such email")
        return False



    def check_balance(self):
        try:
            f = open('users.json', 'r')
            data = json.load(f)
            print("Balance:" ,data[user._select]['amount'])
        except Exception as e:
            print(e)
            print("no balance")


    def history(self):
        f = open('users.json', 'r')
        data = json.load(f)
        print(data[user._select]['history'])
        f.close()


    def change_password(self):
        f = open('users.json', 'r')
        data = json.load(f)
        password = input("enter new password:")
        password = hashlib.sha256(password.encode()).hexdigest()
        data[user._select]['password'] = password
        f = open('users.json', 'w')
        json.dump(data, f)
        f.close()
        print("password changed")





