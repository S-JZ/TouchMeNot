
def speak(msg: str):
    import speech_recognition as sr
    import os
    import pyttsx3
    
    
    
    engine = pyttsx3.init()
    # initialize Text-to-speech engine
    engine.say(msg)
    # play the speech
    engine.runAndWait()


def phone_number(r, source):
    
    msg = "Hello, please tell me your Phone Number to proceed further."
    speak(msg)
    phone_data = r.record(source, duration=9)
    phone = r.recognize_google(phone_data)
    speak("Is your phone number: " + phone)
    phone = "".join(phone.split())
    speak("Please say Yes to continue otherwise say No")
    return phone


def initialize_project(init=True):
    import speech_recognition as sr
    import os
    import pyttsx3
  
    r = sr.Recognizer()
    engine = pyttsx3.init()
    if init:
        msg = "Welcome to Touch Me Not. What would you like to explore? Virtual Doodle, Classroom or Self Checkout? "
        speak(msg)
    init = False
    try:
        with sr.Microphone() as source:
            audio_data = r.record(source, duration=2)
            command = r.recognize_google(audio_data)
            if "".join(command.lower().split()) == "virtualdoodle":
                msg = "Virtual Doodle has been activated."
                speak(msg)
                return "lvdl"
            elif "".join(command.lower().split()) == "classroom":
                msg = "Virtual Classroom has been activated."
                speak(msg)
                return "cls"
            elif "".join(command.lower().split()) == "checkout":
                phone = phone_number(r, source)
                confirm_data = r.record(source, duration=2)
                confirm = r.recognize_google(confirm_data)
                print(confirm)
                if "".join(confirm.lower().split()) == "yes":
                    return "chk", phone
                else:
                    phone = phone_number(r, source)
            elif "".join(command.lower().split()) == "exit":
                msg = "Bye. See you later."
                speak(msg)
            else:
                msg = "I am sorry but " + command + \
                    " is not a valid command. If you wish to exit, please say Exit."
                speak(msg)
                return initialize_project(init)
    except:
        msg = "I am sorry I didn't get that. If you wish to exit, please say Exit."
        speak(msg)
        return initialize_project(init)


def launch_project(url):
    import speech_recognition as sr
    import os
    import pyttsx3
   
    

    options = {'cls': 'Virtual Classroom',
               'chk': 'Self Checkout', 'lvdl': 'Virtual Doodle'}
    r = sr.Recognizer()
    engine = pyttsx3.init()
    msg = "Say launch to launch the " + options[url]
    speak(msg)
    try:
        with sr.Microphone() as source:
            # read the audio data from the default microphone
            audio_data = r.record(source, duration=5)
            print("Recognizing...")
            # convert speech to text
            text = r.recognize_google(audio_data)
            if "".join(text.lower().split()) == "launch":
                return url
            elif "".join(text.lower().split()) == "exit":
                msg = "Bye. See you later."
                speak(msg)
                return None
            else:
                msg = "I am sorry but " + text + \
                    " is not a valid command. If you wish to exit, please say Exit."
                speak(msg)
    except:
        msg = "I am sory I didn't get that. If you wish to exit, please say Exit."
        speak(msg)
        launch_project(url)


# print(initialize_project())
