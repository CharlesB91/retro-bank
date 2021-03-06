import gspread
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError
from math import ceil
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)

# Inspiration for google sheet API was originally
# taken from love sandwiches project

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


def welcome():
    """
    This function is the first option the user is given
    to select if they are a new user or existing user.
    """

    print("")
    print(Fore.GREEN + "****************************************" +
          "**************************")
    print(Fore.RED + "****************************************" +
          "**************************")
    print("")
    print(Fore.BLACK + Back.YELLOW + Style.BRIGHT +
          "                             WELCOME                              ")
    print(Fore.BLACK + Back.YELLOW + Style.BRIGHT +
          "                               TO                                 ")
    print(Fore.BLACK + Back.YELLOW + Style.BRIGHT +
          "                           RETRO BANK                             ")
    print("")
    print(Fore.MAGENTA + "****************************************" +
          "**************************")
    print(Fore.BLUE + "****************************************" +
          "**************************")
    print("")
    while True:
        try:
            print("")
            print(Fore.GREEN + Style.BRIGHT + "If you are a new customer" +
                  " please enter 1:")
            print(Fore.GREEN + Style.BRIGHT + "If you are already are an" +
                  " existing customer please enter 2:")
            choice = input("\n")
            if choice != "1" and choice != "2":
                raise ValueError(Fore.RED +
                                 "Enter 1 for new customer or 2 for" +
                                 "existing customer," +
                                 f"you entered: {choice}"
                                 )
            else:
                return chosen(choice)
        except ValueError as e:
            print(Fore.RED + f"Invalid data: {e}, please try again.\n")


def chosen(choice):
    """
    Once a valid user selection has been made in the
    welcome function. This will then direct the user to
    the appropriate new or existing user function.
    """

    if choice == "1":
        registerEmail()
    elif choice == "2":
        login()


def registerEmail():
    """
    This function checks the email address is correct,
    while loop will continue until a valid email is input.
    """

    print(Fore.GREEN + "Please complete the following fields to " +
          "sign up for an account:\n")

    while True:
        try:
            global email
            email = input("Please enter your email address:\n")
            email = email.lower()
            einput = emailcheck(email)
            if einput != email:
                raise ValueError(Fore.RED +
                                 "Please enter a valid email" +
                                 f" you entered: {email}"
                                 )
            else:
                regDetails()
                return email
        except ValueError as e:
            print(Fore.RED + f"Invalid data: {e}, please try again.\n")


def emailcheck(emailinput):
    """
    Email validator function.
    Checks the new email is valid.
    This code was taken from (https://pypi.org/project/email-validator/).
    """

    try:
        valid = validate_email(emailinput)
        emailinput = valid.email
        return emailinput
    except EmailNotValidError:
        print(Fore.RED + "The email you provided is not valid " +
              "please try again.")


def regDetails():
    """
    This function checks a valid name has been input,
    User data is then added to the google sheet with new balance.
    Code Taken from Gspread documentation.
    """

    new_cust = []
    bonus = 500
    welcome = float(bonus)

    while True:
        name = input("Please enter your full name:\n")
        nameNoSpace = name.replace(" ", "")
        if nameNoSpace.isalpha():
            break
        else:
            print(Fore.RED + "Name must not contain numbers" +
                  f" or special characters. You entered {nameNoSpace}")

    while True:
        password = input("Please enter your password:\n")
        name = name.lower()
        name = name.title()
        if name == "":
            print(Fore.RED + "Name is required")
        elif password == "" and len(password) < 10:
            print(Fore.RED + "Please enter a password")
        elif len(password) < 8:
            print(Fore.RED + "Please enter a password 8 characters minimum." +
                  "Numbers and special characters are acceptable")
        else:
            try:
                worksheet = gsheet.add_worksheet(title=email,
                                                 rows="100", cols="20")
                new_cust.append(email)
                new_cust.append(name)
                new_cust.append(password)
                new_cust.append(welcome)
                worksheet.append_row(new_cust)
                print("")
                print(Fore.GREEN + "WELCOME TO RETRO BANK !" +
                      " As a new customer you will receive ??500 joining bonus")
                print(Fore.GREEN + "Please now log in:")
                print("")
                login()
            except Exception:
                print(Fore.RED + "Email Already Registered !." +
                      "Please try again")
                registerEmail()
            else:
                login()
                break


def login():
    """
    This function checks the email address is valid in the
    google sheet when customer attempts to log in.
    """

    global ename
    global epass

    while True:
        try:
            ename = input("Please enter your email address:\n")
            ename = ename.lower()
            ename = str(ename)
            gsheet.worksheet(ename)
        except Exception:
            print(Fore.RED + "Invalid Email ! \nPlease try again")
            login()
        else:
            verify()
            break


def verify():
    """
    This function checks the password is correct
    so the customer can log into the account dash board.
    """

    epass = input("Please enter your password:\n")

    global username
    email_ver = SHEET.worksheet(ename)
    username = email_ver.col_values(2)
    password = email_ver.col_values(3)

    for i in password:
        if i == epass:
            mainMenu()
            return
    if i != epass:
        print(Fore.RED + "Incorrect Password !")
        print(Fore.RED + "Please note passwords are case sensitive")
        login()
        return


