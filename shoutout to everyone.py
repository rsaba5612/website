import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set the voice to use for the speech
# You can find available voices using `engine.getProperty('voices')`
voice = engine.getProperty('voices')[0]
engine.setProperty('voice', voice.id)

# Set the speed of the speech
engine.setProperty('rate', 150)

# Set the text to be spoken
text = "Hello, how are you?"

# Speak the text
engine.say(text)
engine.runAndWait()
