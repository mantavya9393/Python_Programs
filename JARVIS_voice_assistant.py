# created my own JARVIS (voice assistance) in python.

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
    if current.tm_hour > 16:
        speak("Good Evening Boss")

def intro():
    speak("I am Jarvis.. your personal assistant")
    speak("Sorry Boss I forgot your name...Please say it again")

    with sr.Microphone() as source:
        audio_data = r.record(source, duration=4)
        print("Recognizing.....")
        name = r.recognize_google(audio_data)
    speak("Ok.." + name + "....what are you up to?")

def commands():

    text = ""
    while text != "bye" or text != "no" or text == "stop":
        print("Please talk and say Bye or NO to Stop...")
        try:
            with sr.Microphone() as source:
                audio_data = r.record(source, duration=4)
                print("Recognizing.....")
                text = r.recognize_google(audio_data)
                print(text)

            if text == "how are you":
                speak("I am fine, how are you?")
                time.sleep(1)
            elif text == "kem cho" or text == "KEM chho":
                speak("iik dum majama boss, tamae kem cho?....also I prefer english")
                time.sleep(1)
            elif text == "hello" or text == "hi":
                speak("Hello Boss")
                time.sleep(1)
            elif text == "I am fine" or text == "I am good":
                speak("Great!, What you want to do?")
                time.sleep(1)
            elif text == "tell me a joke" or text == "joke":
                speak("...Placement")
                time.sleep(1)
            elif text == "I didn't get it" or text == "I did not get it":
                speak("Exactly")
                time.sleep(1)
            elif text == "self destruct":
                speak("self destructing in 3.... 2.... 1, haha, Just Kidding")
                time.sleep(1)
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
            elif text == "open browser" or text == "Browser":
                speak("opening browser")
                subprocess.Popen('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
                time.sleep(2)
                speak("I hope you got it, Do you need anything else?")
            elif text == "map" or text == "maps" or text == "open map" or text == "open maps" or text == "open Google Maps":
                speak("opening Google Maps")
                webbrowser.open("https://www.google.com/maps")
                time.sleep(2)
                speak("I hope you got it, Do you need anything else?")
            elif text == "weather" or text == "what is the weather" or text == "what is today's weather":
                speak("opening Accuweather")
                webbrowser.open("https://www.accuweather.com/en/in/ahmedabad/202438/weather-forecast/202438")
                time.sleep(2)
                speak("I hope you got it, Do you need anything else?")
            elif text == "open YouTube" or text == "YouTube":
                speak("opening YouTube")
                webbrowser.open("http://in.youtube.com/")
                time.sleep(2)
                speak("I hope you got it, Do you need anything else?")
            elif text == "play song" or text == "play a song" or text == "song":
                speak("Which song would you like to hear?")
                with sr.Microphone() as source:
                    audio_data = r.record(source, duration=4)
                    print("Recognizing.....")
                    song_name = r.recognize_google(audio_data)
                    print(song_name)
                webbrowser.open("https://music.youtube.com/search?q=" + song_name)
                time.sleep(2)
                speak("I hope you got it, Do you need anything else?")
            elif text == "bye" or text == "no" or text == "no thank you" or text == "stop":
                if current.tm_hour > 20:
                    speak("Okay Boss, Good Night")
                else:
                    speak("Okay Boss...Bye, have a good day")
                break
            elif len(text) == 0:
                speak("sorry..I didn't get that, Say again?")
            else:
                speak("sorry..I didn't get that, Say again?")
        except :
            speak("sorry..I didn't get that, please say it again")


greetings()
intro()
commands()
