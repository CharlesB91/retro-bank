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

## Function Diagram

Originally i sketched how i wanted the flow of my application to follow to get an idea of what functionality was required. I then moved this idea to diagram flowchart maker. 

![Flow-Chart](https://github.com/CharlesB91/retro-bank/blob/main/assets/images/flow_retro_bank-Page-2.drawio.png)

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
- 1. View Balance
- 2. Deposit
- 3. Withdraw
- 4. How much can I borrow
- 5. Log out

- The user needs to enter the number of which transaction they would like to complete and they will be routed accordingly. 

### View Balance

### Deposit

### Withdraw

### Mortgage Calculator - How much can i borrow

### Log out



