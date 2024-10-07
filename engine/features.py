from pipes import quote
import re
import sqlite3
import subprocess
import time
import webbrowser
from playsound import playsound
import eel
import pyautogui
import os
from engine.speak import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
from hugchat import hugchat
from engine.helper import remove_words
from engine.search import open_application

conn=sqlite3.connect("chitti.db")
cursor = conn.cursor()


import datetime
def get_current_time_and_date():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")  # Format: YYYY-MM-DD
    time = now.strftime("%H:%M:%S")  # Format: HH:MM:SS
    return f"Today's date is {date} and the current time is {time}."

# playing assistant sound
@eel.expose
def playAssistantSound():
    music_dir ="www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    """Extract application name from the query and open it."""
    app_name = query.replace('open', '').strip()  # Extract the app name from the command
    response = open_application(app_name)  # Call the function to open the app
    speak(f"opening {app_name}")  # Speak the response message
                  

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    
    if search_term:
        speak(f"Playing {search_term} on YouTube")
        # Construct YouTube search URL
        search_url = f"https://www.youtube.com/results?search_query={search_term.replace(' ', '+')}"
        # Open the YouTube search results in the default web browser
        webbrowser.open(search_url)
    else:
        speak("Sorry, I couldn't understand the search term.")

def extract_yt_term(command):
    # Define a regular expression pattern to capture the search term
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None

def findContact(query):
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0
    
def whatsApp(mobile_no, message, flag, name):
    if flag == 'message':
        target_tab = 12
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        jarvis_message = "staring video call with "+name


    # Encode the message for URL
    encoded_message = quote(message)
    print(encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(jarvis_message)