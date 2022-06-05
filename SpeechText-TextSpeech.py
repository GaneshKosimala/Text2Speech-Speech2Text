import pyttsx3 as pys
import speech_recognition as sr
import datetime
import engineio
def speak(audio):
    engine=pys.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',200)
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<=18:
        speak("good afternoon")
    elif hour>18 and hour<=19:
        speak("good evening")
    else:
        speak("good night sir")    

    speak("I am jarvis sir. Please tell me how can I help you?")
   
def takeCommand():

    r= sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio= r.listen(source)

    try:
        print("recognizing....")
        text= r.recognize_google(audio)
        query=r.recognize_google(audio,language='en-in')

    except:
        print("sorry sir")
        return 'none'
    return query

if __name__=="__main__":
    greet()
    msg= takeCommand() 
    print(msg)   