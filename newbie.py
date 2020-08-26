#!/usr/bin/env python
import speech_recognition as sr
from snowboy import snowboydecoder 
import playsound
import subprocess
import os
import datetime
import webbrowser

def stt_init():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
    return r

def stt(r):
    with sr.Microphone() as source:
        playsound.playsound('sounds/4.mp3', True)
        audio = r.listen(source)
    try:
        i = r.recognize_google(audio, language='en-EN')
    except :
        print ("ERROR")
        i=""
    
    return i
    
def detected_callback(): 
    print("-keyword detected-")
    hotword_detector.terminate()
    
hotwords = ["STT/hey_newbie1.pmdl", "STT/hey_newbie2.pmdl"]

hotword_detector = snowboydecoder.HotwordDetector(hotwords, 
                                          sensitivity = 0.5, audio_gain = 1)

detector = [snowboydecoder.HotwordDetector("STT/_time_.pmdl", 
                                           sensitivity = 0.5, audio_gain = 1),
snowboydecoder.HotwordDetector("STT/_day_.pmdl", 
                                           sensitivity = 0.5, audio_gain = 1)]


R = stt_init()

playsound.playsound('sounds/5.mp3', True)
os.popen(f"notify-send Welcome\ back\ buddy!")

while True:
    hotword_detector.start(detected_callback)

    
    

   

