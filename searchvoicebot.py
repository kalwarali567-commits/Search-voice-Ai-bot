import speech_recognition as sr
from selenium import webdriver

class voice:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.listenOnMic()

    def listenOnMic(self):
        while True:
            try:
                with sr.Microphone() as source:
                    audio = self.recognizer.listen(source)
                    command = self.recognizer.recognize_google(audio).lower()
                    print("You said:", command)

                    if "search" in command:
                        query = command.split("search", 1)[-1].strip()
                        driver = webdriver.Chrome()
                        driver.get(f"https://www.google.com/search?q={query.replace(' ', '+')}")

            except sr.UnknownValueError:
                pass

listener = voice()
