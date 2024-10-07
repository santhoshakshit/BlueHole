# ocr_module.py
import webbrowser
import cv2
import requests
import io
import json
import pyttsx3
import speech_recognition as sr
import eel

from engine import speak

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak_text(text):
    """
    Uses text-to-speech to speak out the provided text.
    :param text: The text to be spoken
    """
    engine.say(text)
    engine.runAndWait()

def take_voice_command():
    """
    Listens for voice commands and returns the recognized text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for capture command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"User said: {command}")
        return command
    except sr.UnknownValueError:
        return ""

def perform_ocr():
    """
    Captures an image using the webcam upon voice command "capture",
    performs OCR on it, and sends the detected text to the hood.
    """
    # Open the camera window in the foreground
    webcam = cv2.VideoCapture(0)
    print("Camera is open. Say 'capture' to take a photo or 'exit' to quit.")
    speak_text("Camera is open. Say 'capture' to take a photo or 'exit' to quit.")

    while True:
        check, frame = webcam.read()
        cv2.imshow("Camera", frame)

        # Listen for the voice command
        command = take_voice_command()

        if "capture" in command:
            img_file = 'captured_image.jpg'
            cv2.imwrite(filename=img_file, img=frame)
            webcam.release()
            cv2.destroyAllWindows()
            print(f"Image captured and saved as {img_file}!")
            speak_text("Image captured successfully.")
            break
        elif "exit" in command:
            webcam.release()
            cv2.destroyAllWindows()
            print("Camera closed by user command.")
            speak_text("Camera closed.")
            return None

    # Perform OCR on the captured image
    url_api = "https://api.ocr.space/parse/image"
    api_key = "K81811960988957"  # Replace with your OCR.Space API key

    img = cv2.imread(img_file)
    _, compressed_image = cv2.imencode(".jpg", img, [1, 90])
    file_bytes = io.BytesIO(compressed_image)

    result = requests.post(url_api,
                           files={img_file: file_bytes},
                           data={"apikey": api_key, "language": "eng"})

    # Parse the result
    result = result.content.decode()
    result = json.loads(result)

    try:
        parsed_results = result.get("ParsedResults")[0]
        text_detected = parsed_results.get("ParsedText")
        eel.DisplayMessage(text_detected)  # Send detected text to hood
        return text_detected
    except:
        eel.DisplayMessage("Sorry, no text was detected.")  # Send error message to hood
        return "Sorry, no text was detected."