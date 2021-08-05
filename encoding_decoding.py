# This is a String Encoding and Decoding GUI made using Tkinker. Enter a string in the GUI and choose either Encoding or Decoding option. Click on "Show Result" to see the result of the option chosen. To see the opposite result, copy the result text to the message and choose the opposite mode and click on "Show Result". #

# Importing the Required Libraries
from tkinter import *
from tkinter import messagebox
import base64
from base64 import encode

# Setting the Tkinter Frame and Styling it
container = Tk()
container.geometry('600x600')
container.title('Encoding and Decoding Messages')
container.config(background='light blue')

# Declaring the Variables
message_text = StringVar()
smessage = StringVar()
choice = StringVar()

# Tkinter Widgets Design and Placement 
label1 = Label(container, text="ENCODE & DECODE MESSAGES", font='helvetica 16 bold', background='light blue').pack(padx=80, pady=20)
label2 = Label(container, text="Enter Message: ", font='helvetica 14 bold', background='light blue').place(x=100, y=120)
entry1 = Entry(container, font='helvetica 14 italic', textvariable=message_text, disabledbackground='black',background='white').place(x=275, y=120)
label5 = Label(container, text="Select Mode: ", font='helvetica 14 bold', background='light blue').place(x=100, y=175)
entry4 = Entry(container, font='helvetica 14 italic', textvariable=choice, disabledbackground='black',background='white').place(x=275, y=175)
label6 = Label(container, text="(Enter 'e' for 'ENCODE' and 'd' for 'DECODE')", font='helvetica 11 italic', background='light blue').place(x=100, y=220)
button1 = Button(container, text="SHOW RESULT", font='helvetica 14 bold', background='light cyan', command=lambda:choice_data()).place(x=220, y=260)
label4 = Label(container, text="Resulting Text: ", font='helvetica 14 bold', background='light blue').place(x=90, y=325)
entry3 = Entry(container, font='helvetica 14 italic', textvariable=smessage, disabledbackground='black',background='white').place(x=250, y=325)
button3 = Button(container, text="RESET", font='helvetica 14 bold', background='light cyan', command=lambda:reset_data()).place(x=255, y=375)

# Data Reset Function
def reset_data():
    message_text.set("--")
    smessage.set("--")
    choice.set("--")

# Choosing action based on Encode or Decode
def choice_data():
    if choice.get() in ("e", "E"):
        smessage.set(encode_data(message_text.get()))
    elif choice.get() in ("d", "D"):
        smessage.set(decode_data(message_text.get()))
    else:
        messagebox.showerror("Check Validity", "Try Again")

# Data Encoding Function
def encode_data(message_string):
    message_string_text = message_string.encode("cp437")
    message_base = base64.b85encode(message_string_text) 
    return (message_base)

# Data Decoding Function
def decode_data(message_string):
    message_string_text = message_string.encode("cp437")
    decode_string = base64.b85decode(message_string_text)
    return (decode_string)

# To keep the window up, till the user closes it
container.mainloop()