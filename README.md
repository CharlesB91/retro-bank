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

## Data Model - Function Digagram

Originally i sketched how i wanted the flow of my application to follow to get an idea of what functionality was required. I then moved this idea to diagram flowchart maker. 

![Flow-Chart](https://github.com/CharlesB91/retro-bank/blob/main/assets/images/flow_retro_bank-Page-2.drawio.png)

- For my data model i deciced to use the google sheets API to store the customer data and balance info. 
- I created functions to register the customers details and to verify the customers data when logging in. 
- I then created fucntions to display the main menu which would then route the customer to the various transctions functions - balance, disposit, withdrawl, how much can i borrow. Then eventually the customer is able to log out of the application and is returned to the welcome screen. 

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

### Additiona Features

- Additioanl features include coloured & highlighted text in the CLI which is to make certain information stand out for the user.
- The moudle used to do this is colorama.

