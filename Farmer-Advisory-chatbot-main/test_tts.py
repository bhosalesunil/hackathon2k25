import pyttsx3

# Initialize engine
engine = pyttsx3.init()

# Set voice properties (optional)
engine.setProperty("rate", 150)   # Speed %
engine.setProperty("volume", 0.9) # Volume (0.0 to 1.0)

# Speak
engine.say("Hello Farmer! Your advisory chatbot is working.")
engine.runAndWait()
