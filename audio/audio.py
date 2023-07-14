import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk()
root.title("Text to Speech")
root.geometry("900x450+100+200")
root.resizable(False, False)
root.configure(background="#305065")

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if (text):
        if (speed =="Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == "Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()   
def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text ,'audio.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text ,'audio.mp3')
            engine.runAndWait()

    if (text):
        if (speed =="Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == "Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()   
#icon
image_icon = PhotoImage(file="speak.png")
root.iconphoto(False, image_icon)

#Top frame
Top_frame=Frame(root,bg="#00FFF7",width=900,height=100)
Top_frame.place(x=0,y=0)

Logo=PhotoImage(file="speaker logo.png")
Label(Top_frame,image=Logo,bg="#00FFF7").place(x=20,y=10)

Label(Top_frame,text="Text to Speech",font=("times new roman",30,"bold"),bg="#00FFF7",fg="black").place(x=100,y=30)


##############################################
text_area=Text(root,font="Robot 20",bg="#00FFF7",fg="black",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

Label(root,text="VOICE",font=("arial",15,"bold"),bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="SPEED",font=("arial",15,"bold"),bg="#305065",fg="white").place(x=760,y=160)

gender_combobox=Combobox(root,values=["Male","Female"],font="arial 14",state="r",width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')

speed_combobox=Combobox(root,values=["Fast","Normal","Slow"],font="arial 14",state="r",width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')

imageicon=PhotoImage(file="speaker logo.png")
btn=Button(root,text="Speak",compound=LEFT,image=imageicon,width=160,height=80,bg="#39c790",font="arial 14 bold",command=speaknow)
btn.place(x=530,y=280)

imageicon2=PhotoImage(file="download.png")
save=Button(root,text="Save",compound=LEFT,image=imageicon2,width=160,height=80,bg="#39c790",font="arial 14 bold",command=download)
save.place(x=710,y=280)





root.mainloop()