import pyaudio
print(pyaudio.__version__)


import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Say something...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("✅ You said:", text)
except sr.UnknownValueError:
    print("❌ Could not understand audio")
except sr.RequestError as e:
    print(f"⚠️ Could not request results; {e}")
