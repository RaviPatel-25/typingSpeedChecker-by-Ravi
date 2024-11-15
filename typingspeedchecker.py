
from tkinter import *

from timeit import default_timer as timer

import random

 

root = Tk()

w=root.winfo_screenwidth()

h=root.winfo_screenheight()

root.resizable(False,False)

root.overrideredirect(True)

root.geometry(str(w)+"x"+str(h)+"+0+0")

root.config(bg='white')

 

x = 0

def reset():

	global root

	root.destroy()

	root = Tk()

	w=root.winfo_screenwidth()

	h=root.winfo_screenheight()

	root.resizable(False,False)

	root.overrideredirect(True)

	root.geometry(str(w)+"x"+str(h)+"+0+0")

	root.config(bg='white')

	

	def destroy():

		root.destroy()

	label=Label(root, text='Do you want to try again', bg='yellow',fg='red',font="times 12 bold")

	label.place(x=130, y=400)

	b= Button(root, text="Enter", command=start, width=12, bg='lightgreen')

	b.place(x=300, y=750)

	b = Button(root, text="Close", command=destroy, width=12, bg='red')

	b.place(x=300, y=650)

	root.mainloop()

def start():

    global x,root

    if x == 0:

        root.destroy()

        x = x+1

        

    root = Tk()

    w=root.winfo_screenwidth()

    h=root.winfo_screenheight()

    root.resizable(False,False)

    root.overrideredirect(True)

    root.geometry(str(w)+"x"+str(h)+"+0+0")

    root.config(bg='white')

    

    def destroy():

    	global root

    	root.destroy()

 

    def check_result():

        global root

        if entry.get() == words[word]:

            end = timer()

            print(str((end-start)*0.1)+'sec')

            req_time=(str((end-start)*0.1))

            req_time=req_time[:8]+' sec'

            label1=Label(root, text='Time required:- ', bg='white',fg='black',font="times 10 bold")

            label1.place(x=130, y=950)

            label2=Label(root, text=req_time+'        ', bg='white',fg='blue',font="times 10 bold")

            label2.place(x=590, y=950)

           

        else:

            label=Label(root, text='   You typed wrong spelling    ', bg='yellow',fg='red',font="times 10 bold")

            label.place(x=130, y=950)

            print("Wrong Input")

 

    words = ['programming','voding' , 'coding', 'algorithm','systems', 'python', 'software']



    word = random.randint(0, (len(words)-1))

    start = timer()



    x2 = Label(root, text='Word:- '+words[word],bg='white' ,font="times 15 bold")

    x2.place(x=130, y=100)



    x3 = Label(root, text="Start Typing:- ", bg='white',font="times 10 bold")

    x3.place(x=20, y=300)

 

    entry = Entry(root)

    entry.place(x=450, y=310)



    b2 = Button(root, text="Done",command=check_result, width=12, bg='lightgreen')

    b2.place(x=300, y=550)

 



    b3 = Button(root, text="Try Again", command=reset, width=12, bg='yellow')

    b3.place(x=300, y=650)

    

    b4 = Button(root, text="Close", command=destroy, width=12, bg='red')

    b4.place(x=300, y=750)



    root.mainloop()

 

 

l1 = Label(root, text="Typing Speed Checker", bg='white',fg='blue',font="times 15 bold underline")

l1.place(x=60, y=150)

x1 = Label(root, text="  Lets start....!  ", bg='yellow',fg='blue',font="times 20")

x1.place(x=160, y=550)

 



b1 = Button(root, text="Start", command=start,bd=5, width=12, bg='orange')

b1.place(x=300, y=850)



root.mainloop()