from asyncio import Task
from pipes import quote
import subprocess
import time
import pyautogui
import pyttsx3
import speech_recognition as sr
import eel
import webbrowser
import wolframalpha
from engine.camera import take_photo, take_photo1
from engine.features import openCommand, PlayYoutube, get_current_time_and_date
from engine.Translator import translate_text
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from engine.api import get_joke, get_weather, get_news
from engine.ocr_module import perform_ocr
from engine.search import get_wikipedia_info, open_or_search_from_command 

# Setup Spotify credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="your_cliend_id",
                                               client_secret="your_client_secret",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-modify-playback-state,user-read-playback-state"))

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Function to speak the given text."""
    text = str(text)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()
    time.sleep(1)
    eel.receiverText(text)

def takecommand():
    """Listen to user input and return the recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1.2
        r.adjust_for_ambient_noise(source, duration=1)

        audio = r.listen(source, timeout=10, phrase_time_limit=8)

    try:
        print('Recognizing...')
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        return query.lower()

    except Exception as e:
        print("Error:", e)
        return ""

def playSpotifySong(song_name):
    """Play a song on Spotify by opening it in the web browser."""
    try:
        results = sp.search(q=song_name, type='track', limit=1)
        if results['tracks']['items']:
            track_url = results['tracks']['items'][0]['external_urls']['spotify']
            webbrowser.open(track_url)
            speak(f"Opening {song_name} on Spotify.")
        else:
            speak(f"Sorry, I couldn't find the song {song_name} on Spotify.")
    except Exception as e:
        speak(f"An error occurred: {str(e)}")

@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)    

    if "open" in query:
        openCommand(query)
    elif "on youtube" in query:
        PlayYoutube(query)
    elif "play" in query and "on spotify" in query:                                     
        
        song_name = query.replace("play", "").replace("on spotify", "").strip()
        playSpotifySong(song_name)
    elif "send message" in query or "phone call" in query or "video call" in query:
        from engine.features import findContact
        from engine.adb_operations import make_call,sendMessage
        contact_no, name = findContact(query)
        if contact_no != 0:
            speak("Which mode would you like to use, WhatsApp or mobile")
            preference = takecommand()
            print(preference)
            from engine.features import whatsApp
            if "mobile" in preference.lower():
            # If mobile is chosen
                if "send message" in query or "send sms" in query: 
                        speak("what message to send")
                        message = takecommand()
                        sendMessage(message, contact_no, name)
                elif "phone call" in query:
                    make_call(contact_no,name)  # Use ADB to make the call
                else:
                    speak("Sorry, I didn't understand. Please try again.")
        
            elif "whatsapp" in preference.lower():
                message = ""
                if "send message" in query:
                    message = 'message'
                    speak("What message would you like to send?")
                    query = takecommand()
                elif "phone call" in query:
                    message = 'call'
                elif "video call" in query:
                    message = 'video call'
                else:
                    speak("Sorry, I didn't understand. Please try again.")
            
                whatsApp(contact_no, query, message, name)  # WhatsApp function

        else:
            speak("Please try again.")


    elif "translate" in query:
        query = query.replace("translate", "").strip()
        speak("Which language would you like to translate to?")
        dest_language = takecommand().strip()
        print(f"Destination language: {dest_language}")
        print(f"Query: {query}")
        source_language = 'auto'
        translated_text = translate_text(query, source_language, dest_language)
        print(f"Translated text: {translated_text}")
        speak(f"Translation to {dest_language}: {translated_text}")

    elif "weather" in query:
        city = query.split("in")[-1].strip()
        api_key = 'your_weatherstack_api'
        weather_report = get_weather(city, api_key)
        speak(weather_report)

    elif "news" in query:
        topic = query.split("about")[-1].strip() if "about" in query else 'latest'
        api_key = 'your_Gnews_api'
        news_report = get_news(api_key, topic)
        speak(news_report)
    elif "joke" in query:
        joke = get_joke()
        speak(joke)
    elif "click a photo" in query:
        speak("Which device would you like to use, mobile or desktop?")
        preference = takecommand().lower()

        if "mobile" in preference:
            take_photo1()  # Call the function for mobile
        elif "desktop" in preference:
            take_photo()  # Call the function for desktop
        else:
            speak("Sorry, I didn't understand. Please try again.")

    elif 'tell me about' in query:
        search_query = query.replace('tell me about', '').strip()
        if search_query:
            wiki_info = get_wikipedia_info(search_query)  # Call your Wikipedia function
            speak(wiki_info)
            print(wiki_info)
        else:
            speak("Please specify a topic to search for on Wikipedia.")

    elif 'time' in query or 'date' in query:
        response = get_current_time_and_date()
        speak(response) 
    elif "browse" in query:
        open_or_search_from_command(query)
    elif 'search for' in query:
        open_or_search_from_command(query)
    elif "read the text" in query or "perform ocr" in query:
        speak("Starting OCR...")
        detected_text = perform_ocr()  # Call the OCR function
        if detected_text:
            speak(f"Detected text: {detected_text}")
        else:
            speak("No text detected in the image.")       
    
    else:
        speak("Command not recognized")

    eel.ShowHood()

