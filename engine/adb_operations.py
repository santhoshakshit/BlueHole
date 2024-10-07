import csv
from os import name
import subprocess
import time

from engine.features import speak

def load_contacts(file_path):
    """
    Load contacts from the CSV file and return them as a dictionary.
    The keys will be the contact names, and the values will be the phone numbers.
    """
    contacts = {}
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Name'].strip().lower()  # Normalize contact name to lowercase
                phone_number = row['Phone Number'].strip()
                contacts[name] = phone_number
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except Exception as e:
        print(f"Error loading contacts: {e}")
    
    return contacts

def find_contact_by_name(name, contacts):
    """
    Find the phone number of a contact by their name.
    The name will be matched in lowercase for consistency.
    """
    name = name.lower().strip()  # Normalize input for matching
    return contacts.get(name, None)

def make_call(contact_number, contact_name):
    """
    Make a phone call using ADB to the specified contact number and speak the contact name.
    """
    try:
        # ADB command to initiate a call
        adb_command = f"adb shell am start -a android.intent.action.CALL -d tel:{contact_number}"
        subprocess.run(adb_command, shell=True, check=True)
        print(f"Calling {contact_number} via ADB...")
        speak(f"Calling {contact_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to make a call to {contact_number}. Error: {e}")
        speak(f"Failed to make a call to {contact_name}. Please try again.")


def sendMessage(message, mobileNo, name):
    from engine.helper import replace_spaces_with_percent_s, goback, keyEvent, tapEvents, adbInput
    message = replace_spaces_with_percent_s(message)
    mobileNo = replace_spaces_with_percent_s(mobileNo)
    speak("sending message")
    goback(4)
    time.sleep(1)
    keyEvent(3)
    # open sms app
    tapEvents(145, 1810)
    #start chat
    tapEvents(946, 2228)
    # search mobile no
    adbInput(mobileNo)
    #tap on name
    tapEvents(544, 732)
    # tap on input
    tapEvents(390, 2270)
    #message
    adbInput(message)
    #send
    tapEvents(957, 1397)
    speak("message send successfully to "+name)    

