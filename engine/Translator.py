from deep_translator import GoogleTranslator
import pyttsx3

def translate_text(text, source_language, dest_language):
    try:
        # Initialize the Google Translator
        translator = GoogleTranslator(source=source_language, target=dest_language)
        
        # Translate the text
        translated_text = translator.translate(text)
        
        # Set up text-to-speech engine
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
        
        # Ensure the engine has a voice and is ready to speak
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[0].id)  # Change index for different voices
            
        # Speak out the translated text
        engine.say(translated_text)
        engine.runAndWait()
        
        # Return the translated text
        return translated_text
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
