def login():
    username_vault = ["john", ]
    password_vault = ["smith", ]
    choose = input(
        "Do you want to create a account or login? Type login for logging in or type create for creating an account: ")
    choose.lower()
    six = 6
    if choose == "create":
        Create()
    elif choose == "login":
        logging()
    else:
        print("there was a error, make sure you typed everything correctly")
    # create an accounty
    def Create():
        print("create an account")
        username = input("Username: ")
        username.lower()
        if len(username) < six:
            print("you need at least 6 characters")
            username = input("Username: ")
            username.lower()
            if len(username) < six:
                print("you need at least 6 characters")
            elif len(username) > six:
                password = input("Password: ")
            else:
                print("username needs at least 6 characters long try again")
        elif len(username) > six:
            password = input("Password: ")
            if True:
                if any(username in word for word in username_vault):
                    print("this username already exists")
                elif any(username in word for word in username_vault) and any(
                            password in word for word in password_vault):
                    print("you already have an account")
                else:
                    print("you created an account")
                    username_vault.append(username)
                    password_vault.append(password)
                print("-" * 50)
                print("login")
                username3 = input("Username: ")
                password3 = input("Password: ")
                if True:
                    if any(username3 in word for word in username_vault) and any(
                            password3 in word for word in password_vault):
                        print("you logged in")
                    elif any(username3 in word for word in username_vault) and any(
                            password3 not in word for word in password_vault):
                        print("Wrong Password")
                    else:
                        print("error")

                print("-" * 50)

    # logging in
    def logging():
        print("login")
        username2 = input("Username: ")
        password2 = input("Password: ")
        if True:
            if any(username2 in word for word in username_vault) and any(password2 in word for word in password_vault):
                print("you logged in")
            elif any(username2 in word for word in username_vault) and any(
                        password2 not in word for word in password_vault):
                print("Wrong Password")
            else:
                print("This account does not exist")
        else:
            print("error")
    print("-" * 50)
        
question = input("Do you want to login? Y or N")
question.lower()
if question == "y":
    print("ok")
    login()
elif question == "n":
    print("ok")
    exit

