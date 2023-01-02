import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

from bs4 import BeautifulSoup
#web=webbrowser.get("D:\Google\Chrome\Application\chrome.exe")
#import vlc
#import pafy
import speech_recognition as s_r
import pyautogui  # for screenshot
import requests
import json
import google
from googlesearch import search
import datefinder
import winsound
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from selenium import webdriver
chromedriver_location ="chromedriver"
#driver = webdriver.Chrome(chromedriver_location)
# install webdriver for required browser to use selenium
#from selenium import webdriver

# Microsoft speech Api - sapi5
engine = pyttsx3.init()
# getproperty is use to get the total number of voice available in your system
voices = engine.getProperty('voices')
# set property is use to set the voice of our assistant
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# For Greeting purpose
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour <= 12:
        speak(" Good morning sir")
    elif hour >= 12 and hour <= 18:
        speak(" Good evening sir")
    else:
        speak("Good night sir")



# takecommand takes input from user and return it in string form

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("SPEAK...")
        speak(" Welcome back sir ")
        audio = r.listen(source)
        speak("Okay")

    try:
        query = r.recognize_google(
            audio, language='en-IN', )

        print(query)
    except Exception as e:
        print("Sorry Sir")
        return "None"
    return query


def sendemail(to, content):
    speak("do you want me to take screenshot and send it via email")
    print("do you want me take screenshot ")
    c = takecommand().lower()
    if "yes" in c or "ok" in c:
        msg= MIMEMultipart()
        msg['From']="hritik162001@gmail.com"
        msg['To']= to
        msg['Subject']=" NO subject"
        body=content
        msg.attach(MIMEText(body,'plain'))
        filen="screenshot.png"
        screens=open("screenshot/screenshot.png","rb")
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload((screens).read())

        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filen)

        # attach the instance 'p' to instance 'msg'
        msg.attach(p)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        # Authentication
        s.login('hritik162001@gmail.com', '7905776327')

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail('hritik162001@gmail.com', to, text)

        # terminating the session
        s.quit()
        speak("Sir, email has been sent")
    else:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('hritik162001@gmail.com', '7905776327')
        server.sendmail('hritik162001@gmail.com', to, content)
        server.close()
        speak("Sir, email has been sent")


def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0


