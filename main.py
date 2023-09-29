import pyttsx3
import speech_recognition as sr
import subprocess

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Function to speak a response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)
    return audio

# Main loop for the voice assistant
while True:
    try:
        audio = listen()
        query = recognizer.recognize_google(audio)  # Use Google Web Speech API for recognition
        print("You said:", query)
        speak("You said: " + query)

        # Open applications based on voice commands
        if "open notepad" in query.lower():
            subprocess.Popen(["notepad.exe"])
        elif "open calculator" in query.lower():
            subprocess.Popen(["calc.exe"])
        elif "open chrome" in query.lower():
            subprocess.Popen(["chrome.exe"])  # Change this to your browser's executable
        elif "exit" in query.lower():
            speak("Goodbye!")
            break
        else:
            speak("I'm not sure how to respond to that.")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Can you please repeat?")
        speak("Sorry, I didn't catch that. Can you please repeat?")
    except sr.RequestError:
        print("Sorry, I'm having trouble processing your request. Please try again later.")
        speak("Sorry, I'm having trouble processing your request. Please try again later.")

