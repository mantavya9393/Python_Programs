import speech_recognition as sr
import pyttsx3
import time
import webbrowser
import subprocess

r = sr.Recognizer()

engine = pyttsx3.init('sapi5')  # to get inbuilt windows voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

current = time.localtime(time.time())

def speak(audio):
    engine.setProperty("rate", 185)
    engine.say(audio)
    engine.runAndWait()

def greetings():
    if current.tm_hour < 12:
        speak("Good Morning Boss")
    if current.tm_hour >= 12 and current.tm_hour <= 16:
        speak("Good Afternoon Boss")
    if current.tm_hour > 16 and current.tm_hour <= 20:
        speak("Good Evening Boss")

def intro():
    speak("I am Jarvis.. your personal assistant")
    speak("Sorry Boss I forgot your name... Please say it again ")

    with sr.Microphone() as source:
        audio_data = r.record(source, duration=4)
        print("Recognizing.....")
        name = r.recognize_google(audio_data)
    speak("Ok.." + name + "....what are you up to?")

def commands():
    text = ""
    while text != "bye" or text != "no":
        print("Please talk and say Bye or NO to Stop...")
        with sr.Microphone() as source:
            audio_data = r.record(source, duration=4)
            print("Recognizing.....")
            text = r.recognize_google(audio_data)
            print(text)

        if text == "how are you":
            speak("I am fine, how are you?")
            time.sleep(1)
        elif text == "I am fine" or text == "I am good":
            speak("Great!, What you want to do?")
            time.sleep(1)
        elif text == "tell me a joke" or text == "joke":
            speak("..Placement")
            time.sleep(1)
        elif text == "I didn't get it" or text == "I did not get it":
            speak("Exactly")
            time.sleep(1)
        elif text == "self destruct":
            speak("self destructing in 3.... 2.... 1, haha, Just Kidding")
        elif text == "hungry" or text == "I am hungry":
            speak("Let's eat something.")
            webbrowser.open("https://www.zomato.com/india")
            time.sleep(2)
            speak("I hope you got it, Do you need anything else?")
        elif text == "open calculator" or text == "calculator":
            speak("opening calculator")
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            time.sleep(2)
            speak("I hope you got it, Do you need anything else?")
        elif text == "open Notepad" or text == "Notepad":
            speak("opening Notepad")
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
            time.sleep(2)
            speak("I hope you got it, Do you need anything else?")
        elif text == "open browser":
            speak("opening browser")
            subprocess.Popen('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
            time.sleep(2)
            speak("I hope you got it, Do you need anything else?")
        elif text == "map" or text == "open map":
            speak("opening google maps")
            webbrowser.open("https://www.google.com/maps")
            time.sleep(2)
            speak("I hope you got it, Do you need anything else?")
        elif text == "weather" or text == "what is the weather":
            speak("opening Accuweather")
            webbrowser.open("https://www.accuweather.com/en/in/ahmedabad/202438/weather-forecast/202438")
            time.sleep(2)
            speak("I hope you got it, Do you need anything else?")
        elif text == "open YouTube" or text == "YouTube":
            speak("opening YouTube")
            webbrowser.open("http://in.youtube.com/")
            time.sleep(2)
            speak("I hope you got it, Do you need anything else?")
        elif text == "bye" or text == "no":
            if current.tm_hour > 20:
                speak("Okay, Good Night Boss")
            else:
                speak("Okay Boss...Bye, have a good day")
            break
        else:
            speak("sorry..I didn't get that, Say again?")


greetings()
intro()
commands()
