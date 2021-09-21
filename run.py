import gspread
from google.oauth2.service_account import Credentials
from email_validator import validate_email,EmailNotValidError

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('retro-bank')

def emailcheck(emailinput):
    """
    Email validator function
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
    while loop will continue until a valid emai is input
    """

    print("Welcome to retro bank As a new customer\n" +
        "Please complete the following fileds to sign up for an account\n")

    while True:
        try:
            global email
            email = input("Please enter your email address: ")
            einput = emailcheck(email)
            if einput != email:
                raise ValueError(
                    "Please enter a valid email" +
                    f"you entered: {email}"
                )
            else:
                regDetails()
                return email
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")

def regDetails():

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
            new_cust.append(email)
            new_cust.append(name)
            new_cust.append(password)
            new_cust.append(bonus)
            sheet.append_row(new_cust)
            print("WELCOME TO RETRO BANK ! " +
            " As a new customer you will receive £500 joining bonus")
            break



def login():
    """
    This fucntion will allow the exisiting user 
    log into their bank account
    """
    print("This is to login - Exisiting User")
    ename = input("Please enter your email")
    epass = input("Please enter your password")


def welcome():
    """
    This function is the first option the user is given 
    to select if they are a new user or existing user
    """
    while True:
        try:
            choice = input("If you are a new customer please enter 1:\n" +
                           "If you are already are an existing customer please enter 2:\n")
            if choice != "1" and choice != "2":
                raise ValueError(
                    "Enter 1 for new customer or 2 for existing customer," +
                    f"you entered: {choice}"
                )
            else:
                return choice
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


def main():
    """
    Temp function to check all other functions work
    """
    choice = welcome()
    chosen(choice)
    

print("Welcome to RETRO BANK !!")
main()
    