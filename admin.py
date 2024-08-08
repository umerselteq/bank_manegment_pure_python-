
import json

#admin class
class admin:

    def __init__(self):
        pass

    #details of all users
    def show_details(self):
        f = open("users.json",'r')
        a = json.load(f)
        dict = {}
        dict = a
        print("id" , "name" , "email")
        for i in range( 0 , len(dict)):
            print(dict[i]['id'],dict[i]['name'],dict[i]['email'])
        f.close()
        return


    def show_history(self):
        f = open("users.json",'r')
        data = json.load(f)
        print("1.All \n 2.One user")
        choice = input("Enter your choice: ")
        if choice == "1":
            for i in range(0, len(data)):
                print(data[i]['name'] , data[i]['history'])

        if choice == "2":
            email = input("Enter user email:")
            condition = False
            for i in range( 0 , len(data)):
                if email == data[i]['email']:
                    condition = True
                    print(data[i]['name'],data[i]['history'])

            if condition == False:
                print("no such user")



    def delete_user(self):
        email = input("Enter user email:")
        f = open("users.json", 'r')
        data = json.load(f)
        condition = False
        for i in range(0, len(data)-1):
            if email == data[i]['email']:
                print(data[i]['email'])
                condition = True
                del data[i]
                f = open("users.json", 'w')
                json.dump(data, f)
                f.close()
                print("deleted user")
                return

        if condition == False:
            print("no such user")



    def freeze_user(self):
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

        print("user not found")










