from admin import admin
from register import register
from user import user
from transaction import transaction

if __name__ == '__main__':
    while True:
        print(" 1.Admin\n 2.User")
        choice = int(input("Enter your choice:"))
        condition = True

        if choice == 0:
            print("Exiting")
            break

        if choice == 1:
            admin = admin()
            while condition:
                print(" 1.Create Account\n 2.Show Details \n 3.Show History \n 4.delete user \n 5.Freeze \n 6.Exit")
                choice = int(input("Enter your choice:"))

                if choice == 1:
                    name = input("Enter your name:")
                    password = input("Enter your password:")
                    email = input("Enter your email:")
                    reg = register()
                    reg.create_account(name, password, email)
                elif choice == 2:
                    admin.show_details()
                elif choice == 3:
                    admin.show_history()
                elif choice == 4:
                    admin.delete_user()
                elif choice == 5:
                    admin.freeze_user()
                elif choice == 6:
                    condition = False
                else:
                    print("Invalid choice")


        elif choice == 2:
            user = user()
            transaction = transaction()
            check = False

            while check == False:
                email = input("Enter your email:")
                password = input("Enter your password:")
                check = user.login(email, password)
                print(check)


            while condition:
                if check == True:
                    print(" 1.Deposit Amount\n 2.Withdraw Amount \n 3.Check balance \n 4.Transfer Amount \n 5.History \n 6.change password \n 7.Exit")
                    choice = int(input("Enter your choice:"))
                    if choice == 1:
                        amount = int(input("Enter your amount:"))
                        transaction.deposit(amount)
                    elif choice == 2:
                        amount = int(input("Enter your amount:"))
                        transaction.withdraw(amount)
                    elif choice == 3:
                        user.check_balance()
                    elif choice == 4:
                        transaction.transfer()
                    elif choice == 5:
                        user.history()
                    elif choice == 6:
                        user.change_password()
                    elif choice == 7:
                        condition = False
                    else:
                        print("Invalid choice")





