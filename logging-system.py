users = {'malgo':'toddler',
'mati':'freak'}

def welcome ():
    print("Welcome to MyApp!")
    decision = input("If you are a new user, please register by typing 'R'. \nIf you already have an account, type 'L' and log in")
    return decision

def logging ():
    username = input("Please provide user name")
    if username not in users:
        print("This user name does not exist")
    else:
        password = input("Please provide password")
        if password == users[username]:
            print("You are logged in, " + username + "!")
        else:
           print("Incorrect password")
            

def register():
    username = input("Please provide user name")
    if username in users:
        print("This user already exists")
    else:
        password = input("Please type the new password")
        confirm_password = input("Please confirm your password")
        if password == confirm_password:
            users[username] = password
        else: 
            print("The passwords don't match")

print("Welcome to MyApp!")
decision = input("If you are a new user, please register by typing 'R'. \nIf you already have an account, type 'L' and log in")
    
if decision == "L":
    logging()
elif decision == 'R':
    register()
else:
    print("The only acceptable responses are R or L")

print(users)
