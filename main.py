# installed packages
# pyttsx3, SpeechRecognition, PyAudio, selenium

import pyttsx3 as p
import speech_recognition as sr
from selenium_web import Infow
from yt_audio import *
from News import *
import randfacts
from jokes import *
import weather

# used to initiate pyttsx3
engine = p.init()

# to get the range of voice i.e. the speed of voice
rate = engine.getProperty('rate')

# to set the speed of voice
engine.setProperty('rate',180)

# to get voices and to set voices
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


# creates an instance to take audio from our microphone
r = sr.Recognizer()




speak("Hello sir, I am you voice assistant . ")
speak("Temperature in mumbai is " + str(weather.temp()) + "degree celcius" + "and with" + str(weather.des()))
speak("what can i do for you ?")

with sr.Microphone() as source:
    # to get clear voice and not take any background noise
    r.energy_threshold=4000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    # listens to our audio and saves it in the variable audio
    audio = r.listen(source)
    # it gives the audio to google api engine and converts the audio to text
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak("I am also having a good day sir")
speak("How can I help you")

with sr.Microphone() as source:
    # to get clear voice and not take any background noise
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

def listen_and_recognize():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        r.energy_threshold = 4000
        print("Listening...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print("You said:", text)
        return text

if text2 and "information" in text2:
    speak("You need information related to which topic?")
    infor = listen_and_recognize()
    if infor:
        print(f"Fetching information about: {infor}")
        # Create an instance of the Infow class and get information
        assist = Infow()
        assist.get_info(infor)
        speak("Here is the information you requested.")

elif "play" and "video" in text2:
    speak("You want to play which video?")
    vid = listen_and_recognize()
    if vid:
        print(f"play video for: {vid}")
        # Create an instance of the Infow class and get information
        assist = Music()
        assist.get_info(vid)
        speak("Here is the video you requested.")

elif "news" in text2:
    print("Sure sir, now i will read news for you. ")
    speak("Sure sir, now i will read news for you. ")

    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "facts" or "fact" in text2:
    speak("Sure sir")
    x=randfacts.getFact()
    print(x)
    speak("Did you know that")

elif "joke" or "jokes" in text2:
    speak("Sure sir")
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])



