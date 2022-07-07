from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
from PIL import ImageTk, Image

#Create a frame
root = Tk()
root.title("CrazyChatBot")
root.geometry("500x1000")

#Add a background
bg = ImageTk.PhotoImage(file="background.jpg")
canvas = Canvas(root, width=500, height=1000)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor='nw')



# BG_GRAY = "#ABB9B9"
# BG_GRAY = "#ABB2B9"
#TEXT_COLOR = "#EAECEE"
root.mainloop()
