#!/usr/bin/env python
import speech_recognition as sr
from snowboy import snowboydecoder 
import playsound
import subprocess
import os
import datetime
import webbrowser
import pygame

# NOTES: need a math focalized STT, that recognize exponential operators, 
# and roots better; 

results=["empty"]

def stt():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)
        playsound.playsound('sounds/4.mp3', True)
        audio = r.listen(source)
        
    try:
        i = r.recognize_google(audio, language='en-EN')
        

    except :
        print ("ERROR")
        i=""
    return i
    

def mt(x):
    x=x.replace(" ","")
    x=x.replace("x","*")
    x=x.replace("÷","/")
    try:
        y=eval(x)
        return y
    except:
        print("eval error")
    

def detected_callback(): 
    print("-listening-")
    detector.terminate()

def print_gui(x):
    lbl = Label(window, anchor=CENTER, text=x, font=("Hack",20))
    lbl.grid(column=0, row=0)

detector = snowboydecoder.HotwordDetector("STT/hey_newbie1.pmdl", 
                                          sensitivity = 0.5, audio_gain = 1)

playsound.playsound('sounds/5.mp3', True)
os.popen(f"notify-send welcome\ back\ buddy!")

while True:
    
    detector.start(detected_callback)
    
    i=stt()
    print(i)

    if "show last result" in i.lower():
        print(f"\nHere you are: {results[-1]}")
    
    if "open" in i.lower():
        if "telegram" in i.lower():
            try:
                subprocess.Popen("org.telegram.desktop")
            except Exception as e:
                print(e)
        if "spotify" in i.lower():
            try:
                subprocess.Popen("com.spotify.Client")
            except Exception as e:
                print(e)
        else:
            i=i.lower()
            il=i.split(" ")
            index=il.index("open")
            try:
                subprocess.Popen(f"{il[index+1]}")
            except Exception as e:
                print("Error: ",e)

    if "close" in i.lower():
            i=i.lower()
            il=i.split(" ")
            index=il.index("close")
            try:
                os.popen(f"pkill {il[index+1]}")
            except Exception as e:
                print("Error: ",e)
    
    if "get me to" in i.lower():
        i=i.lower()
        il=i.split(" ")
        index=il.index("to")
        path=il[index+1]
        os.popen(f"dolphin ~/{path.title()}") 
    
    if "update" in i.lower():
        subprocess.Popen(["sh", "Newbie.sh"]) #the second time often get error
        quit()
    
    if "time" in i.lower(): #the notification need to be formatted
        os.popen(f"notify-send {datetime.datetime.now().time()}")
    
    if "date" in i.lower(): #the notification need to be formatted
        os.popen(f"notify-send {datetime.datetime.now().date()}")
        
    if "quit" in i.lower():
        quit()
        exit()
    
    if "shut down" in i.lower():
        os.popen("shutdown -h now ") 
    
    if "lock" in i.lower() or "lockup" in i.lower() and "screen" in i.lower():
        os.popen("qdbus org.freedesktop.ScreenSaver /ScreenSaver Lock")
    
    if "print" in i.lower() and "say" in i.lower(): #not functioning
       a=stt()
       os.popen(f"notify-send {a}")
    
    if "search for" in i.lower() or "take a look for" in i.lower():
        i=i.lower()
        il=i.split(" ")
        index=il.index("for")
        target=' '.join(il[index+1:])
        url=f"https://duckduckgo.com/?q={target}&t=brave&ia=web"
        webbrowser.open(url, new=0, autoraise=True)
    
    if "what" in i.lower() and "about" in i.lower():
        i=i.lower()
        il=i.split(" ")
        index=il.index("about")
        target=' '.join(il[index+1:])
        url=f"https://duckduckgo.com/?q=!w {target.title()}&t=brave&ia=web"
        webbrowser.open(url, new=0, autoraise=True)
    
    if "volume" in i.lower():
        if "up" and "by" in i.lower():
            i=i.lower()
            i=i.replace("volume","")
            i=i.replace("up","")
            i=i.replace("by","")
            i=i.replace(" ","")
            os.popen(f"amixer -q sset Master {i}+")
        
        elif "down" and "by" in i.lower():
            i=i.lower()
            i=i.replace("volume","")
            i=i.replace("down","")
            i=i.replace("by","")
            i=i.replace(" ","")
            os.popen(f"amixer -q sset Master {i}-")
        
        elif "set" and "to" in i.lower():
            i=i.lower()
            i=i.replace("volume","")
            i=i.replace("set","")
            i=i.replace("to","")
            i=i.replace(" ","")
            os.popen(f"amixer sset 'Master' {i}")

    else: # it always get executed unless the last if is satisfied
        res=mt(i)
        j=f"\nHere you are:\n{res}"
        print(j)
        results.append(res)
