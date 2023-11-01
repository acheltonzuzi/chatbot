import tkinter as tk 
from tkinter import ttk


window=tk.Tk()
window.geometry('720x500')

text=tk.Text(window)
text.pack()
entry=ttk.Entry(window)
entry.pack()
btn=ttk.Button(window,text='cadastrar')
btn.pack()

window.mainloop()