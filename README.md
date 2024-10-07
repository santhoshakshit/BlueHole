---

# Bluehole - Voice Assistant 🌀

Welcome to **Bluehole**, your personal voice assistant! This assistant leverages various APIs and powerful tools to bring you a smooth, hands-free experience that integrates seamlessly with your system and mobile devices.

## Project Overview 🚀

Bluehole is an interactive voice assistant built using Python, Flask, and various APIs. It allows users to perform a variety of tasks like searching for information, controlling apps, interacting with devices, and much more—all through voice commands.

### APIs Used 🔗
- [Weatherstack](https://weatherstack.com/) – For live weather updates 🌦️
- [GNews](https://gnews.io/) – For fetching the latest news 📰
- [JokeAPI](https://jokeapi.dev/) – To lighten up the mood with some jokes 😂

## Features 🌟
- 🎙️ **Voice Commands:** Interact using voice commands to execute tasks effortlessly.
- 🔄 **Task Automation:** Automates day-to-day tasks on your desktop or mobile.
- 🌐 **Web Integration:** Uses APIs for weather, news, jokes, etc.
- 📷 **Device Control:** Supports camera, calling, and multimedia commands.
- 💬 **Multilingual Support:** Translates commands into multiple languages for global accessibility.
  
## Tasks 🎯
- 🗂️ **Opens System Applications**
- 📺 **Opens and Searches on YouTube**
- 🎵 **Plays Songs on Spotify**
- 💬 **Sends Messages on WhatsApp or Mobile**
- 📞 **Makes Phone Calls on WhatsApp or Mobile**
- 📹 **Video Calls on WhatsApp**
- 🌐 **Translates Commands to Desired Languages**
- 🌦️ **Provides Weather Updates**
- 📰 **Shares News Updates**
- 😂 **Tells Jokes**
- 📸 **Takes Photos on Desktop or Mobile**
- 📖 **Searches on Wikipedia**
- 🕰️ **Tells Time and Date**
- 🌍 **Opens Websites**
- 🔍 **Searches on Google**
- 📝 **Reads Text from Camera (OCR)**

## Setup Instructions 🛠️

1. Clone the repository:
   ```bash
   git clone https://github.com/santhoshakshit/BlueHole
   ```
2. Install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```
3. **Download and set up ADB**:
   - Download ADB from the official [Android Developer Tools](https://developer.android.com/studio/releases/platform-tools).
   - Extract the platform tools to a folder (e.g., `C:\adb\platform-tools`).
   - Add the folder to your system’s **Path** environment variable to easily use ADB commands from anywhere.
4. Run the `device.bat` to set up ADB for mobile integration:
   ```bash
   device.bat
   ```
   change the ip address according to your network
5. Start the Flask server:
   ```bash
   python app.py
   ```
6. Access the application in your browser at `http://localhost:8000`.

## Technologies Used 🖥️
- **Backend:** Flask, Python, SQLite
- **Frontend:** HTML, CSS, JavaScript, Eel
- **Voice Processing:** Google Text-to-Speech, SpeechRecognition
- **APIs:** Weatherstack, GNews, JokeAPI
- **Mobile Integration:** ADB (Android Debug Bridge)

## Tasks Pending 📝
- Optimize voice recognition for more languages.
- Add more interaction features for better task management.
- Improve speed and performance for low-end systems.

## Connect with Me 👥
- [GitHub](https://github.com/santhoshakshit/)
- [LinkedIn](https://www.linkedin.com/in/santosh-akshit-8a67102b6/)
- [Instagram](https://www.instagram.com/__akshh._07/)
- 📧 Email: santhoshakshit@gmail.com

---
