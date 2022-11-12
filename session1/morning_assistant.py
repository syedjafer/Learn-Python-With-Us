from gtts import gTTS
import os
import espeakng
#engine.runAndWait()
from bs4 import BeautifulSoup as bs
import requests
import random


myspeaker=espeakng.Speaker()
myspeaker.wpm = 170
def speak(speaker,text,langu):
    speaker.voice=langu
    speaker.say(text, wait4prev=True)

url="https://www.autocarindia.com/car-news"
content=requests.get(url).text

text=["நல்லதே நடக்கும்",'''எதையும் தாங்கும் இதயம் இருந்தால்
இறுதி வரைக்கும் அமைதி இருக்கும்.''']

greetings='''காலை வணக்கம்'''
speak(myspeaker, greetings, 'dra')

data=bs(content, 'lxml')
for item in data.find_all("h6", class_="new-heding-h6")[:3]:
    speak(myspeaker, item.text,"en")


phrase=random.choice(text)
speak(myspeaker, phrase,"dra")


ending='''நன்றி வணக்கம்'''
speak(myspeaker, ending, 'dra')
