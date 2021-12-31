import os
import psutil
import bs4
import pyttsx3
import  datetime
# import time
import speech_recognition as sr
# import cv2
# from googletrans import Translator
# from gtts import gTTS
from requests import get
import wikipedia
import wikipedia as googleScrap
import webbrowser
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
import urllib.request
import re
import keyboard
# import xrsze_rmndr
import random
import requests
# import pyjokes
import pywhatkit
import pyautogui  # for controling system vollume
from bs4 import BeautifulSoup
import googlesearch
from googletrans import Translator






# init() function to get an engine instance for the speech synthesis
# sapi5 = Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft. Starting with Windows XP, it ships as part of the Windows OS.
engine = pyttsx3.init('sapi5')
# getting all voices present in system
voices = engine.getProperty('voices')
# seting  voice
engine.setProperty('voice',voices[1].id)
# setting rate of speach
engine.setProperty('rate',110)

def speak(audio):
    print("         ")
    print(audio)
    print("         ")
    # say func is used for speack the text
    engine.say(audio)
    # runAndWait mathod is used for processing the voice command
    engine.runAndWait()


def take_opening_command():
    while True:
        hour = datetime.datetime.now().hour
        if hour >= 1 and hour <= 24:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...........")
                r.pause_threshold = 1
                audio = r.listen(source,0,5)

            try:
                print("Recognizing..........")
                query = r.recognize_google(audio, language='en-in')
                print(f"user said : {query}")

            except Exception as e:
                speak(" ")
                return "none"
            return query


def take_command():
    while True:
        hour = datetime.datetime.now().hour
        if hour >= 1 and hour <= 24:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...........")
                r.pause_threshold = 1
                audio = r.listen(source,0,10)

            try:
                print("Recognizing..........")
                query = r.recognize_google(audio, language='en-in')
                print(f"user said : {query}")

            except:

                return " "

            return query



def take_Hindi_command():
    while True:
        hour = datetime.datetime.now().hour
        if hour >= 1 and hour <= 24:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...........")
                r.pause_threshold = 1
                audio = r.listen(source,0,5)

            try:
                print("Recognizing..........")
                query = r.recognize_google(audio, language='hi')
                print(f"user said : {query}")

            except Exception as e:
                speak(" ")
                return "none"
            return query

def wish(command):
    hour = int(datetime.datetime.now().hour)
    def great():
        if hour >= 0 and hour <= 12:
            speak("Good Mornig Sir ")
        elif hour > 12 and hour < 18:
            speak("Good After Noon Sir ")
        else:

            speak("Good evening sir")
    great()
    str = "How can i help you "
    speak(str)
    # commands = take_command().lower()
    # feelings = ["said","happy","fine","good","great","sad"]
    # if command  in feelings :
    #     speak("it's good i pray to the god for sending happiness in your life")
    #     print(command, "its a command")

def talk_to_ai(command):
    if 'thank you' in command:
        speak("it's my plaser ")
        print(command, "its a command")
    elif 'how are you' in command:
        lst = ["I'm fine sir ", "I'm  phasing some problem sir ", "I'm  happy"]
        rand_res = random.choice(list(lst))
        speak(rand_res)
        speak("thank you for asking to me sir ")
        print(command, "its a command")
    print(command, "its a last line command command")

