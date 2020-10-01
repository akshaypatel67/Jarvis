import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio

import datetime
from email.mime import audio

engine = pyttsx3.init("sapi5")

# volume = engine.getProperty("volume")
# engine.setProperty("volume", 1)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio1):
    engine.say(audio1)
    engine.runAndWait()


def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak('Good Morning')
    elif 12 <= hour < 18:
        speak('Good Afternoon')
    elif hour >= 18:
        speak('Good Evening')




def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query


if __name__ == "__main__":
    speak('Welcome Priyanshu')
    greet()
    speak('How can I help you sir?')

    while True:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'date' in query:
            strDate = datetime.datetime.now().date()
            reply = f"Sir, the date is {strDate}"
            print(reply)
            speak(reply)
            
        elif 'where is' in query:
            query = query.replace("where is ", "")
            reply = f"finding location of {query} on maps"
            print(reply)
            speak(reply)
            webbrowser.open("https://www.google.com/maps/place/" + query)
            
        elif 'joke' in query:
            joke_results = pyjokes.get_joke()   # gets a random joke
            print(joke_results)
            speak(joke_results)

