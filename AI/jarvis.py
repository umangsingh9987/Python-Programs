# Before importing pyttsx3 and speech_recognition, we need tO install python pakages for them
# we can do so by using following command in terminal:

# pip install pyttsx3 
# pip install SpeechRecognition

# pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
# If there is error such as No module named win32com.client, No module named win32, or No module named win32api, 
# we will need to additionally install pypiwin32 for python 3 using command

# pip install pypiwin32

import pyttsx3
import speech_recognition as sr
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id) 
engine.setProperty('voice', voices[1].id)



def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good Morning!")

	elif hour>=12 and hour<18:
		speak("Good Afternoon!")

	else:
		speak("Good Evening!")

	speak("I am yashvi sir. Please tell me how may I help you")

def takeCommand():

	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"user said: {query}\n")

	except Exception as e:

		print("Say that again please...")
		return "None"
	return query

if __name__ == "__main__":
	wishMe()
	takeCommand()
	
