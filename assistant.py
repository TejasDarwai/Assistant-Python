import sys
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import pyjokes
import pywhatkit
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am now online Sir. Please tell me how may I help you")       

def changeassistant():
    engine.setProperty('voice', voices[4].id)
    speak("Hello sir, its zara , I am online now")


def execution():
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'hello' in query:
            speak("hello sir, how are you")
        elif 'what about' in query:
            speak("I am good sir, here to help you")
        elif 'evening' in query:
            speak("Good Evening sir, how's your day")
        elif 'bored' in query:
            speak("may I play a song")
            speak("or, I have a joke, may I")
        elif 'ok tell the joke' in query:
            speak(pyjokes.get_joke())         
        elif 'wikipedia' in query:
            speak("Searching wikipedia...")
            print(query)
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentance = 2)
            speak("According to wikipedia")
            speak(results)
            print(results)
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
        elif 'open my mails' in query:
            speak("Opening Emails")
            webbrowser.open("gmail.com")
        elif 'play' in query:
            song = query.replace('play', ' ')
            speak("playing" + song)        
            print("playing your song jut a secs")
            pywhatkit.playonyt(song)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'change assistant' in query:
            speak("switching to zara")
            changeassistant()    
        elif 'visual studio code' in query:
            vsPath = "C:\\Users\\tejas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsPath)    
        elif 'go to sleep' in query:
            speak("I am going to sleep mode, wake me when you need me")
            break
        elif 'shutdown' in query:
            speak("shutting down, have a good day")
            sys.exit()

if __name__ == "__main__":
    speak(" Hello its me your virtual assistant ")
    while True:
        permit = takeCommand().lower()
        if 'wake up' in permit:
            execution()
        elif 'shutdown' in permit:
            speak("shutting down, have a good day")
            sys.exit()