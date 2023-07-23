import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import subprocess


ai = pyttsx3.init("sapi5")
voices = ai.getProperty("voices")
ai.setProperty("voice", voices[1].id)


def speak(audio):
    ai.say(audio)
    ai.runAndWait()
# def wakeup():
#     speak("hello whats up yo?")
#     query = takecommand().lower()
#     if "oliver wake up" in query:
#         speak("hello mr jayandhan , the best Ai expert in the world what shall i do for you?")


def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning beautiful")
        print("Good morning beautiful")
    elif 12 <= hour < 18:
        speak("Good afternoon dude, what's up!")
        print("Good afternoon dude, what's up!")
    else:
        speak("Good evening  kanishkaran  how was your day! , i  am the newly formed  AI by jayandhan")
        #print("Good evening  the AI expert")
    #speak("I am oliver speaking the best ai in the world , What shall I do for you?")
    #print("I am oliver speaking the best ai in the world , What shall I do for you?")
    # speak("I feel happy to help you ")
    # print("I feel happy to help you ")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)# Corrected syntax for Microphone
        speak("i am Listening... please say something")
        print("i am Listening... please say something")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        speak("i am recognizing your voice")
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        speak("Say that again please...")

    return query

# wakeup()
wishme()
end = True
while end:
    query = takecommand().lower()
    if "wikipedia" in query:
        speak("searching in wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        wb.open("youtube.com")
    elif 'open google' in query:
        wb.open("google.com")
    elif 'open stackoverflow' in query:
        wb.open("stackoverflow.com")
    elif 'play movie' in query:
        moviedir = r"D:\Captures - Copy"
        movie = os.listdir(moviedir)
        print(movie)
        os.startfile(os.path.join(moviedir,random.choice(movie)))
    elif "open notepad" in query:
        path1 = r"C:\Program Files\WindowsApps\Microsoft.WindowsNotepad_11.2302.26.0_x64__8wekyb3d8bbwe\Notepad"
        subprocess.Popen(path1)
    elif "open visual studio code" in query:
        path2 = r"C:\Users\jayan\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        subprocess.Popen(path2)
    elif "search" in query:
        path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
        wb.open_new_tab(query)
    elif "what" in query:
        path3 = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
        wb.open_new_tab(query)
    elif "keep quiet" in query:
        end = False
        speak("okay fine i am turning off")
        print("okay fine i am turning off")
    elif "piece of advice" in query:
        speak("hello Mr kanishkaran , how are you doing , eat well drink plenty of water , study python programming and excercise well")




