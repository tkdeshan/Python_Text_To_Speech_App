import tkinter as tk
from tkinter import *
import os
import playsound
import gtts


def speaknow():
    text_to_speak = textv.get()  # Get the text value from the StringVar
    sound = gtts.gTTS(text_to_speak, lang="en")
    sound.save("welcome.mp3")
    file_path = os.path.abspath("welcome.mp3")
    playsound.playsound(file_path)


root = Tk()

textv = StringVar()

obj = LabelFrame(root, text="Text to Speech", font=20, bd=1)
obj.pack(fill="both", expand=10, padx=10, pady=10)

lbl = Label(obj, text="Text", font=30)
lbl.pack(side=tk.LEFT, padx=5)

text = Entry(obj, textvariable=textv, font=30, width=25, bd=5)
text.pack(side=tk.LEFT, padx=5)

btn = Button(obj, text="Speak", font=20, bg="black", fg="white", command=speaknow)
btn.pack(side=tk.LEFT, padx=10)

root.title("Text to Speech")
root.geometry("500x200")
root.resizable(False, False)

root.mainloop()
