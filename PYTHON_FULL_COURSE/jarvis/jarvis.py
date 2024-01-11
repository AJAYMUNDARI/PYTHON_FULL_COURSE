import pyttsx3  #NEED TO INSTALL,text to speech converter library
import speech_recognition as sr #pip install speechRecognition
import datetime #NO NEED TO INSTALL, built-in func
import wikipedia
import webbrowser
import os
import smtplib

engine= pyttsx3.init('sapi5') #used for voice input
voices= engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)



def speak(audio):      #important because we hv to speak , text to audio converter
    engine.say(audio) #audio string will speak by engine9
    engine.runAndWait() #it will run the function

def wishMe():
    hour= int(datetime.datetime.now().hour)     #hour will give time from 0 to 24 hr,now() system time
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Please tell me how may i help you")

def takeCommand():  #it takes microphone input from user and returns string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1 #for noice cancelation we can increase the threshold
        r.adjust_for_ambient_noise(source)
        #audio=r.listen(source,phrase_time_limit=10)
        audio=r.listen(source,phrase_time_limit=10)

    try:            ##when there is chances of error
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ajaymundari1929@gmail.com','hjghff')
    server.sendmail('ajaymundari1005@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()        # speak("Ajay is a lover boy") #call the speak func
    while True:
    #if 1:
        query= takeCommand().lower()    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query= query.replace("wikipedia","")
            result= wikipedia.summary(query,sentences=2)
            speak("wikipedia")
            print(result)
            speak(result)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\91907\\Music'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"SIR, the time is {strtime}")
        #elif 'open code' in query.lower():
        # codePath="C:\Users\91907\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
        # os.startfile(codePath)
        elif  'email to ajay' in query.lower():
            try:
                speak("What should I send")
                content=takeCommand()
                to='ajaymundari1005@gmail.com'
                sendEmail(to,content)
                speak('Emmail has been sent successfully')
            except Exception as e:
                print(e)
        elif 'bye' in query.lower():
            break