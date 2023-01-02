from tkinter import *
import tensorflow as tf
import json
import os
import wikipedia
import re
from bs4 import BeautifulSoup
import requests
from googlesearch import search
root = Tk()
root.title("CHATBOT")
root.iconbitmap(r'C:\Users\Hritik\AppData\Roaming\JetBrains\PyCharmCE2020.2\scratches\C.ICO')
root.maxsize(530,652)

frame1= LabelFrame(bd=0,bg="black",fg="blue")
rules=Label(frame1,text = "Rules: ",bd=3, relief=  "raised",bg ='firebrick3',fg= 'white',font = ("Times",16,"bold"),anchor='nw')
#rules.config(highlightcolor="white")
rule1=Label(frame1,text="1. Be specific to ur query.",bd=3, relief=  "raised",bg ='firebrick3',fg= 'white',font = ("Times",12,"bold"),anchor='nw')
rule2=Label(frame1,text="2. Use speech assistant to:",bd=3, relief=  "raised",bg ='firebrick3',fg= 'white',font = ("Times",12,"bold"),anchor='nw')

rule21=Label(frame1,text="a. Send email. ",bd=3, relief= "raised",bg ='firebrick3',fg= 'white',font = ("Times",12,"bold"),anchor='w')

rule22=Label(frame1,text="b. Set alarm ....personal stuff.",bd=3, relief=  "raised",bg ='firebrick3',fg= 'white',font = ("Times",12,"bold"),anchor='nw')
rule23=Label(frame1,text="c. Voice search ",bd=3, relief=  "raised",bg ='firebrick3',fg= 'white',font = ("Times",12,"bold"),anchor='w')

rule3=Label(frame1,text="3.For queries use chatbot.",bd=3, relief= "raised",bg ='firebrick3',fg= 'white',font = ("Times",12,"bold"),anchor='nw')

frame2= LabelFrame(bd=8,relief="raised",bg="black")
frame3= LabelFrame(bd=0,bg="black")

inputm = Entry(frame3,bg ='firebrick3',relief="groove",bd=5,fg="white")
inputm.insert(0, "Enter your msg " )

def sendmsg():
    user.delete(0,END)
    user.insert(0, inputm.get().upper())
    compreply()
def compreply():
    count=0
    chatbot.delete(0,END)
    chatbot.insert(0, "...")
    var = inputm.get().lower()
    query=var
    inputq=var
    if("developed") in inputq or ("you") in inputq or ("hi") in inputq or ("hi") in inputq or "thank" in inputq:
        inputq="thank you. hello, can i help you. i am fine fine hope you're doing well too, i am a chatbot. i am developed by (hritik gupta & divyam pal)."
    else:
     try:
        '''inputq=wikipedia.summary(inputq).lower()
        inputq=re.sub(r'\([^()]*\)', " " ,inputq)
        print(input)'''

        # link for extract html data
        def getdata(url):
            r = requests.get(url)
            return r.text

        print(query)
        for j in search(query, tld="com", num=2,start=1, stop=1):
            htmldata = getdata(j)

        soup = BeautifulSoup(htmldata, 'html.parser')
        data = ''
        data1 = ""
        for data in soup.find_all("p"):
            if len(data1) < 300:
                data1 = data1 + str((data.get_text()))
        count = 1
        for element in range(0, len(data1)):
            if count:
                if data1[element].isalpha():
                    len1 = element
                    print(len1)
                    print(len(data1))
                    data1 = data1[len1:len(data1)]
                    count = 0
        data1 = re.sub(r'\([^()]*\)', "", data1)
        print(data1)
        inputq=data1
     except exceptions as e:
        print("hiiii")
        chatbot.insert(0, "sorry")
        count=1
    if count==0:
       data = {
         "version": "v2.0",
         "data": [
            {
                "title": "your_title",
                "paragraphs": [
                    {
                        "qas": [
                            {
                                "question": var,
                                "id": "1",

                            },

                        ],
                        "context": inputq }]
            }
        ]
    }
       with open("input_file.json", "w") as outfile:
        json.dump(data, outfile)
        print("done")
       os.system("python run_squad.py")
       answer = json.load(open('uncased_L-12_H-768_A-12/predictions.json'))
       answer = answer['1']
       chatbot.insert(0, answer.upper())





def speechfriday():
    os.system(' python main.py')
speechbutton=Button(frame3, text="SPEECH",fg='white',bg ='firebrick3',bd=5, relief=  "raised",command=speechfriday,font = ("Times",11,"bold"))
sendbutton =  Button(frame3, text="SEND",command=sendmsg,bg ='firebrick3',bd=5, relief=  "raised",fg='white',font = ("Times",11,"bold"))

user=Entry(frame2,bd=7,bg= "deep sky blue",fg = 'white',relief="raised", font = ("Times",10,"bold"))
user.insert(0,"USER QUERY")
chatbot=Entry(frame2,bg= "green yellow",bd=7,fg = 'tomato',relief="raised", font = ("Times",10,"bold"))
chatbot.insert(0, "CHATBOT REPLY" )
rules.grid(row=0,column=0)
rule1.grid(row=1,column=1,ipadx=4,ipady=6,pady=4)
rule2.grid(row=2,column=1,ipady=6,pady=5)
rule21.grid(row=3,column=2,ipadx=50,pady=4)
rule22.grid(row=4,column=2,pady=4,ipady=3,ipadx=2)
rule23.grid(row=5,column=2,ipadx=48,pady=4)
rule3.grid(row=6,column=1,ipady=5,pady=4)
#
frame1.grid(row=0,column=0,ipadx=33,ipady=10,sticky='W')
#row=1,column=0 ,rowspan=10, columnspan=10 ,sticky=W,ipady=100
frame2.grid(row=1,column=0 ,rowspan=10, columnspan=10 ,sticky=W,ipady=50,ipadx=0)
#row=11,column=0,sticky=W
frame3.grid(row=11,column=0,sticky=W,ipadx=16)

speechbutton.grid(row=0,column=0,ipadx=12, ipady=15)
inputm.grid(row=0,column=1,columnspan=3,ipadx=104, ipady=15)
sendbutton.grid(row=0,column=4,ipadx=14, ipady=15)
user.grid(row=0,column=1,rowspan=7,ipadx=45,ipady=20,sticky=NW)
chatbot.grid(row=7,column=0,rowspan=3,sticky= W,ipadx=60,pady=10,ipady=20)

root.mainloop()