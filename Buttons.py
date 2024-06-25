# from tkinter import *
# root = Tk()
#
# root.geometry("500x400")
# root.title("button project")
#
# def hello():
#     print("hello bhai")
# def name():
#     print("my name is samir")
# def surname():
#     print("my name is salekar")
# def villege():
#     print("my villege name is ghagarkond")
# frame = Frame(root,borderwidth=6,bg="red",relief=SUNKEN)
# frame.pack(anchor="nw",side=LEFT)
# frame1 = Frame(root,borderwidth=6,bg="red",relief=SUNKEN)
# frame1.pack(anchor="nw",side=LEFT)
# frame2 = Frame(root,borderwidth=6,bg="red",relief=SUNKEN)
# frame2.pack(anchor="nw",side=LEFT)
# frame3 = Frame(root,borderwidth=6,bg="red",relief=SUNKEN)
# frame3.pack(anchor="nw",side=LEFT)
#
# b1 = Button(frame,fg="green",text="press the button",command=hello)
# b1.pack(side=LEFT,padx=25)
#
# b2 = Button(frame1,fg="green",text="press the button",command=name)
# b2.pack(side=LEFT,padx=25)
# b3 = Button(frame2,fg="green",text="press the button",command=surname)
# b3.pack(side=LEFT,padx=25)
# b4 = Button(frame3,fg="green",text="press the button",command=villege)
# b4.pack(side=LEFT,padx=25)
#
# root.mainloop()



# from tkinter import *
# root=Tk()
# def getvals():
#     print(uservalue.get())
#     print(passvalue.get())
# root.geometry("500x400")
# user = Label(root,text="Username")
# password = Label(root,text="Password")
# user.grid()
# password.grid(row=1)
#
# uservalue =StringVar()
# passvalue = StringVar()
#
# userentry= Entry(root,textvariable= uservalue)
# passentry= Entry(root,textvariable=passvalue)
#
# userentry.grid(row=0,column=1)
# passentry.grid(row=1,column=1)
# Button(text="Submit",command=getvals).grid()
#
#
#
#
#
#
#
#
# root.mainloop()
import tkinter as tk

# Create a tkinter window
root = tk.Tk()
root.title("Button Replication")

# List of button labels
button_labels = ["Button 1", "Button 2", "Button 3", "Button 4", "Button 5"]

# Create buttons using a for loop
for label in button_labels:
    button = tk.Button(root, text=label)
    button.pack()

# Start the tkinter event loop
root.mainloop()
