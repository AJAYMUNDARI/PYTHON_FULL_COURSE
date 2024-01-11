#Speech Recognition:-Speech recognition is the process of converting audio into text
#API(application programming interface):-It  is a type of software interface offering service to other pieces of code
#Python provides an API called SpeechRecognition to allow us to convert audio into text
import pyttsx3 #pyttsx3 is a text to speech conversion library in python (pip install pyttsx3)
import speech_recognition as sr #pip install speechRecognition
import datetime #Date and time are used to showing Date and Time
import wikipedia #wikipedia module helps us to get information from wikipedia or to perform wikipedia search(pip install wikipedia)
import webbrowser #webbrowser module helps to web search
import os
import smtplib #Used to send mail
#Install PyAudio ussing pip
MASTER='Moseena'

print('Initializing Jarvis')
#Set engine to Pyttsx3 which is used for text to speech in Python
#sapi5 is a Microsoft speech application platform interface 
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) #voices[1].id-->female voice,voices[0].id-->male voice

#Speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()
 

#This function will wish you as per time
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak('Good Morning'+MASTER)
    elif(hour>=12 and hour<17):
        speak('Good Afternoon'+MASTER)
    elif(hour>=17 and hour<20):
        speak('Good Evening'+MASTER)
    elif(hour>=20 and hour<24):
        speak('Good Night'+MASTER)
    speak('I am Jarvis How may I help you')

#This function will take command from the microphone
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source,phrase_time_limit=10)
    try:
        print('Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print("Say that again please")
        query=None
    return query
#This function sends email
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.startls()
    server.login('mohammedmoseena611@gmail.com','moseena611')
    server.sendmail('thrilokyapriya2002@gmail.com',to,content)
    server.close()



#Main Program starts here....
def main():
    speak('Initializing Jarvis...')  
    wishMe()
    query=takeCommand()
#Logic for executing tasks as per the query
    if query!=None:
        if 'wikipedia' in query.lower():
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        elif 'open youtube' in query.lower():
            speak("Here you go to Youtube")
            webbrowser.open("youtube.com")  
            # url='youtube.com'
            # chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" 
            # webbrowser.get(chrome_path).open(url)
        elif 'open google' in query.lower():
            speak('Here you go to Google')
            webbrowser.open("google.com")
        elif 'play song' in  query.lower():
            songs_dir='C:\\Users\\DELL\\Music'
            songs=os.listdir(songs_dir)
            print(songs)        
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif 'the time' in query.lower():
            strtime=datetime.datetime.now().strtime('%H:%M:%S')
            speak(f'{MASTER} the time is {strtime}')
        elif 'open code' in query.lower():
            codePath="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif  'email to thrilokyapriya' in query.lower():
            try:
                speak("What should I send")
                content=takeCommand()
                to='thrilokya2002@gmail.com'
                sendEmail(to,content)
                speak('Emmail has been sent successfully')
            except Exception as e:
                print(e)


main()


    
    
    








