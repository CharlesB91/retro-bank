# Retro Bank

This retro banking application allows new & existing users to sign up for a retro account where they will receive a £500 joining bonus. This application has features such as check balance, deposit money, withdraw money and a mortgage calculate which will indicate how much a user can borrow based on their income and outgoings. This application has been set up with a google sheet API therefore all customer data & balance info is stored on a google sheet waiting to be accessed by the authenticated user.

## Aim

The aim of this application to provide a simple banking application to any new and existing user to complete basic banking transactions. This ultimelty demonstrates the use of remote database using google sheets API. The data can be requested, read, updated and saved as per the users request. 

### Business Goals

- To collect user data and store this on a remove data base (google sheets).
- Allow a user to create a new retro account and allow existing users to log into their retro account. 
- A user can complete some basic transactions i.e. view balance, deposit, withdraw and mortgage calculator.

### Client Goals

- To provide some basic banking facilities to the user whilst maintaining the data integrity. 

## Data Model - Function Diagram

Originally I sketched how I wanted the flow of my application to follow to get an idea of what functionality was required. I then moved this idea to diagram flowchart maker. 

![Flow-Chart](https://github.com/CharlesB91/retro-bank/blob/main/assets/images/flow_retro_bank-Page-2.drawio.png)

- For my data model I decided to use the google sheets API to store the customer data and balance info. 
- I created functions to register the customers details and to verify the customers data when logging in. 
- I then created functions to display the main menu which would then route the customer to the various transactions functions - balance, deposit, withdrawal, how much can i borrow. Then eventually the customer is able to log out of the application and is returned to the welcome screen. 

## Features

### Welcome 

- This area features a graphical message of retro bank.
- This area is where the user can enter 1 to register as a new user or 2 for existing user log in.

### New User Registration

- This area is where the user can enter their email, address, name & password.
- The email address entered will check the email has not been already registered.
- Once successfully registered the customers details will be saved onto a new worksheet on a google sheet with their new balance of £500

### Existing User Log In

- This area is where the customer enters their email address & password.
- The details entered is checked against the google sheets to ensure the authenticity of the user. 
- Once successfully logged in the user will be presented with the main menu.

### Main Menu

- This area where what the customer will see once they are successfully logged in.
- The menu has 5 options
- 1 View Balance
- 2 Deposit
- 3 Withdraw
- 4 How much can I borrow
- 5 Log out

- The user needs to enter the number of which transaction they would like to complete and they will be routed accordingly. 

### View Balance

- This area displays the customer live balance which is fetched from the google sheet. 
- The customer will be presented with a message if they would like to go back to the main menu or log out. 

### Deposit

- This area is where the user can enter in how much they would like to deposit. 
- Once this is completed the user will see the new balance. This new balance is updated on the google sheet. 
- The customer will be presented with a message if they would like to go back to the main menu or log out. 

### Withdraw

- This area allows the user to withdraw money at their request.
- The user will enter in how much they would like to withdraw. The application will then check with the google sheet that the customer has sufficient funds.
- If the customer has sufficient funds they will be presented with their new balance and again this new balance saved back to the google sheet. 
- If the customer does not have sufficient funds they will be presented with an insufficient funds message with their live balance from the google sheet. 
- The customer will be presented with a message if they would like to go back to the main menu or log out. 

### Mortgage Calculator - How much can i borrow

- This area features a simple mortgage calculation which is inform the user how much they can borrow.
- The user needs to enter their annual salary along with their monthly contractual commitments.
- The user will then be information how much in principle they can borrow. 
- If the amount us under 10K they will be displayed a message that they do not qualify for a mortgage.
- The customer will be presented with a message if they would like to go back to the main menu or log out. 

### Log out

- This area allows the user to log out with a corresponding message. 
- The user will then be routed back to the welcome screen.

### Additional Features

- Additional features include coloured & highlighted text in the CLI which is to make certain information stand out for the user.
- The module used to do this is colorama.

## Testing

- I have manually tested by doing the following:
    - Ran my python code through pep8linter via gid pod with no significant issues.
    - Have input incorrect values to input areas to ensure error functions are working correctly. 
    - Testing code via terminal & heroku terminal

### Validator Testing

- Code has been passed through (http://pep8online.com/) with no significant issues after corrections

## Bugs

### Resolved Bugs

- Initially when a user was trying to sign in could not access appropriate cell data as there would be multiple customers eventually registering so could not implements a specific cell to search as customer data was on the one worksheet. After chatting with mentor she advised to look at my data structure with google sheets. After this i decided to use the method of when a new user is registered google sheets would create a new worksheet for this user. This was i could access the customer email address, name, password, balance data as the cells would not be changing only the specific worksheet for who ever was trying to log in. The gspread documentation helped me figure this out which was very helpful. (https://docs.gspread.org/en/latest/user-guide.html).
- As part of testing realised that all email address should be converted to lower case to ensure when a customer attempts to log back in this be always converted into the correct format from what google sheets has. Using the .lower() method has resolved this issue. 
- Again whilst testing because we are dealing with money values the user could input commas and decimal points which i had not accounted for. After some research implement replace(',', '') method to remove the commas and the method float() if the users a decimal point. The application can now handle values with commas and calculate using decimals. Stack overflow provided the solution to remove the commas (https://stackoverflow.com/questions/16233593/how-to-strip-comma-in-python-string).
- When a customer registers their email i had not implemented anything to check that the email had already been registered. Additionally did not account for when a user logs in with an unknown email. After some thought realised all i had to do was catch this in an try block to stop the application from crashing.

### Unresolved Bugs

- No current unresolved bugs I have come across so far after testing. 

## Deployment

- This project was deployed using code institute's mock Terminal for Heroku.
- Deployment Steps:
  - Fork or clone this repository.
  - Create new Heroku app.
  - Set a built back to Python and nodeJs (in this exact order).
  - Link the Heroku app to the repository.
  - Finally click on Deploy.

## Credits

- The original inspiration was taken from YouTube tutorial. Although the app features in this tutorial is deployed completely differently and also how the data is stored. This allowed me to understand the logic and functionality. (https://www.youtube.com/watch?v=71X58zIzrgA&list=RDCMUCfgSHpMOBXqmtqufxgVp68g&index=3)
- The gspread documentation provided amazing guidance for manipulating data in the google sheet. (https://docs.gspread.org/en/latest/user-guide.html)
- After some googling came across a specific email validator for when a user registers for the first time (https://pypi.org/project/email-validator/)
- The coloured text and highlighted text effect was taken from YouTube tutorial (https://www.youtube.com/watch?v=u51Zjlnui4Y)
