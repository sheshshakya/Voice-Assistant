import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib


print("Initializing Jarvis")
MASTER = "Shesh"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("good morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("good afternoon" + MASTER)

    else:
        speak("good Evening" + MASTER)

    speak("i am your assistant. How may I help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shakya1125@gmail.com', 'password')
    server.sendmail("madhu2003@gmail.com", to, content)
    server.close()

    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        query = None

    return query

def main():
    speak("Initializing Jarvis...")
    wishMe()
    query = takeCommand()

    
    if 'wikipedia' in query.lower():
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences =2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        
        url = "youtube.com"
        chrome_path ='C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        
        url = "google.com"
        chrome_path = 'C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir = "C:\music\music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'open code' in query.lower():
        codePath = "D:\Voive Ass"
        os.startfile(codePath)
    
    elif 'email to madhu' in query.lower():
        try:
            speak("what should i send")
            content = takeCommand()
            to = "madhu2003@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent to madhu")
        except Exception as e:
            print(e)


main()