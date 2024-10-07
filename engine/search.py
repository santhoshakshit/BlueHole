from multiprocessing.connection import Client
import wikipedia

from engine.speak import speak

def get_wikipedia_info(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return "Your query is too ambiguous, please be more specific."
    except wikipedia.exceptions.PageError:
        return "No matching results found."
    except Exception as e:
        return f"An error occurred: {e}"


import webbrowser
import re

def open_or_search_from_command(command):
    """
    Opens a website or performs a search based on the command.

    Args:
    command (str): The command string containing the URL/domain or search query.
    """
    # Check if the command includes a search query
    search_match = re.search(r'search for (.+)', command)
    if search_match:
        query = search_match.group(1)
        # Perform a search on Google
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
        print(f"Searching for {query}")  # You can replace this with `speak()` if needed
        speak(f"Searching for {query}")
    else:
        # Extract the URL or domain from the command
        url_match = re.search(r'browse (https?://[^\s]+|[^\s]+)', command)
        if url_match:
            url = url_match.group(1)
            # Ensure the URL is properly formatted
            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url
            webbrowser.open(url)
            print(f"Opening {url}")  # You can replace this with `speak()` if needed
            speak(f"Opening {url}")
        else:
            print("Please specify a valid website or search query.")  # You can replace this with `speak()` if needed


import subprocess

def open_application(app_name):
    """
    Open the system application based on the app_name provided.
    """
    # Map common app names to system executable names
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "wordpad": "write.exe",
        "paint": "mspaint.exe",
        "file explorer": "explorer.exe",
        "command prompt": "cmd.exe",
        "control panel": "control.exe",
        "task manager": "taskmgr.exe",
        "powershell": "powershell.exe",
        "settings": "ms-settings:"
    }

    # Check if the app_name is in the dictionary
    app_exec = apps.get(app_name.lower())
    
    if app_exec:
        try:
            subprocess.run(app_exec, shell=True)
            print(f"{app_name} opened successfully.")
        except Exception as e:
            print(f"Failed to open {app_name}. Error: {e}")
    else:
        print(f"Application {app_name} not found.")
