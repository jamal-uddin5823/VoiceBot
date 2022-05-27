import enum
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import pyaudio
import keyboard
from time import sleep

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):

    engine.say(text)
    engine.runAndWait()


def initialize():
    # talk("hello, what should my name be?  ")
    # name = input("what should my name be?  ")
    talk(f"Hello, I am your assistant. How may i be of your help? Ask me what can I do in case you do not know. Press q to ask. ")


def listen():
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source, duration=1)
        print("Press 'q' to ask something")
        while True:
            if keyboard.is_pressed('q'):
                print('Listening....')
                listener.pause_threshold = 1
                audio = listener.listen(source)
                command = ''
                break

        try:
            print("Recognizing....")
            command = listener.recognize_google(audio)
            print(command)

        except:
            print("Sorry, I didn't understand")
            talk("Sorry, I didn't understand")

    return command.lower()


def time_tell():
    time = datetime.datetime.now().strftime('%I:%M')
    return "The time now is "+time


def play(comm):
    try:
        print("Playing...")
        talk("Playing"+comm.replace('play', ''))
        pywhatkit.playonyt(comm)

    except:
        print("Network Error Occured")


def joke():
    joke = pyjokes.get_joke()
    return joke


def date():
    talk("I would love to.")


def search(comm):
    topic = comm.replace('search', '')
    print(wikipedia.summary(topic, 2))
    talk(wikipedia.summary(topic, 1))


if __name__ == "__main__":
    initialize()
    while True:
        command = listen()
        
        if 'what can you do' in command:
            command = "I can tell you the current time, play youtube videos, tell a joke, search anything for you"
            li = command.split(",")
            for i,j in enumerate(li,1):
                print(i,j,sep=". ")
            talk(command)

        elif 'time' in command:
            talk(time_tell())

        elif 'play' in command:
            play(command)

        elif 'joke' in command:
            joke_1 = joke()
            print(joke_1)
            talk(joke_1)
        elif 'date' in command:
            date()

        elif 'search' in command:
            search(command)

        elif "stop" in command:
            talk("Ok, Logging out")
            break

        elif 'how are you' in command:
            talk("I am fine. thanks for asking.")

        else:
            talk("Sorry for the inconvinience. Should I search it for you?")
            print("yes or no?")
            permission = listen().lower()
            if 'yes' in permission:
                pywhatkit.search(command)
                sleep(5)
            # talk(command)