def youtube_automation(commands):

    if "pause" in commands:
        keyboard.press('space bar')
    elif "play" in commands:
        keyboard.press("space bar")
    elif 'full screen' in commands:
        keyboard.press('f')
    elif 'normal screen' in commands:
        keyboard.press('f')
    elif 'skip' in commands:
        keyboard.press('l')
    elif 'back' in commands:
        keyboard.press('j')
    elif 'youtube mute' in commands:
        keyboard.press('m')
    elif 'youtube unmute' in commands:
        keyboard.press('m')
    elif 'fast forward' in commands:
        keyboard.press_and_release('shift + .')
    elif 'slow' in commands: # not working
        keyboard.press_and_release('shift + ,')
    elif 'volume up' in commands:
        keyboard.press_and_release('shift + P')
    elif 'next' in commands:
        keyboard.press_and_release('shift + N')
    elif "volume up" in commands or "increase volume" in commands:
        speak("how much volume i increase.. example.. increase volume 10%")
        input = take_command()
        try:
            removing_unwant_phase_1 = input.replace("%","")
            removing_unwant_phase_2 = int(removing_unwant_phase_1.replace("increase volume ",""))
            volume = int(removing_unwant_phase_2/2)
            i = 0
            while (i<volume):
                pyautogui.press("volumeup")
                i+=1
        except Exception as e:
            speak("phasing problem on increasing volume")
    elif "volume down" in commands or "decrease volume" in commands:
        speak("how much volume i decrease.. example..> decrease volume 10%")
        input  = take_command()
        try:
            removing_unwant_phase_1 = input.replace("%","")
            removing_unwant_phase_2 = int(removing_unwant_phase_1.replace("decrease volume ",""))
            print(removing_unwant_phase_2)
            volume = int(removing_unwant_phase_2/2)
            print(volume)
            i=0
            while (i<volume):
                pyautogui.press("volumedown")
                i+=1
        except Exception as e:
            speak("phasing problem on decreasing volume")

    elif "mute" in commands or "volume mute" in commands or "nude" in commands:
        pyautogui.press("volumemute")

def weather_forcast(command):
    if "today's temperature" in command or "weather forecast" in command or "today's weather" in command or "today weather" in command:
        url = f"https://www.google.com/search?q={command}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_ = "BNeawe").text
        speak(f"current {command} is {temp}")


# def translator(): # not working currect as aspected
#     speak("speak what you want to translate")
#     query = take_Hindi_command()
#     trans = Translator()
#     result = trans.translate(query,'en','auto')
#     text = result.text
#     speak(text)




def time_teller(commands):
    hour = datetime.datetime.now().hour
    minut = datetime.datetime.now().minute
    if "time" in commands:
        if (hour <= 12):
            phase = "AM"
        else:
            phase = "PM"
        speak(f"{hour}:{minut} {phase}")
def google_search(commands):
    if "open google" in commands:
        co_co = commands.replace("open google","")
        ed_cmd_this_funk = co_co.replace(" ", "+")
        if ed_cmd_this_funk == "":
            speak("what should i search on google")
        ed_cmd_this_funk = take_command()
        ed_cmd = ed_cmd_this_funk.replace(" ", "+")
        webbrowser.open("https://search.yahoo.com/search?fr=mcafee&type=E211US885G0&p=" + ed_cmd)
        speak("searching on google")
    if "search" in commands:
        co_co = commands.replace("search","")
        ed_cmd = co_co.replace(" ", "+")
        if ed_cmd =="" :
            speak("what should i search on google ")
        search_cmd = take_command()
        ed_cmd1 = search_cmd.replace(" ", "+")
        webbrowser.open("https://search.yahoo.com/search?fr=mcafee&type=E211US885G0&p=" + ed_cmd1)
        speak("searching on google")

    elif "what is" in commands or  "meaning of" in commands or  "where is" in commands  or "who is" in commands:
        commands  = commands.replace("what is","")
        commands  = commands.replace("friday","")
        commands  = commands.replace("search","")


        try:
            pywhatkit.search(commands)
            result = googleScrap.summary(commands,2)
            speak("i found something")
            speak(result)
        except Exception as e:
            speak("no speakable data found")




def about_friday(command):
    if "about yourself" in command:
        speak("my name is friday !")
        speak("my version is 0.1")
        speak("sir ankush creaded me")
        speak("am still learning for better help")

def my_name(command):
    if "your name" in command:
        speak("my name is friday !")
    if "who are you" in command:
        speak("my name is friday !")
        speak("i am  your virtual assistante ")