def mainMenu():
    """
    Once the customer is successfully logged in,
    they will be presented with options:
    1. View Balance
    2. Deposits
    3. Withdraw
    4. How much can i borrow
    5. Logout
    """

    while True:
        try:
            print("")
            print(Fore.GREEN + f"Welcome {username[0]}" +
                  " To Your Retro Account Dashboard")
            print("")
            print("Please Select from the following menu:")
            print("")
            print(Fore.BLACK + Back.GREEN + "1. Account Balance ")
            print(Fore.BLACK + Back.YELLOW + "2. Deposit Money ")
            print(Fore.BLACK + Back.BLUE + "3. Withdrawal ")
            print(Fore.BLACK + Back.GREEN + "4. How Much Can I Borrow ")
            print(Fore.BLACK + Back.RED + "5. Logout ")
            print("")
            choice = input("\n")
            if (choice != "1" and choice != "2" and choice != "3" and
                    choice != "4" and choice != "5"):
                raise ValueError(Fore.RED +
                                 "Enter 1 for Balance, 2 for deposits, 3 for" +
                                 "withdrawals, 4 to logout\n" +
                                 f"you entered: {choice}"
                                 )
            elif choice == "1":
                balance()
            elif choice == "2":
                deposit()
            elif choice == "3":
                withdrawal()
            elif choice == "4":
                mortgageCalc()
            elif choice == "5":
                print("")
                print(Fore.YELLOW + "Thank You For Banking With Us")
                print(Fore.YELLOW + "Have A Nice Day")
                print("")
                welcome()
            else:
                return choice
        except ValueError as e:
            print(Fore.RED + f"Invalid data: {e}, please try again.\n")


def userContinue():
    """
    This function runs a while loop whilst
    checking if the user wants to revert to the main
    menu or log out.
    """

    while True:
        try:
            print("")
            choice = input(Fore.YELLOW + "If you would like to complete " +
                           "an other" +
                           " transactions please 1 for main menu.\n" +
                           "If you would like to log out its 2:\n")
            if choice != "1" and choice != "2":
                raise ValueError(Fore.RED +
                                 "Enter 1 for new customer or 2 for" +
                                 "selection" +
                                 f"you entered: {choice}"
                                 )
            elif choice == "1":
                mainMenu()
            else:
                print("")
                print(Fore.YELLOW + "Thank You For Banking With Us")
                print(Fore.YELLOW + "Have A Nice Day")
                print("")
                welcome()
        except ValueError as e:
            print(Fore.RED + f"Invalid data: {e}, please try again.\n")


def balance():
    """
    This function allows the user to view
    their real time balance from the google sheet.
    """

    user = SHEET.worksheet(ename)
    balance = user.col_values(4)
    value = balance[0]
    print("")
    print(Fore.GREEN + f"The balance of your account is ??{value}")
    userContinue()


def deposit():
    """
    This function allows the user to deposit money.
    Once they have completed this transaction they???re
    new balance will display.
    """

    user = SHEET.worksheet(ename)
    balance = user.col_values(4)
    value = balance[0]
    value = float(value)

    while True:
        try:
            print("")
            choice = input("How much would you like to deposit ? \n")
            choice = choice.replace(',', '')
            choice = float(choice)
            if choice != float(choice):
                raise ValueError(Fore.RED +
                                 "Please enter a valid amount" +
                                 f"you entered: {choice}"
                                 )
            else:
                new = value + choice
                new = ceil(new * 100) / 100.0
                user.update("D1", new)
                print("")
                print(Fore.GREEN + "The balance of your account" +
                      f"is now ??{new}")
                userContinue()
                break
        except ValueError as e:
            print(Fore.RED + f"Invalid data: {e}, please try again.\n")


def withdrawal():
    """
    This function allows the user to withdraw money.
    This will check if they have sufficient funds to do so.
    """

    user = SHEET.worksheet(ename)
    balance = user.col_values(4)
    value = balance[0]
    value = float(value)

    while True:
        try:
            print("")
            choice = input("How much would you like to withdraw ?\n")
            choice = choice.replace(',', '')
            choice = float(choice)
            if choice != float(choice):
                raise ValueError(Fore.RED +
                                 "Please enter a valid amount" +
                                 f"you entered: {choice}"
                                 )
            else:
                if value >= choice:
                    new = value - choice
                    new = ceil(new * 100) / 100.0
                    user.update("D1", new)
                    print("")
                    print(Fore.GREEN + "The balance of your account" +
                          f"is now ??{new}")
                    userContinue()
                    break
                else:
                    print("")
                    print(Fore.RED + "You have insufficient funds")
                    print(Fore.GREEN + "The Balance of your account" +
                          f"is ??{value} \n")
                    userContinue()
                    break
        except ValueError as e:
            print(Fore.RED + f"Invalid data: {e}, please try again.\n")


def mortgageCalc():
    """
    This function gives the user
    an idea of how much they could
    borrow if they were looking to
    take a mortgage based on their
    income & outgoings.
    """

    while True:
        try:
            print("")
            choice = input("How much is your annual salary?\n")
            choice = choice.replace(',', '')
            choice = float(choice)
            if choice <= 10000:
                print("")
                print(Fore.RED + "You are not eligible for a mortgage based" +
                      " on your salary\n")
                userContinue()
                break
            else:
                outgoing = input("What is your monthly contractual" +
                                 " outgoings?\n")
                outgoing = outgoing.replace(',', '')
                outgoing = float(outgoing)
                if choice != float(choice) and outgoing != float(outgoing):
                    raise ValueError(Fore.RED +
                                     "Please enter a valid amount" +
                                     f"you entered: {choice}"
                                     )
                else:
                    totalOut = outgoing * 12
                    total = choice - totalOut
                    total = round(total * 4.75)
                    total = ceil(total * 100) / 100.0
                    if total <= 20000:
                        print("")
                        print(Fore.RED + "You are not eligible for a " +
                              "mortgage based on your income & outgoings\n")
                        userContinue()
                        break
                    else:
                        print("")
                        print(Fore.GREEN + "The indicitive amount you could" +
                              f" borrow is ??{total}\n")
                        userContinue()
                        break
        except ValueError as e:
            print(Fore.RED + f"Invalid data: {e}, please try again.\n")


welcome()
