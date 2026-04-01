import speech_recognition as sr
import webbrowser
import pyttsx3

#pip install speechrecognition pyaudio
#pip install setuptools
#pip install pyttsx3
#pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text): 
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open facebook" in c.lower():
          webbrowser.open("http://facebook.com")
    elif "open youtube" in c.lower():
          webbrowser.open("http://youtube.com")           
    elif "open linkedin" in c.lower():
          webbrowser.open("http://linkedin.com")
    elif "open chatgpt" in c.lower():
          webbrowser.open("http://chatgpt.com")

if __name__ == "__main__":
    speak("Initializing jarvis... ")
    while True:
        #Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        

           
        print("recognizing...")
        # recognize speech using Google
        try:
            with sr.Microphone() as source:
                print("Listening!")
                audio = r.listen(source,timeout=10)
            word = r.recognize_google(audio)
            if "hello" in word:
                print("Jarvis Activated!")
                speak("How can I help you?")
                #Listen for command
            with sr.Microphone() as source:
                    print("Jarvis Active!")
                    audio = r.listen(source, timeout=5, phrase_time_limit=3)
                    command = r.recognize_google(audio).lower()
                    process_command(command)

        
        except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")
    
    