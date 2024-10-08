from user import user
import json
import datetime
x = datetime.datetime.now()


""" class Transaction:
it will be responsible for handling users all the money related functions
like deposite amount withdraw and transfer amount to other users """
class transaction(user):

    def __init__(self):
        self._amount = None
        #self._select = None

    """ deposit amount """
    def deposit(self , amount):
        try:
            #opening file and geting the data
            f = open('users.json', 'r')
            data = json.load(f)
            #print("select value in child:", user._select)
            dictt = data
            person = dictt[user._select]
            #adding amount against the user
            if 'amount' in person.keys():
                person['amount'] += amount
            else:
                person['amount'] = amount

            person['history'].append(f"deposit {amount} Date:{(x.strftime("%d-%m-%Y"))}")
            #adding the updated data back to file
            dictt[user._select] = person  #updating the dict amount
            #print(type(dictt))
            f = open('users.json', 'w')
            json.dump(dictt,f)
            f.close()
            print("cash deposited")
        except Exception as e:
            print(e)


    """ withdraw amount """
    def withdraw(self, amount):
        try:
            f = open('users.json', 'r')
            data = json.load(f)
            dictt = data
            person = dictt[user._select]
            if 'amount' in person.keys():
                if amount < person['amount']:
                    person['amount'] -= amount
                    person['history'].append(f"withdraw {amount} Date:{(x.strftime("%d-%m-%Y"))}")
                else:
                    print("enter smaller amount you dont have enough balance")
                    return
            else:
                print("no balance")
                return
            dictt[user._select] = person  #updating the dict amount of that perticuler user
            #print(dictt)
            f = open('users.json', 'w')
            json.dump(dictt, f)
            f.close()
            print("cash withdrawn")
        except Exception as e:
            print(e)






    """ logged user transfer money to another user with limit smaller then 1000"""
    def transfer(self):
        try:
            user2 = None
            email = input("Enter other email:")
            f = open('users.json', 'r')
            data = json.load(f)
            print(data)
            person = data[user._select]

            for i in range(0, len(data)):
                if email == data[i]['email']:
                    index = i
                    user2 = data[i]  #user where to send money
                    print("user found :", user2)
                    break
            if user2 is None:
                print("user not found")
                return

            #transfer amount
            amount = int(input("Enter amount:"))
            if amount > 1001:
                print("out of limit enter smaller amount")
                return

            #checking if the person has enough money
            if person['amount'] > amount:
                if 'amount' in user2.keys():
                    user2['amount'] += amount
                    person['amount'] -= amount
                else:
                    user2['amount'] += amount
                    person['amount'] -= amount
            else:
                print("enter smaller amount you dont have enough balance")
                return

            #seting history list
            person['history'].append(f"send {amount} Date:{(x.strftime("%d-%m-%Y"))}")
            user2['history'].append(f"received {amount} Date:{(x.strftime("%d-%m-%Y"))}")
            #updating data with new values
            print("amount transferred")
            data[user._select] = person
            data[index] = user2
            #print(data)
            f = open('users.json', 'w')
            json.dump(data,f)
            f.close()
        except Exception as e:
            print(e)











