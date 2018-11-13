import speech_recognition as sr
recording = sr.Recognizer()

with sr.Microphone() as source:
    recording.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = recording.listen(source)
try:
   print("You said: \n" + recording.recognize_google(audio))
except sr.UnknownValueError as e:
   print(e)