# Retro Bank

This retro banking application allows new & existing users to sign up for a retro account where they will receive a £500 joining bonus. This application has features such as check balance, deposit money, withdraw money and a mortgage calculator which will indicate how much a user can borrow based on their income and outgoings. This application has been set up with a google sheet API therefore all customer data & balance info is stored on a google sheet waiting to be accessed by the authenticated user.

! [Welcome](https://github.com/CharlesB91/retro-bank/blob/main/assets/images/welcome1.PNG)

- Deployed Site(https://retro-bank21.herokuapp.com/)

## Aim

The aim of this application to provide a banking application to any new and existing user to complete some basic banking transactions. This ultimately demonstrates the use of python code and a remote database using google sheets API. The data can be requested, read, updated and saved as per the users request. 

### Business Goals

- To collect user data and store this on a remote database.
- Allow a user to create a new retro account and allow existing users to log into their retro account. 
- Allow a user to complete some basic transactions i.e., view balance, deposit, withdraw and mortgage calculator.

### Client Goals

- To provide some useful banking facilities to the user whilst maintaining data integrity. 

## Data Model - Function Diagram

Originally, I sketched how I wanted the flow of my application to follow to get an idea of what functionality was required. I then moved this idea to diagram flowchart. 

! [Flow-Chart] (https://github.com/CharlesB91/retro-bank/blob/main/assets/images/flow_retro_bank-Page-2.drawio.png)

- For my data model I decided to use the google sheets API to store the customer data and balance info. 
- I created functions to register the customers details and to verify the customers data when logging in. 
- I then created functions to display the main menu which would then route the customer to the various transaction’s functions - balance, deposit, withdrawal, how much can I borrow. Eventually then the customer is able to log out of the application and is returned to the welcome screen. 

## Features

### Welcome 

- This area features a graphical message of retro bank.
- This area is where the user can enter 1 to register as a new user or 2 for existing user log in.

! [Welcome](https://github.com/CharlesB91/retro-bank/blob/main/assets/images/welcome1.PNG)

### New User Registration

- This area is where the user can enter their email address, full name & password.
- The application will first check the email address entered is not already registered.
- Once successfully registered the customers details will be saved onto a new worksheet on the google sheet with their new balance of £500

! [New-User] (https://github.com/CharlesB91/retro-bank/blob/main/assets/images/register.PNG)

### Existing User Log In

- This area is where the user enters their email address & password.
- The details entered is checked against the google sheets to ensure the authenticity of the user. 
- Once successfully logged in the user will be presented with the main menu.

! [Login](https://github.com/CharlesB91/retro-bank/blob/main/assets/images/login.PNG)

### Main Menu

- This area is where the user is routed to once successfully logged in. 
- The menu has 5 options:
    - 1 View Balance
    - 2 Deposit
    - 3 Withdraw
    - 4 How much can I borrow
    - 5 Log out

- The user needs to enter the corresponding menu number of which transaction they would like to complete and they will be routed accordingly. 

! [Main-Menu] (https://github.com/CharlesB91/retro-bank/blob/main/assets/images/menu.PNG)

### View Balance

- This area displays the customers live balance which is fetched from the google sheet. 
- The customer will be presented with a message if they would like to revert to the main menu or log out. 

! [Balance](https://github.com/CharlesB91/retro-bank/blob/main/assets/images/balance.PNG)

### Deposit

- This area is where the user can enter in how much they would like to deposit. 
- Once this is completed the user will see the new balance. This new balance is updated on the google sheet. 
- The customer will be presented with a message if they would like to revert to the main menu or log out. 

! [Deposit](https://github.com/CharlesB91/retro-bank/blob/main/assets/images/deposit.PNG)

### Withdraw

- This area allows the user to withdraw money at their request.
- The user will enter in how much they would like to withdraw. The application will then check with the google sheet that the customer has sufficient funds.
- If the customer has sufficient funds they will be presented with their new balance and again this new balance saved back to the google sheet. 
- If the customer does not have sufficient funds, they will be presented with an insufficient funds message with their live balance from the google sheet. 
- The customer will be presented with a message if they would like to revert to the main menu or log out. 

! [Withdraw](https://github.com/CharlesB91/retro-bank/blob/main/assets/images/withdraw.PNG)
! [Insufficent-Funds] (https://github.com/CharlesB91/retro-bank/blob/main/assets/images/insufficent.PNG)

### Mortgage Calculator - How much can I borrow

- This area features a simple mortgage calculation which will inform the user how much they can borrow.
- The user needs to enter their annual salary along with their monthly contractual commitments.
- The user will then be information how much in principle they can borrow. 
- If the amount offered is under 20K they will be presented with a message that they do not qualify for a mortgage.
- Additionally, if the customers annual salary is 10K or below they will be presented with a message that they do not qualify for a mortgage.
- The customer will be presented with a message if they would like to revert to the main menu or log out. 

! [Insufficent-Funds] (https://github.com/CharlesB91/retro-bank/blob/main/assets/images/mortgage.PNG)

### Log out

- This area allows the user to log out with a corresponding message. 
- The user will then be routed back to the welcome screen.

! [Logout](https://github.com/CharlesB91/retro-bank/blob/main/assets/images/logout.PNG)

### Additional Features

- Additional features included are coloured & highlighted text in the Command line which is to make certain information stand out for the user.
- The module used to do this is colorama.

## Testing

- I have manually tested by doing the following:
    - Ran my python code through pep8linter via git pod with no significant issues.
    - Have input incorrect values to input areas to ensure error functions are working correctly. 
    - Testing code via terminal & heroku terminal.

### Validator Testing

- Code has been passed through (http://pep8online.com/) with no significant issues after corrections.

## Bugs

### Resolved Bugs

- Initially when a user was trying to sign in the code could not access appropriate cell data as there would be multiple customers eventually registering so could not implements a specific cell to search as customer data was on the one worksheet. After chatting with mentor, she advised to look at my data structure within google sheets. After some thought I decided to change the method in which new users are registered against the google sheet. Instead of having all customer data in one worksheet I implemented a method that would register a new worksheet for any new user with their email address as the name of the worksheet. By doing this was I could then access the customer email address, name, password, balance data as the cells would not be changing only the specific worksheet for whoever was trying to log in. The gspread documentation helped me figure this out which was very helpful. (https://docs.gspread.org/en/latest/user-guide.html).
- As part of testing realised that all email address should be converted to lower case to ensure when a customer attempts to log back in this be always converted into the correct format from what google sheets has. Using the .lower() method has resolved this issue. 
- Again, whilst testing, as we are dealing with monetary values the user could input commas and decimal points which I had not accounted for. After some research I implemented the replace(',', '') method to remove the commas and the method float() if the user inputs a decimal point. The application can now handle values with commas and calculate using decimals. Stack overflow provided the solution to remove the commas (https://stackoverflow.com/questions/16233593/how-to-strip-comma-in-python-string).
- When a customer registers their email, I had not implemented anything to check that the email had already been registered. Additionally, I did not account for when a user logs in with an invalid email address. After some thought realised all, I had to do was catch this in a try block to stop the application from crashing.
- When completing certain transactions, the output would have large decimal remainders. Researched and found a solution to round up to the next decimal (https://stackoverflow.com/questions/9232256/round-up-to-second-decimal-place-in-python)

### Unresolved Bugs

- No current unresolved bugs I have come across so far after testing.


## Future Features

- For the registration area I would implement a password validator which would check that the password meets a certain criteria i.e., 8 characters long with number and special character. 
- Again, for the registration section where the user inputs their name. I would implement a name checker which validates the customer has entered a valid name. Right now, the user could enter any character and this would be added to the google sheet as their name. 
- Lastly when the user registers, I would implement a savings goal. This would be displayed every time the user checks their balance or deposits

## Deployment

- This project was deployed using code institute's mock Terminal for Heroku.
- Deployment Steps:
  - Fork or clone this repository.
  - Create new Heroku app.
  - Set a built back to Python and nodeJs (in this exact order).
  - Link the Heroku app to the repository.
  - Finally click on Deploy.

## Credits

- The original inspiration was taken from YouTube tutorial. Although the app featured in this tutorial is deployed completely differently with a different data model. This allowed me to understand the logic and functionality I needed to build this application. (https://www.youtube.com/watch?v=71X58zIzrgA&list=RDCMUCfgSHpMOBXqmtqufxgVp68g&index=3)
- The gspread documentation provided amazing guidance for manipulating data in the google sheet. (https://docs.gspread.org/en/latest/user-guide.html)
- After some googling came across a specific email validator for when a user registers for the first time (https://pypi.org/project/email-validator/)
- The coloured text and highlighted text effect were taken from YouTube tutorial (https://www.youtube.com/watch?v=u51Zjlnui4Y)
