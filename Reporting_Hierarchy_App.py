# App Front end 
from tkinter import *
import backend

def ImportCommand():
    backend.ImportData()

def GetDetails_Command():
    data = backend.Display(e1.get())
    l1_text.set(data[0][0])
    l2_text.set(data[0][1])
    l3_text.set(data[0][2])
    l4_text.set(data[0][3])
    l5_text.set(data[0][4])
    l6_text.set(data[0][5])
        

root = Tk()
root.title('Reporting Hierarchy App')
root.geometry("300x250")

topframe = Frame(root)
topframe.pack(pady=20)

middleframe = Frame(root)
middleframe.pack()

bottomframe = Frame(root)
bottomframe.pack()

# Top Frame

b1 = Button(topframe,text='Import Data',width=10,command=ImportCommand)
b1.pack(side=LEFT,padx=20,pady=15)

l1 = Label(topframe,text='Enter Employee ID')
l1.pack()

e1= Entry(topframe,width=15)
e1.pack()

# Middle Frame
b1 = Button(middleframe,text='Get Details',width=10,command=GetDetails_Command)
b1.pack(side=LEFT)

# Bottom Frame
l1 = Label(bottomframe,text='Employee Name')
l1.grid(row=0,column=0)

l1_text = StringVar()
l1_display = Label(bottomframe,textvariable= l1_text,bg='white')
l1_display.grid(row=1,column=0)

l2 = Label(bottomframe,text='Sponser Name')
l2.grid(row=2,column=0)

l2_text = StringVar()
l2_display = Label(bottomframe,textvariable=l2_text,bg='white')
l2_display.grid(row=3,column=0)

l3 = Label(bottomframe,text='Business Name')
l3.grid(row=4,column=0)

l3_text = StringVar()
l3_display = Label(bottomframe,textvariable=l3_text,bg='white')
l3_display.grid(row=5,column=0)

l4 = Label(bottomframe,text='Supervisor L1')
l4.grid(row=0,column=1)

l4_text = StringVar()
l4_display = Label(bottomframe,textvariable=l4_text,bg='white')
l4_display.grid(row=1,column=1)

l5 = Label(bottomframe,text='Supervisor L2')
l5.grid(row=2,column=1)

l5_text = StringVar()
l5_display = Label(bottomframe,textvariable=l5_text,bg='white')
l5_display.grid(row=3,column=1)

l6 = Label(bottomframe,text='Supervisor L3')
l6.grid(row=4,column=1)

l6_text = StringVar()
l6_display = Label(bottomframe,textvariable=l6_text,bg='white')
l6_display.grid(row=5,column=1)

root.mainloop()