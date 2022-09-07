import pyttsx3
import speech_recognition as sr
engine=pyttsx3.init('sapi5')
import datetime
import wikipedia as wk
import sys
import pywhatkit as kit
import time
import webbrowser
import requests
from bs4 import BeautifulSoup 
voices = engine.getProperty('voices')
voices = engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print(voices)

def takecommand():
     r=sr.Recognizer()
     with sr.Microphone() as source:
        print("listing...")
        r.pause_threshold=1
        audio=r.listen(source)
     try:
        print("recognization...")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said:{query}")
     except Exception as e:
         speak('Sorry.. say again')
         return "none"
     return query
def wish():
     hour=int(datetime.datetime.now().hour)
     if hour >12 and hour<18:
       
        speak("good afternoon")
     
     if hour>=0 and hour<12:
        speak("goodMorning")
     if hour>=18:
        speak("good eveneing")

     speak("hi mam i am friday your virtual assistant how may i help you")
    

def Temp():
            speak("which state")
            search = "tempreture of bihar"
            url = f"https://www.google.com/search?q{search}"
            r=requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            data.find("div", class_="BNeawe").text
            speak(f"current{search}")
           

def Start():
   
   while True:
      query = takecommand().lower()
      if "what is your name" in query:
         speak("my name is friday")
      
      elif "what can you do for me" in query:
         speak("i can do for you searching wikipedia sending whatsapp message open youtube open google and send email")
      

      elif "open youtube" in query:
         speak("what should i search for you")
         y=takecommand().lower()
         speak("ok mam")
         time.sleep(1)
         kit.playonyt(f'{y}')

         if "just open" in y:

            webbrowser.open("www.youtube.com")

      elif "temperature" in query:
        speak("where?")
        miejsce=takecommand().lower()
        search = (f"Temperature in  {miejsce}")
        url = (f'https://www.google.com/search?q={search}')
        r = requests.get(url)
        data = BeautifulSoup(r.text , "html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak(f"In {search} there is {temp}")
         


      elif "send a message" in query:
         speak("please tell me number")
         cm = int(input())
         speak("what should i say")
         g=takecommand().lower()
         speak("tell me time")
         Ti=input()
         speak("tell me Minute")
         mi=input()
         kit.sendwhatmsg("+91"+cm,f"{g}",Ti,mi)

     


      elif "no thanks" in query:
         speak("ok i hope you enjoying me.... by")
         break

      elif "wikipedia" in query:
         speak("searching wikipedia...")
         query = query.replace("wikipedia","")
         result = wk.summary(query,sentences=2)
         speak(result)
         print(result)
      
      
      
      speak("do you have other work mam")

      

        

   

if __name__=="__main__":
 while True:
    permissin = takecommand().lower()
   

    if permissin in "hello friday" or permissin in "hello Friday":
      
        wish()
        Start()
        
    if permissin in "good" and permissin in "good and you":
        speak("ok lets code and i am good")
    elif "by now you can sleep" in permissin:
      speak("ok mam if you have work then you will wake up me")
      break

