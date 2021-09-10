import speech_recognition as sr
import pyttsx3 as p
import webbrowser
import wikipedia
from selenium import webdriver
import datetime


engine = p.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 6 >= hour < 12:
        speak('Good Morning Rishikesh')
    elif 12 >= hour < 17:
        speak("Good Afternoon Rishikesh")
    elif 17 >= hour < 19:
        speak('Good Evening')
    elif 22>=hour or hour<6:
        speak('Good night Rishikesh')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
            print('Listening....')
            audio = r.listen(source)
            try:
                print("Recognizing....")
                query = r.recognize_google(audio,language='en-in')
                query.lower()
                print(f'user Said: {query}')
            except Exception as e:
                # print(e)
                print("Did not catch that\nSay it again")
                return None
            return query

if __name__ == "__main__":
    speak('Hi this is jarvis')
    wish_me()
    query = 'who is prime minister of india'
    if 'open google' in query:
        webbrowser.open('www.google.com')
    elif 'in wikipedia' in query:
        speak('searching wikipedia...')
        query = query.replace('in wikipedia', ' ')
        results = wikipedia.summary(query, sentences=2)
        speak(results)
        print(results)

    elif 'open youtube' in query:
        webbrowser.open('https://www.youtube.com/')
    elif 'open stack' in query:
        webbrowser.open('https://stackoverflow.com/')
    elif 'open git' in query:
        webbrowser.open('https://github.com/')
    elif "in youtube" in query:
        query = query.replace('in youtube', '')
        driver = webdriver.Chrome()
        driver.get('https://youtube.com')
        searchBar = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
        searchBar.send_keys(query)
        searchButton = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')
        searchButton.click()
    else: 
        driver = webdriver.Chrome()
        driver.get('https://www.google.com/')
        G_search = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')
        G_search.send_keys(query)
        G_button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[3]/center/input[1]')
        G_button.click()