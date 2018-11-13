import speech_recognition as sr
import webbrowser
import pyttsx3


recording = sr.Recognizer()

with sr.Microphone() as source:
    recording.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = recording.listen(source)

if recording.recognize_google(audio) == "open browser":
    engine = pyttsx3.init()
    engine.say("Yes Boss")
    engine.runAndWait()
    url = 'http://www.python.org/'

    webbrowser.open(url)