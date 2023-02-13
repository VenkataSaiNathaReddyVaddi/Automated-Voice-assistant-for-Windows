import time
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import pyautogui
from plyer import notification
from bs4 import BeautifulSoup
from subprocess import call
import requests
from playsound import playsound
import pynput
#import mouseimport
#import cv2 
#import mediapipe as mp
from math import hypot
import screen_brightness_control as sbc
import numpy as np 
import pywhatkit
# Import nmap so we can use it for the scan
import nmap
# We need to create regular expressions to ensure that the input is correctly formatted.
import re
from pynput.keyboard import Key,Controller



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!sir")
        playsound('C:\\Users\\Venka\\Downloads\\Jarvis.mp3')
        speak("sir,this is jarvis . your own artificial desktop assistant ,waiting for your order")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!sir")
        playsound('C:\\Users\\Venka\\Downloads\\Jarvis.mp3')
        speak("sir,this is jarvis . your own artificial desktop assistant ,waiting for your order")

    else:
        speak("Good Evening!sir ")
        playsound('C:\\Users\\Venka\\Downloads\\Jarvis.mp3')
        speak("sir,this is jarvis . your own artificial desktop assistant ,waiting for your order")
    

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Sir!please say that again...")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query :
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'joke' in query:
            random_joke = pyjokes.get_joke()
            print(random_joke)
            speak(random_joke)

        elif 'screenshot' in query:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            speak('Screenshot taken.')

        elif 'jarvis are you there' in query:
            speak("yes sir,do you nedd any help?")        

        elif 'shutdown' in query:
            speak("sure sir,good bye! see you soon")
            pyautogui.hotkey('alt','f4')
            pyautogui.press('enter')
   
        elif 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "how" in query or "who" in query or "what" in query or "which" in query or "why" in query or "where" in query or "when" in query:
            query = query.replace("search","")
            query = query.replace("on google","")
            query = query.replace("google","")
            string = query.split()
            search = ""
            for i in string:
                search += i
        
                search += "+"

            webbrowser.open(f"https://www.google.com/search?q={search}&oq={search}&aqs=chrome.0.69i59j0i22i30l9.3639j0j15&sourceid=chrome&ie=UTF-8")
            results = wikipedia.summary(query, sentences=3)
            speak(results)
                  
        elif 'restart' in query:
            speak("ok sir i will restart your pc")
            pyautogui.hotkey('alt','f4')
            pyautogui.hotkey('down')
            pyautogui.press('enter')

            
        elif 'increase the volume' in query:
            pyautogui.hotkey('Fn', 'f12',clicks=10)
            speak("volume adjusted to it's full capacity sir")

        elif 'decrease the volume ' in query:
            pyautogui.hotkey('Fn', 'f11',clicks=5,interval=0.2)
            speak("volume adjusted to it's half capacity sir")

        elif 'brightness' in query and 'full' in query:
            sbc.set_brightness(100)
            speak("brightness adjusted to it's full capacity sir")

        elif 'brightness' in query and 'half' in query:
            sbc.set_brightness(50)
            speak("brightness adjusted to it's half capacity sir")

        elif 'decrease the brightness' in query:
            sbc.set_brightness(0)
            speak("sir the brightness is adjusted to zero")

        elif 'close' in query:
            pyautogui.hotkey('alt', 'f4')
            speak("sure,sir")

        elif 'copy' in query:
            pyautogui.hotkey('ctrl', 'c')
            speak("copying completed")

        elif 'paste' in query:
            pyautogui.hotkey('ctrl', 'v')
            speak("ok sir!")

        elif 'select all' in query:
            pyautogui.hotkey('ctrl', 'a')
            speak("selected everything ,on this window sir")

        elif 'close my current tab' in query:
            pyautogui.hotkey('ctrl','w')

        elif 'scroll up' in query:
            pyautogui.hotkey('up')

        elif 'scroll down' in query:
            pyautogui.hotkey('down')
           

        elif 'jarvis play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")            
            
        elif 'minimise' in query:
             pyautogui.hotkey('win', 'down')

        elif 'maximize' in query:
             pyautogui.hotkey('win', 'up')

        elif 'mails' in query:
            webbrowser.open("gmail.com")
            speak("opening email")

        elif 'play' in query and 'jarvis' in query:
            song=query.replace('play',' ')
            song=query.replace('jarvis',' ')
            speak('ok sir playing'+song+'on youtube')
            pywhatkit.playonyt(song)


        elif 'type my words' in query:
            speak("sure sir! please dictate me what you want to type")
            try:
                keyboard=Controller()
                tye=takeCommand()
                keyboard.type(tye)
            except Exception as e:
                speak(e)
                print(e)
                
        elif 'open' in query:
            query=query.replace("open","")
            pyautogui.hotkey('win','s')
            time.sleep(1)
            pyautogui.write(query)
            time.sleep(1)
            pyautogui.press('enter')
            pyautogui.press('enter')


                        
