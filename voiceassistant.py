import speech_recognition as sr
import os
import re
import webbrowser


def speak(text):
    for line in text.splitlines():
        os.system(" say "+text)
speak('say edit')
print("Say Edit")

def command(cmd,name):
    if('shutdown' in cmd):
        speak(name+'Do you really shutdown your laptop Yes or No')
        while(True):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio).lower()
                    if(text == 'yes'):
                        os.system("shutdown /s /t 1")
                    else:
                        exit()    
                except sr.UnknownValueError:
                    continue

    if(('.com' in cmd or 'dot com' in cmd or 'com' in cmd) and 'open' in cmd):
        s=''
        a=[]
        for i in cmd.split():
            a.append(i)
        for i in range(len(a)):
            if(a[i]=='com' or a[i]=='.com'):
                if(a[i-1]!='dot' or a[i-1]!='.'):
                    s = 'www.'+a[i-1]+'.com' 
                else:
                    s = 'www.'+a[i-2]+'.com'
        speak('ok'+name)
        webbrowser.open(s)            



    if('youtube' in cmd):
        if('open youtube' in cmd):
            speak('ok'+name)
            url = 'www.youtube.com'
            webbrowser.open(url)
        else:
            s=''
            for i in cmd.split():
                if(i == 'youtube' or i == 'search'):
                    break
                s = s+' '+i
            search = '+'.join(s.split())
            speak('Ok'+name)
            url = "https://www.youtube.com/results?search_query="
            webbrowser.open(url+search)

    if('google' in cmd):
        if('open google' in cmd):
            speak('Ok'+name)
            url = "https://google.com"
            webbrowser.open(url)
        else:
            s = ''
            for i in cmd.split():
                if(i == 'google' or i == 'search'):
                    break
                s = s+' '+i
            search = '+'.join(s.split())
            speak('Ok'+name)
            url = "https://google.com/search?q="
            webbrowser.open(url+search)

    if('open new tab' in cmd or 'new tab' in cmd):
        webbrowser.open_new_tab("chrome://newtab")

    if('open whatsapp' in cmd):
        webbrowser.open("https://web.whatsapp.com/")












def start(name):

    while(True):
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            print('say anything')
            try:
                cmd = r.recognize_google(audio).lower()
                if('edit' in cmd):
                    text = 'yes'+str(name)
                    speak(text)
                    speak('What can I do')
                    audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio).lower()
                        print(text)
                        command(text,name)
                    except sr.UnknownValueError:
                        continue
            except sr.UnknownValueError:
                continue
k = True

while(k):
    
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio).lower()
            if('edit' in text):
                speak("Hello")
                speak("Please Give Your Name")
                audio = r.listen(source)
                try :
                    name = r.recognize_google(audio).lower()
                    nm = name
                    if('my name is'  in name):
                        n = name.split()
                        nm = n[-1]
                    speak('Hello'+nm);    
                    start(nm)
                    k = False
                except sr.UnknownValueError:
                    continue
        except sr.UnknownValueError:
            continue            
            




                




