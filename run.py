   
import gspread
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError
import colorama 
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('retro-bank')
global gsheet 
gsheet = SHEET

def emailcheck(emailinput):
    """
    Email validator function
    Checks the new email is valid
    """
    try:
        valid = validate_email(emailinput)
        emailinput = valid.email
        return emailinput
    except EmailNotValidError as e:
        print("The email you provided is not valid please try again\n")


def registerEmail():
    """
    This fucntion checks the email address is correct 
    while loop will continue until a valid email is input
    """

    print("Welcome to retro bank As a new customer\n" +
        "Please complete the following fields to sign up for an account\n")

    while True:
        try:
            global email
            email = input("Please enter your email address: ")
            email = email.lower()
            einput = emailcheck(email)
            if einput != email:
                raise ValueError(
                    "Please enter a valid email" +
                    f" you entered: {email}"
                )
            else:
                regDetails()
                return email
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")


def regDetails():
    """
    This function adds the new customers
    details to the google sheet long with new balance
    """

    sheet = SHEET.worksheet("customer-data")
    new_cust = []
    bonus = 500
    

    while True:
        name = input("Please enter your full name: ")
        password = input("Please enter your password: ")
        if name == "":
            print("Name is required")
        elif password == "":
            print("Password Required")
        else:
            worksheet = gsheet.add_worksheet(title=email, rows="100", cols="20")
            new_cust.append(email)
            new_cust.append(name)
            new_cust.append(password)
            new_cust.append(bonus)
            worksheet.append_row(new_cust)
            print("WELCOME TO RETRO BANK !" +
            " As a new customer you will receive £500 joining bonus")
            login()
            break


def login():
    """
    This function checks the email address is valid in the 
    google sheets ie worksheet.
    """

    global ename
    global epass
   

    while True:
        try:
            ename = input("Please enter your email address: ")
            ename = ename.lower()
            ename = str(ename)
            email_ver = gsheet.worksheet(ename)
        except:
            print("Invalid Email ! \nPlease try again: ")
            login()
        else:
            verify()
            break


def verify():
    """
    This function checks the email address and password is correct
    so the customer can log into the dash board.
    """

    epass = input("Please enter your password: ")

    global email_ver
    global details
    global password
    global balances
    global username
    email_ver = SHEET.worksheet(ename)
    details = email_ver.col_values(1)
    username = email_ver.col_values(2)
    password = email_ver.col_values(3)
    balances = email_ver.col_values(4)
    user = []

    user.append(ename)
    user.append(epass)

    found = 0

    for i in zip(details, password):
        if i == tuple(user):
            found = 1
            print("Successfully Verified")
            mainMenu()
            return found
    if found == 0:
        print("The username or the password you provided might be wrong.\n")
        login()
        return found


def mainMenu():
    while True:
        try:
            print(f"WELCOME {username[0]} TO YOUR ACCOUNTS DASHBOARD")
            print("Please Select from the following menu")
            print("1. Account Balance")
            print("2. Deposit Money")
            print("3. Withdrawal")
            choice = input("")
            if choice != "1" and choice != "2" and choice != "3":
                raise ValueError(
                    "Enter 1 for new customer or 2 for existing customer," +
                    f"you entered: {choice}"
                )
            elif choice == "1":
                balance()
            elif choice == "2":
                deposit()
            elif choice == "3":
                withdrawal()
            else:
                return choice
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")


def balance():
    user = SHEET.worksheet(ename)
    balance = user.col_values(4)
    value = balance[0]
    print(f"The balance of your account is {value}")
    
    while True:
        try:
            choice = input("If you would like to complete an other transactions please 1 for main menu " +
                           "If you would like to log out its 2:\n")
            if choice != "1" and choice != "2":
                raise ValueError(
                    "Enter 1 for new customer or 2 for selection" +
                    f"you entered: {choice}"
                )
            elif choice == "1":
                mainMenu()
            else:
                exit()
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")


def deposit():
    user = SHEET.worksheet(ename)
    balance = user.col_values(4)
    value = balance[0]
    value = int(value)
    

    while True:
        try:
            choice = input("How much would you like to deposit ? ")
            choice = int(choice)
            if choice != int(choice):
                raise ValueError(
                    "Please enter a valid amount" +
                    f"you entered: {choice}"
                )
            else:
                new = value + choice
                newBalance = user.update("D1", new)
                print(f"The balance of your account is now {new}")
                break
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")


    while True:
        try:
            choice = input("If you would like to complete an other transactions please 1 for main menu " +
                           "If you would like to log out its 2:\n")
            if choice != "1" and choice != "2":
                raise ValueError(
                    "Enter 1 for new customer or 2 for selection" +
                    f"you entered: {choice}"
                )
            elif choice == "1":
                mainMenu()
            else:
                exit()
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")


def withdrawal():
    user = SHEET.worksheet(ename)
    balance = user.col_values(4)
    value = balance[0]
    value = int(value)
    

    while True:
        try:
            choice = input("How much would you like to withdraw ? ")
            choice = int(choice)
            if choice != int(choice):
                raise ValueError(
                    "Please enter a valid amount" +
                    f"you entered: {choice}"
                )
            else:
                if value >= choice:
                    new = value - choice
                    newBalance = user.update("D1", new)
                    print(f"The balance of your account us {new}")
                    break
                else:
                    print("You have insufficient funds \n"+
                    f"The Balance of your account is {value}")
                    break
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")

    while True:
        try:
            choice = input("If you would like to complete an other transactions please 1 for main menu " +
                           "If you would like to log out its 2:\n")
            if choice != "1" and choice != "2":
                raise ValueError(
                    "Enter 1 for new customer or 2 for selection" +
                    f"you entered: {choice}"
                )
            elif choice == "1":
                mainMenu()
            else:
                exit()
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")


def welcome():
    """
    This function is the first option the user is given 
    to select if they are a new user or existing user
    """
    while True:
        try:
            print("")
            print(Back.RED + Style.BRIGHT + "If you are a new customer please enter 1:")
            print(Back.BLUE + Style.BRIGHT + "If you are already are an existing customer please enter 2:")
            print("")
            choice = input("")
            if choice != "1" and choice != "2":
                raise ValueError(
                    "Enter 1 for new customer or 2 for existing customer," +
                    f"you entered: {choice}"
                )
            else:
                return chosen(choice)
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")


def chosen(choice):
    """
    Once a valid user selection has been made in the
    welcome function. This will then direct the user to
    the appropriate new or existing user function
    """
    if choice == "1":
        registerEmail()
    elif choice == "2":
        login()

print("")
print(Fore.GREEN +"+++++++++++++++++++++++++++++++++++")
print("")
print(Fore.BLACK + Back.YELLOW + Style.BRIGHT + "               WELCOME             ")
print("")
print(Fore.BLACK + Back.YELLOW + Style.BRIGHT + "                 TO                ")
print("")
print(Fore.BLACK + Back.YELLOW + Style.BRIGHT + "              RETRO BANK           ")
print("")
print(Fore.GREEN +"+++++++++++++++++++++++++++++++++++")
welcome()
