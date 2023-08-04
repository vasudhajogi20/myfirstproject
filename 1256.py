from tkinter import *
from textblob import TextBlob

window=Tk()
window.title("My Spell Checker")
window.geometry('500x400+450+200')
window.config(background="grey")

text_heading=Label(window,text="Spell Checker", font=("Arial",35),bg ="pink",fg="black")
text_heading.pack()

text_check=Label(window,text="Enter the spelling",font=("Arial",20),bg="light blue",fg="blue")
text_check.pack()

spell_check=Entry(window, font=("Arial",20),width=500,bg="white")
spell_check.pack()

check_button = Button(window,text ="Check!!",font=("Arial",15),fg="White",bg="red")
check_button.pack()
window.mainloop()

