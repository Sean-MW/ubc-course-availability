# UBC Waitlist
A Python bot that scrapes the UBC site for course availability and sends SMS alerts when spots in desired courses open up.

## Install / Setup

### Clone the Repo
```
git clone https://github.com/Sean-MW/ubc-waitlist.git
```
### Create and Activate a Python Virtual Environment
```
cd ubc-waitlist
python -m venv venv
source venv/bin/activate
```
### Install Dependencies
```
pip install -e .
```
### Set Up Environment Variables
Create file for environment variables.
```
touch .env
```
Enter the following information in the env file:
- PHONE_NUM_EMAIL: Your mobile carrier email for your phone number. My carrier is Freedom Mobile, so for me this field looks like: (my-phone-number)@txt.freedommobile.ca. [Here](https://avtech.com/articles/138/list-of-email-to-sms-addresses/) is a list of some email-to-sms addresses from various carriers.
- GMAIL_ADDRESS: The gmail address that will send you the text alerts.
- GMAIL_APP_PASSWORD: Create a (free) gmail app by following [these](https://support.google.com/accounts/answer/185833) instructions and use that app password in this field.
```
PHONE_NUM_EMAIL=yourphonenumber@yourcarrieremail.com
GMAIL_ADDRESS=youremail@gmail.com
GMAIL_APP_PASSWORD=putyourapppasswordhere
```

## Getting Started

### Running the Bot
Start the bot by calling main.
```
python src/ubc_waitlist/main.py
```
A menu will pop up with the options to add and remove course alerts, view current alerts, and search for course availability.

