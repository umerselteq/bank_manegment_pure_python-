import json
import hashlib

""" class user: it will be responsible for user actions like
logging in , checking his transaction history , changing his password and checking his balance"""
class user:
    _select = None

    def __init__(self):
        self._email = None
        self._password = None

    """ logging user if verified return true otherwise return false  """
    def login(self, email, password):
        try:
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
        except Exception as e:
            print(e)
            return False

    """ checking user balance in the bank """
    def check_balance(self):
        try:
            f = open('users.json', 'r')
            data = json.load(f)
            print("Balance:", data[user._select]['amount'])
        except Exception as e:
            print(e)
            print("no balance")

    """ checking history of transactions """
    def history(self):
        try:
            f = open('users.json', 'r')
            data = json.load(f)
            print(data[user._select]['history'])
            f.close()
        except Exception as e:
            print(e)

    """ changing the password of logged user """
    def change_password(self):
        try:
            f = open('users.json', 'r')
            data = json.load(f)
            password = input("enter new password:")
            password = hashlib.sha256(password.encode()).hexdigest()
            data[user._select]['password'] = password
            f = open('users.json', 'w')
            json.dump(data, f)
            f.close()
            print("password changed")
        except Exception as e:
            print(e)





