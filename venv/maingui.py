from tkinter import *
from PIL import ImageTk, Image
import os
root = Tk()
root.title('AI Virtual Assistant')
root.geometry("1055x633")
canvas = Canvas(width=800, height=800)
canvas.pack(expand=YES, fill=BOTH)

image = ImageTk.PhotoImage(file="696969.jpg")
canvas.create_image(10, 10, image=image, anchor=NW)
img1 = ImageTk.PhotoImage(Image.open("222.png"))
img2 = ImageTk.PhotoImage(Image.open("777.png"))
img3 = ImageTk.PhotoImage(Image.open("444.png"))
img4 = ImageTk.PhotoImage(Image.open("555.png"))

frame = LabelFrame(canvas )
frame.pack(side = BOTTOM)
def speech():
    os.system("python main.py")
def chatbot():
    os.system("python chatbogui.py")
mybutton1 = Button(frame, text="   Voice Assistant ", image=img1,
                   compound=RIGHT, fg="sky blue",command= speech, activebackground="black", activeforeground="white",
                   bg="purple", bd=10, padx=38, pady=2,font=("Helvetica", 15)).pack()
mybutton2 = Button(frame, text="   Chat BOT ", fg="sky blue", activebackground="black",
                   activeforeground="white",command=chatbot, bg="purple", bd=10, image=img2,
                   compound=RIGHT, padx=53, pady=2, font=("Helvetica", 15)).pack()

buttonquit = Button(frame, text="   EXIT HERE", command=root.quit, fg="sky blue",
                    activebackground="black", activeforeground="white", bg="purple", bd=10, image=img3,
                    compound=RIGHT, padx=50, pady=2, font=("Helvetica", 15)).pack()
root.mainloop()