from tkinter import *
from PIL import ImageTk,Image
import pyttsx3
import speech_recognition
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit as kit
import sys
import pyjokes
import psutil
import requests
import pyautogui
#import speedtest
from bs4 import BeautifulSoup
from requests import get
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

root=Tk()
root.title('Yololuna')
root.geometry('1280x720')
#img=ImageTk.PhotoImage(Image.open(r"/Users/dipaghosh/Downloads/robot2.png"))
pantext=""

panel=Label(root, text="")
panel.config(text=pantext)
#panel.pack(side='right', fill='none', expand='no')
compText=StringVar()
userText=StringVar()
userText.set("START")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    #tt=datetime.strf("%I:%M %p")
    if hour>=5 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    elif hour>=0 and hour<5:
        speak("Go! and sleep now!")
    else:
        speak("Good Evening!")
    speak("I am yololuna, Mandira's assistant. I was born on 28th november, 2021. Sounds Awesome, right? How may i help you?")
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


"""def butfunc():
    wishMe()
    command=takeCommand()
    #root.mainloop()

    

    
myButton= Button(root, text="start", padx=50, pady=50, command=butfunc, fg="blue", bg="yellow" )
#button_quit = Button(root, text="bye",command=root )
#button_quit.pack()
userFrame=LabelFrame(root,text="User", font=('Black ops one',10, 'bold' ))
userFrame.pack(fill='both', expand='yes')

myButton.pack()
root.mainloop()"""






"""
def run(self):
    speak("say wakeup to continue")
    while True:
        self.query=self.takecommand()
        if "wakeup" in self.query or "are you there" in self.query or "hello" in self.query:
            self.TaskExecution()"""





if __name__ == "__main__":

    def butfunc():
        wishMe()
        command = takeCommand()


    myButton = Button(root, text="start", padx=50, pady=50, command=butfunc, fg="blue", bg="yellow")
    # button_quit = Button(root, text="bye",command=root )
    # button_quit.pack()
    userFrame = LabelFrame(root, text="User", font=('Black ops one', 10, 'bold'))
    userFrame.pack(fill='both', expand='yes')

    myButton.pack()
    root.mainloop()




    #print("hello")
    wishMe()
    while True:

        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia .... Please wait!")
                #query = query.replace("wikipedia","")
            results = wikipedia.summary(query)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'current location' in query or 'where am i' in query:
            speak("wait, let me check..")

            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"I think we are current in {city} city of {country} country")
                
            except Exception as e:
                speak("sorry, due to network issues , i cannot find out where we are right now!")
                pass


        elif 'open youtube' in query:
            speak("What should i search in youtube?")
            cm = takeCommand().lower()
            webbrowser.open(f"https://youtube.com/search?q={cm}")


        elif 'open whatsapp' in query:
            #speak("What should i search in youtube?")
            #cm = takeCommand().lower()
            webbrowser.open("https://web.whatsapp.com")


        elif 'open discord' in query:
            #speak("What should i search in youtube?")
            #cm = takeCommand().lower()
            webbrowser.open("https://discord.com")


        elif 'open google' in query:
            speak("What should i search in google?")
            cm = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={cm}")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")


        elif 'how are you' in query:
            speak("I am fine! Mandira keeps me happy always. how are you?")


        elif 'hi' in query or 'name' in query:
            speak("Hello! My name is Yololuna. Nice to meet you!")


        elif 'love' in query:
            speak("sorry, i dont love anyone other than mandira. She is my creator. I obey her. ")


        elif 'take screenshot' in query or 'take a screenshot' in query:
            speak("please tell me with which name you want to save the screenshot ")
            name=takeCommand().lower()
            speak("please hold the screen for a moment. I am taking the screenshot.")
            #time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done with the screenshot. now, i am ready for the next command!")

        elif 'the date' in query:
            strDate = datetime.datetime.now().strfdate("%DD:%M:%YYYY")
            speak(f"The date is {strDate}")
            #elif 'open terminal' in query:
             #   os.system("python cmd")


        elif 'open spotify' in query:
            webbrowser.open('https://spotify.com')


        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")
            print(f"Your IP address is {ip}")
            #elif 'send message' in query:
                #speak("Whom should i send message in whatsapp?")
                #cm1 = takeCommand().lower()
                #speak("What should i send in whatsapp?")
                #cm2 = takeCommand().lower()
                #kit.sendwhatmsg("+91 9322337670" , "hello baba filled the hostel form" , '1125')


        elif 'play songs' in query:
            speak("Which song should i play?")
            pyt = takeCommand().lower()
            kit.playonyt(f"{pyt}")


        elif 'no thanks' in query:
             speak("Thanks for using me! Have an awesome day!")
             sys.exit()


        elif 'tell me a joke' in query:
             joke = pyjokes.get_joke()
             speak(joke)


        elif 'battery' in query:
            battery = psutil.sensors_battery()
            percentage=battery.percent
            speak(f"Mandiras mac book pro has {percentage} percent battery")

            if percentage>75:
                speak("Your mac book pro has enough power !  dont worry ! continue your work")

            elif percentage>40 and percentage<=75:
                speak("Its preferable to connect your mac book pro to the charging point")

            elif percentage>15 and percentage<=40:
                speak("Connect your mac book pro to the charging point right now!")

            elif percentage>0 and percentage<=15:
                speak("stop your work! your mac book pro will die now ! rather, save your work!")


        elif 'shut down the system' in query:
            os.system("shutdown /s /t 5")


        elif 'restart the system' in query:
            os.system("restart /r /t 5")


        elif 'send message on whatsapp' in query:
            kit.sendwhatmsg("+918828256857","Hello, message from mandira's assistant",19,35)
        #elif 'internet speed' in query:
            #import speedtest
            #st = speedtest.Speedtest()
            #d1 = st.download()
           # up = st.upload()

            #speak("Mandiras mac book pro is having {d1} bit per second downloading speed and {up} bit per second uploading speed")
        elif 'activate how to do mode' in query:
            from pywikihow import search_wikihow
            speak("how to mode has been activated.?")
            while True:
                   speak("please tell me what do you want to know?")
                   how= takeCommand()
                   try:
                      if "exit" in how or "close" in how:
                          speak("how to do mode has been deactivated")
                          break

                      else:
                         maxresults=1
                         how_to= search_wikihow(how, maxresults)
                         assert len(how_to)==1
                         how_to[0].print()
                         speak(how_to[0].summary)
                   except Exception as e:
                      speak("sorry, i am not able to find this.")


        elif 'weather forecast' in query:
             speak("tell me the name of the place whose temperature you want.")
             cm = takeCommand().lower()
             search= f"Temperature in {cm}"
             url= f"https://www.google.com/search?q={search}"
             r=requests.get(url)
             data = BeautifulSoup(r.text,"html.parser")
             temp = data.find("div" ,class_="BNeawe").text
             speak(f"current {search} is {temp}")



        speak("Do you have any other work?")
        root.mainloop()

        #greet
        #wikipedia
        #open youtube
        #open whatsapp
        #open discord
        #open google
        #the ime
        #how are you
        #hi / name?
        #love
        #take screenshot/ take a screenshot
        #the date
        #open spotify
        #ip address
        #play songs
        #tell me a joke
        #battery
        #shut down
        #restart
        #send message on whatsapp
        #activate how to do mode
        #weather forecast
        #no thanks