def jokes(commands):
    if "joke" in commands:
        jokeitem = 'yes'
        information = requests.get(f"https://icanhazdadjoke.com/search?term={jokeitem}",
                                   headers={"Accept": "application/json"})
        connection = information.ok
        result = information.json()
        l_no_of_jokes = result["results"]
        no_of_jokes = len(l_no_of_jokes)
        print(no_of_jokes, "length of jokes")

        response = ""
        if no_of_jokes == 0:
            while no_of_jokes == 0:
                response = input("Try some other word(Type 'quit' to quit): ")
                if response == "quit":
                    break

                else:
                    information = requests.get(f"https://icanhazdadjoke.com/search?term={response}",
                                               headers={"Accept": "application/json"})
                    result = information.json()
                    l_no_of_jokes = result["results"]
                    no_of_jokes = len(l_no_of_jokes)

        if response != "quit":
            information = requests.get(f"https://icanhazdadjoke.com/search?term={response}",
                                       headers={"Accept": "application/json"})
            l_no_of_jokes = result["results"]
            no_of_jokes = len(l_no_of_jokes)
            # print(f"There are {no_of_jokes} joke/s available.\n")
            # print(f"The {no_of_jokes} jokes are:\n")

            rand_num = random.randint(0, no_of_jokes)
            jokes = (l_no_of_jokes[rand_num]['joke'])
            speak(jokes)

def Whatsapp_masseg_send(commands):

    if "send message" in commands:
        speak("who do you want to message..")

        name_send=take_command().lower()

        if "deepak" in name_send:
            speak("what message want to send..")
            massege_send = str(take_command())
            speak("you want to send message now or letter")
            message_now = take_command().lower()
            if message_now != "now":
                speak("on which time you want to send message..")
                time_for_sendMasseg = take_command()
                time_for_sendMasseg1 = time_for_sendMasseg.split(" ")
                minut_time_for_sendMasseg1 = int(time_for_sendMasseg1[0])
                hour_time_for_sendMasseg1 = int(time_for_sendMasseg1[3])
                pywhatkit.sendwhatmsg("+918368185229",massege_send,hour_time_for_sendMasseg1,minut_time_for_sendMasseg1)

            elif massege_send=="now":
                pywhatkit.sendwhatmsg_instantly()

        if "priyanshu" in name_send:
            speak("what message want to send..")
            massege_send = str(take_command())
            speak("you want to send message now or letter")
            message_now = take_command().lower()
            if message_now != "now":
                speak("on which time you want to send message..")
                time_for_sendMasseg = take_command()
                time_for_sendMasseg1 = time_for_sendMasseg.split(" ")
                minut_time_for_sendMasseg1 = int(time_for_sendMasseg1[0])
                hour_time_for_sendMasseg1 = int(time_for_sendMasseg1[3])
                pywhatkit.sendwhatmsg("+9193196 43218",massege_send,hour_time_for_sendMasseg1,minut_time_for_sendMasseg1)

            elif massege_send=="now":
                pywhatkit.sendwhatmsg_instantly()

def opening_system_app(commands):
    if"open notepad" in commands:
        notpad_path = "C:\\Windows\\system32\\notepad.exe"
        speak("opening notepad")
        os.startfile(notpad_path)
    elif "open pycharm" in commands:
        pycharm_path = "C:\\Program Files\\JetBrains\PyCharm Community Edition 2021.2.2\\bin\\pycharm64.exe"
        speak("opening pycharm")
        os.startfile(pycharm_path)
    elif "open command prompt" in commands:
        speak("opening command promt")
        os.system("start cmd")
        speak("opening command promt")
    elif "play music" in commands:
        path = "C:\\Users\\asus\\AppData\\Local\\Programs\\Resso\\Resso.exe"
        os.startfile(path)
        speak("playing music")
    elif "play song" in commands:
        path = "C:\\Users\\asus\\AppData\\Local\\Programs\\Resso\\Resso.exe"
        os.startfile(path)
        speak("playing song")
    elif "ip address" in commands:
        ip = get('https://api.ipify.org').text
        speak(f"My IP address is {ip} ")
    elif "set reminder" in commands:
        path = 'E:\\CISCO\\set_reminder.py'
        os.startfile(path)
    elif "play movie" in commands:
        speak("select your movie and watch")
        path = f"D:\\"
        os.startfile(path)

    elif "open chrome" in commands:
        path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        speak("opening chrome")
        os.startfile(path)

    elif "open vs code" in commands:
        path = "C:\\Users\\asus\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
        speak("opening vs code ")
        os.startfile(path)
    elif "open brave" in commands:
        path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        speak("opening brave browser")
        os.startfile(path)
    elif "open file manager" in commands:
        path = "D:\\"
        speak("opening file manager")
        os.startfile(path)
    elif "open gmail" in commands:
        path = "https://mail.google.com/mail/u/0/#inbox"
        speak("opening gmail")
        webbrowser.open(path)




