import subprocess
import time
import cv2

from engine.speak import speak

def take_photo(filename='photo.jpg'):
    """Capture a photo using the webcam and save it to a file."""
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise Exception("Could not open webcam")

    # Give the camera a moment to warm up
    cv2.waitKey(1000)

    # Capture a single frame
    ret, frame = cap.read()

    if ret:
        # Save the frame as an image file
        cv2.imwrite(filename, frame)
        print(f"Photo saved as {filename}")
    else:
        print("Failed to capture photo")

    # Release the webcam
    cap.release()
    cv2.destroyAllWindows()

def take_photo1():
    """
    Open the camera app and take a photo using two simulated taps (shutter button included).
    """
    try:
        speak("Opening the camera app.")
        # Step 1: Open the camera app (adjust the coordinates based on your device)
        subprocess.run("adb shell input tap 940 2220", shell=True)  # Coordinates to open the camera app
        time.sleep(1)  # Wait for the camera app to open
        
        speak("Focusing and preparing for the shot.")
        # Step 2: Simulate the first click (for focusing or preparation, optional)
        subprocess.run("adb shell input tap 500 1000", shell=True)  # Focus (optional, adjust coordinates)
        time.sleep(1)
        
        speak("Taking the photo.")
        # Step 3: Simulate the shutter button tap
        subprocess.run("adb shell input tap 546 2005", shell=True)  # Replace with your shutter button coordinates
        time.sleep(1)  # Add a slight delay to ensure the photo is captured
        
        speak("Photo taken successfully.")
        print("Photo taken successfully.")
    except subprocess.CalledProcessError as e:
        speak(f"Failed to take the photo. Error: {e}")
        print(f"Failed to take the photo. Error: {e}")

