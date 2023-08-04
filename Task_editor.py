from tkinter import *
import tkinter.messagebox as mb

def remove():
    lb.delete(ACTIVE)



def add():
    if enter.get() != "":
        lb.insert(END, enter.get())
        enter.delete(0, "end")
    else:
        mb.showwarning("warning", "Please enter some task.")


root = Tk()
root.geometry("540x540")
root.maxsize(540, 540)
root.config(bg="GREY")
frame = Frame(root)
frame.pack(pady=10)
sb = Scrollbar(frame, borderwidth=5, bg="Silver")
lb = Listbox(frame, borderwidth=5, border=10,width=25, height=10, font="areal 19 bold", yscrollcommand=sb.set)
lb.pack(side=LEFT, fill=BOTH)
l = ["Breakfast", "College", "Lunch", "Friend", "Enjoy"]
for i in l:
    lb.insert(END, i)
sb.pack(side=RIGHT, fill=BOTH)
sb.config(command=lb.yview)

frame2 = Frame(root)
frame2.pack(pady=25)
enter = Entry(frame2, font="areal 19 bold", width=25, highlightthickness=10, highlightcolor="silver")
enter.pack()

frame3 = Frame(root)
frame3.pack()

b1 = Button(frame3, text="Add", font="areal 10 bold", width=20, height=3, bg="Silver", command=add)
b1.pack(side="left", padx=3)
b2 = Button(frame3, text="REMOVE", font="areal 10 bold", width=20, height=3, bg="Silver", command=remove)
b2.pack(side=RIGHT, padx=3)

root.mainloop()