def closing_window_tabs(commands): # not working
    if "close chrome" in commands:
        os.system("taskkill /im chrome.exe /f")
        speak("closing chrome")


def wikipedia_search(command):
    if "according to wikipedia" in command:
        speak("searching.....! your qyery on wikipedia")
        query1 = command.replace("according to wikipedia", "")

        result = wikipedia.summary(query1, 2)
        speak("according to wikipedia ")
        speak(result)

def Battery_check(command):

    def converter(second):
        minutes , second = divmod(second,60)
        hours , minutes = divmod(minutes,60)
        return "%d:%02d:%02d"%(hours,minutes,second)

    battery = psutil.sensors_battery()
    if "battery percentage" in command :
        plug = str(battery.power_plugged)
        if plug == "True":
            speak(f"{battery.percent} % battery charged")
            speak("power is still plugged")
        if plug=="False":
            speak(f"{battery.percent} % battery remains .power is not plugged and battery life is {converter(battery.secsleft)}")
            speak("")



def task_funktions(command):
    # query = take_command().lower()
    # print("inside task_function")
    if "friday" in command:
        # translator()
        talk_to_ai(command)
        youtube_automation(command)
        google_search(command)
        my_name(command)
        about_friday(command)
        google_search(command)
        jokes(command)
        opening_system_app(command)
        time_teller(command)
        Whatsapp_masseg_send(command)
        weather_forcast(command)
        wikipedia_search(command)
        closing_window_tabs(command)
        # direct_QNA_with_friday(query)
    if "according to wikipidia" in command:
        speak("searching.....! your qyery on wikipidia")
        query1 = command.replace("what is", "")

        result = wikipedia.summary(query1, 2)
        speak("according to wikipedia ")
        speak(result)



    elif "open youtube" in command:
        speak("what should search on youtube")


        search = take_command().lower()

        ed_search = search.replace(" ", '+')
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + ed_search)
        video_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        video_link = "https://www.youtube.com/watch?v=" + video_id[0]
        webbrowser.open(video_link)

    elif "open whatsapp" in command:
        url = 'https://web.whatsapp.com/'
        webbrowser.open(url)
        speak("opening whatsapp")


if __name__ == '__main__':
# while True:
# # start = take_opening_command().lower()
# #
# # if "friday"in start:
# #     wish(start )
    while True:
        print("abobe main")
        command = take_opening_command().lower()
        print("inside main")
        if "friday" in command or "friday" in command:
            if"friday"in command:
                task_funktions(command)
                speak("yes sir ")
        if "exit" in command or "take rest" in command or "take a rest" in command or "quit" in command:
            speak("ok sir . But when you need my help just call me")
            break

        talk_to_ai(command)
        youtube_automation(command)
        google_search(command)
        my_name(command)
        about_friday(command)
        jokes(command)
        Battery_check(command)
        # direct_QN A_with_friday(command)
        opening_system_app(command)
        time_teller(command)
        Whatsapp_masseg_send(command)
        weather_forcast(command)
        task_funktions(command)
        wikipedia_search(command)
        closing_window_tabs(command)
        # translator()