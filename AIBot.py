# Python program to translate
# speech to text and text to speech


from random import random
from gtts import gTTS
import speech_recognition as sr
import pyttsx3
import openai
import playsound
import os
from googletrans import Translator


# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
openai.api_key = "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"
model = "text-davinci-003"
translator = Translator()

def speak(audio_string): 
    tts = gTTS(text=audio_string, lang='ur') # text to speech(voice)
    audio_file = 'audio-' + str() + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    # print(audio_string) # print what app said
    os.remove(audio_file) # remove audio file

# def SpeakText(command):

#     # # Initialize the engine
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)
#     engine.say(command)
#     engine.runAndWait()
#     engine = pyttsx3.init()


# Loop infinitely for user to
# speak
def getResponse(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        temperature=0.9,
    )
    return response.choices[0].text
# print(response.choices[0].text)
# SpeakText(response.choices[0].text)

while (1):

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            print("Say Something")
            r.adjust_for_ambient_noise(source, duration=0.5)

            # listens for the user's input
            audio2 = r.listen(source)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            eng = translator.translate(MyText, dest='en')
            
            # translator = Translator()
            lan=translator.detect(MyText)
            if lan.lang=='ur' or lan.lang=='hi':
                speak(MyText)
                # urdu = translator.translate(MyText, dest='ur')
                # speak(urdu.text)
                # eng = translator.translate(MyText, dest='en')
                print(eng.text)
                # speak("\n"+getResponse(eng.text)+"\n")
                aiAns = getResponse(eng.text)
                print(aiAns)
                urduAns = translator.translate(aiAns, dest='ur')
                speak(urduAns.text)
            else:
                speak(MyText)
                # print(MyText)
                speak("\n"+getResponse(MyText)+"\n")

            # print("\n"+MyText)
            # # SpeakText(MyText)
            # print("\n"+getResponse(MyText)+"\n")
            # # speak(getResponse(MyText))
            # # text=getResponse(MyText)
            # speak(getResponse(MyText))

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
