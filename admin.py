
import json

"""  admin class for admin functionalities like
showing the details of all users , freeze/unfreeze users account"""
class admin:
    def __init__(self):
        pass

    """ showing the details of every user in the database """
    def show_details(self):
        try:
            f = open("users.json", 'r')
            a = json.load(f)
            dict = a
            print("id", "name", "email")
            for i in range(0, len(dict)):
                print(dict[i]['id'], dict[i]['name'], dict[i]['email'])
            f.close()
            return
        except FileNotFoundError as e:
            print(e)
            return

    """ showing the history of transaction of all/each user in the database """
    def show_history(self):
        try:
            f = open("users.json", 'r')
            data = json.load(f)
            print("1.All \n 2.One user")
            choice = input("Enter your choice: ")
            if choice == "1":
                for i in range(0, len(data)):
                    print(data[i]['name'], data[i]['history'])

            if choice == "2":
                email = input("Enter user email:")
                for i in range(0, len(data)):
                    if email == data[i]['email']:
                        print(data[i]['name'],data[i]['history'])
                else:
                    print("no such user")

        except FileNotFoundError as e:
            print(e)


    """ delete a user from the database """
    def delete_user(self):
        try:
            email = input("Enter user email:")
            f = open("users.json", 'r')
            data = json.load(f)
            for i in range(0, len(data)-1):
                if email == data[i]['email']:
                    print(data[i]['email'])
                    del data[i]
                    f = open("users.json", 'w')
                    json.dump(data, f)
                    f.close()
                    print("deleted user")
                    return

            print("no such user")
        except FileNotFoundError as e:
            print(e)


    """ freeze the user account so he cant logged in """
    def freeze_user(self):
        try:
            f = open("users.json", 'r')
            data = json.load(f)
            email = input("Enter person email:")

            for i in range(0, len(data)):
                if email == data[i]['email']:
                    data[i]['freeze'] = True
                    f = open("users.json", 'w')
                    json.dump(data, f)
                    f.close()
                    print("User freeze")
                    return
            else:
                print("user not found")
        except FileNotFoundError as e:
            print(e)
            return

    """ unfreeze the user account """
    def unfreeze_user(self):
        try:
            f = open("users.json", 'r')
            data = json.load(f)
            email = input("Enter person email:")

            for i in range(0, len(data)):
                if email == data[i]['email']:
                    data[i]['freeze'] = False
                    f = open("users.json", 'w')
                    json.dump(data, f)
                    f.close()
                    print("User unfreeze")
                    return
            else:
                print("user not found")
        except FileNotFoundError as e:
            print(e)
            return