# Function to perform arithmetic
# operations.
def applyOp(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a // b


# Function that returns value of
# expression after evaluation.
def evaluate(tokens):
    # stack to store integer values.
    values = []

    # stack to store operators.
    ops = []
    i = 0

    while i < len(tokens):

        # Current token is a whitespace,
        # skip it.
        if tokens[i] == ' ':
            i += 1
            continue

        # Current token is an opening
        # brace, push it to 'ops'
        elif tokens[i] == '(':
            ops.append(tokens[i])

        # Current token is a number, push
        # it to stack for numbers.
        elif tokens[i].isdigit():
            val = 0

            # There may be more than one
            # digits in the number.
            while (i < len(tokens) and
                   tokens[i].isdigit()):
                val = (val * 10) + int(tokens[i])
                i += 1

            values.append(val)


            i -= 1

        # Closing brace encountered,
        # solve entire brace.
        elif tokens[i] == ')':

            while len(ops) != 0 and ops[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()

                values.append(applyOp(val1, val2, op))

            # pop opening brace.
            ops.pop()

        # Current token is an operator.
        else:
            while (len(ops) != 0 and
                   precedence(ops[-1]) >=
                   precedence(tokens[i])):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()

                values.append(applyOp(val1, val2, op))


            ops.append(tokens[i])

        i += 1

    while len(ops) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()

        values.append(applyOp(val1, val2, op))

    # Top of 'values' contains result,
    # return it.
    return values[-1]


def climate():
    api_key = "59cc930d8aa7ab65247dd1da87838983"  # pass-7905776326 email - hritik162001@gmail.com
    base = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Renukoot"
    compelete = base + 'appid=' + api_key + "&q=" + city
    response = requests.get(compelete)
    x = response.json()
    if x["cod"] != '404':
        y = x['main']
        temp = int(y['temp'] - 273)
        z = x['weather']
        weather_d = z[0]['description']
        speak("Here is the quick whether report..")
        speak(" Outside Temperature is " + str(temp) + "celsius" + "\n weather is " + str(weather_d))
    else:
        print("city not found")

if __name__ == "__main__":


    wishme()

    climate()
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.dynamic_energy_threshold = True
        r.pause_threshold = 1
        speak("setting up mic")
        r.adjust_for_ambient_noise(source, duration=1)
    count = 0



    while True:
        # query is conv in lower case so that if statement doesn't treat capital and lower case query in a different manner

      query = takecommand().lower()
      def fri(query):
        if "stop friday" in query or "stop" in query:
            speak(" Thank you sir ")
            qu="friday"
            while "friday" in qu:
                r = sr.Recognizer()
                with sr.Microphone(device_index=1) as source:
                    audio = r.listen(source)
                    try:
                        qu = r.recognize_google(audio, language='en-IN', )
                    except Exception as e:
                        print(" pls call me when you need any help")
            fri(qu)

        if 'search' in query:
            speak("Please wait i am searching...")
            query = query.replace("wikipedia", "")
            query = query.replace("friday", "")
            query = query.replace("search", "")
            speak("Results are ")
            for j in search(query, tld="co.in", num=1, stop=1):
                webbrowser.open(str(j))
        elif "instagram" in query:
            driver = webdriver.Chrome(chromedriver_location)
            driver.get('https://www.instagram.com/')
            driver.implicitly_wait(10)
            first_l = "//*[@id=\"react-root\"]/section/main/article/div[2]/div[2]/div/p/a/span"
            login = "//*[@id=\"loginForm\"]/div/div[3]"
            username_input = "//*[@id=\"loginForm\"]/div/div[1]/div/label/input"
            password = "//*[@id=\"loginForm\"]/div/div[2]/div/label/input"
            driver.find_element_by_xpath(username_input).send_keys("hritik162001@gmail.com")
            driver.find_element_by_xpath(password).send_keys("12hritik")
            driver.find_element_by_xpath(login).click()
            speak("SIR do you want me to save your username and password")
            com=takecommand()
            if "yes" in com:
                save="//*[@id=\"react-root\"]/section/main/div/div/div/section/div/button"
                driver.find_element_by_xpath(save).click()
            else:
                nosave="//*[@id=\"react-root\"]/section/main/div/div/div/div/button"
                driver.find_element_by_xpath(nosave).click()
            speak("sir ")
            com=takecommand()
            if("yes") in com:
                on="/html/body/div[4]/div/div/div/div[3]/button[1]"
                driver.find_element_by_xpath(on).click()
            else:
                of="/html/body/div[4]/div/div/div/div[3]/button[2]"
                driver.find_element_by_xpath(of).click()
        elif "alarm" in query:
            if "after" in query:
                if "minutes" in query or "minute" in query:
                    a= ''.join(i for i in query if i.isdigit())
                    if(len(a)==0):
                            speak("sir After how many minutes")
                            query = takecommand().lower()
                            a = ''.join(i for i in query if i.isdigit())
                    min = datetime.datetime.now().minute + int(a)
                    hour=datetime.datetime.now().hour
                    speak("SIR your alarm is set")
                    if(min>60):
                        hour = datetime.datetime.now().hour+1
                        min=min-60
                    while True:
                        print(datetime.datetime.now().minute)
                        if hour == str(datetime.datetime.now().hour):
                            if min == (datetime.datetime.now().minute):
                                print('ALARM..WAKE UP')
                                winsound.PlaySound('C:\\Users\\Hritik\\Music\\alarmr.wav', winsound.SND_LOOP)
                            elif min > (datetime.datetime.now().minute):
                                break
                elif "hour" in query:
                    a = ''.join(i for i in query if i.isdigit())
                    if (len(a) == 0):
                        speak("sir After how many hour")
                        query = takecommand().lower()
                        a = ''.join(i for i in query if i.isdigit())
                    hour = datetime.datetime.now().hour + int(a)
                    min = datetime.datetime.now().minute
                    speak("SIR your alarm is set")
                    while True:
                        if hour == (datetime.datetime.now().hour):
                            if min == str(datetime.datetime.now().minute):
                                print('ALARM..WAKE UP')
                                winsound.PlaySound('C:\\Users\\Hritik\\Music\\alarmr.wav', winsound.SND_LOOP)
                            elif min > str(datetime.datetime.now().minute):
                                break
            else:
                while (1):
                    datetimea = datefinder.find_dates(query)
                    for match in datetimea:
                        print(match)
                    sa = str(match)
                    time = sa[11:]
                    hour = time[0:2]

                    if time[3] == '0':
                        min = time[4]
                    else:
                        min = time[3:5]
                    '''print(min)
                    print(hour)
                    print(datetime.datetime.now().minute)
                    print(datetime.datetime.now().hour)'''
                    speak("SIR your alarm is set")
                    while True:
                        if hour == str(datetime.datetime.now().hour):
                            if min == str(datetime.datetime.now().minute):
                                print('ALARM..WAKE UP')
                                winsound.PlaySound('C:\\Users\\Hritik\\Music\\alarmr.wav', winsound.SND_LOOP)
                            elif min > str(datetime.datetime.now().minute):
                                break
        elif "meaning" in query:
            query = query.replace("what", " ")
            query = query.replace("friday", "")
            query = query.replace("is", " ")
            query = query.replace("the", " ")
            query = query.replace("of", " ")
            speak("Results are ")
            #q=search(query,tld="co.in",num=1,stop=1)
            for j in search(query,tld="co.in",num=1,stop=1):
                webbrowser.open(str(j))
        elif "song" in query or "play" in query:
            query = query.replace("play", "")
            query = query.replace("friday", "")
            query = query.replace("any", "")
            query = query.replace("is", "")
            query = query.replace("some", "")
            speak("Searching your song on youtube")
            for j in search(query, tld="co.in", num=1, stop=1):
                webbrowser.open(str(j))
        elif "calculate" in query:
            a=query.replace("calculate", "")
            a= query.replace("friday", "")
            print(len(a))
            if(len(a)==0):
                speak("please write the expresssion for calculation")
                a=str(input())
            print(evaluate(a))
        elif "amazon" in query:
            webbrowser.open_new("Amazon.in")
        elif "flipkart" in query:
            webbrowser.open("Flipkart.in")
        elif "youtube" in query:
            webbrowser.open("youtube.in")
        elif "time" in query:
            strtime = datetime.datetime.now().strftime( "%H: %M: %S")
            speak(f"Sir the time is {strtime}")
        elif "open code" in query:
            codepath = "C:\\Users\\Hritik\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

            # Here email is sent to hritik only
        elif "send " in query or "email" in query:
            try:
                to=query.split('to')
                to=to[1].lower()
                if "divyam" in to:
                    to= "divyampal12013@gmail.com"
                elif "me" in to:
                    to="hritik162001@gmail.com"
                else:
                    speek("Sir where you want me to send this email ")
                    to=input("\nENTER SENDER EMAIL:")
                speak("what do you want me to send ")
                content=takecommand()
                sendemail(to, content)
            except Exception as e:
                speak("Sir where you want me to send this email ")
                to=input("\nENTER SENDER EMAIL:")
                speak("what do you want me to send ")
                content=takecommand()
                sendemail(to, content)
                #speak("Sorry there is some error in sending email")

        #elif "calculate" in query:
         #   calculator()

        elif "screenshot" in query:
            screenshot = pyautogui.screenshot("screenshot.png")
            screenshot.save(r"D:\PyCharm\\JARVIS\\venv\\screenshot")
        else:
            speak("Sir please say it loudly")
            '''   c=takecommand().lower()
            if "no" in c or "ok" in c:
                speak("Thank you sir")
                exit(0)'''
      fri(query)