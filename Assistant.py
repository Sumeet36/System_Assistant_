import pyttsx3
import os

pyttsx3.speak("Hello User!")
pyttsx3.speak("This is Nova, your personal system assistant, How may I help you?")


while True:
    p = input("chat with me with your requirements : ")

    if ((("run" in p) or ("open" in p )) and ("chrome" in p)) :
        pyttsx3.speak("Opening Chrome")
        os.system("chrome")

    elif (("run" in p) or  ("open" in p )) and (("notepad" in p) or ("editor" in p) ) :
        pyttsx3.speak("Opening Notepad")
        os.system("notepad")

    elif ('facebook' in p):
        pyttsx3.speak('opening facebook')
        os.system('start  http://www.facebook.com/')

    elif ('notepad++' in p) or ('pad editor' in p):
        pyttsx3.speak('Launching your notepad++')
        os.system('notepad++')

    elif (("run" in p) or  ("open" in p ))  and ("player" in p) and ("media" in p) :
        pyttsx3.speak("Opening Media Player")
        os.system("wmplayer")
    
    elif ('youtube' in p):
        pyttsx3.speak('opening youtube')
        os.system('start  http://www.youtube.com/')

    elif ('prompt' in p) or ('command' in p) or ('cmd' in p):
            pyttsx3.speak('opening your command prompt')
            os.system('start cmd.exe')
    
    elif ("exit" in p)  or ("quit" in p):
        pyttsx3.speak("Happy to help you. See you around")
        break

    else:
        pyttsx3.speak("not supported, Please try again!")