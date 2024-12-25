from currency_converter import CurrencyConverter
import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry("500x400")
root.title("Currency Converter")
root.resizable(False,False)

a=CurrencyConverter()

def clicked():
    amount=int(e1.get())
    curr1=e2.get()
    curr2=e3.get()
    res=a.convert(amount,curr1,curr2)
    global l5
    l5=tk.Label(root,text=res,font=("Times",15,"bold"),fg="red",pady=10)
    l5.place(x=180,y=350)

def reset():
    e1.delete(0,tk.END)
    e2.set('')
    e3.set('')
    if 'l5' in globals():
        l5.destroy()

l1=tk.Label(root,text="Currency Conveter",font=("Arial",24,"bold"))
l1.place(x=100,y=30)

l2=tk.Label(root,text="Enter amount here:",font=("Times",15,"bold"),pady=25)
l2.place(x=50,y=80)

e1=tk.Entry(root,justify="center",font="bold")

l3=tk.Label(root,text="Enter currency:",font=("Times",15,"bold"),pady=25)
l3.place(x=50,y=130)

currency_options=list(a.currencies)
e2=ttk.Combobox(root,values=currency_options,justify="center",font="bold")

l4=tk.Label(root,text="Enter req currency:",font=("Times",15,"bold"),pady=25)
l4.place(x=50,y=180)

e3=ttk.Combobox(root,values=currency_options,justify="center",font="bold")

b1=tk.Button(root,text="Click",command=clicked,font=("Arial",15,"bold"),bg="gray")
b1.place(x=130,y=280,width=70)

b2=tk.Button(root,text="Reset",command=reset,font=("Arial",15,"bold"),bg="gray")
b2.place(x=310,y=280,width=70)

e1.place(x=250,y=110,width=200)

e2.place(x=250,y=160,width=200)

e3.place(x=250,y=210,width=200)

root.mainloop()
