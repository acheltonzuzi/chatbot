import tkinter as tk
import ttkbootstrap as ttk

def convert():
    milha=input_int.get()
    kilometro=milha*1.61
    output_string.set(kilometro)
#window=ttk.Window(themename='journal')
window=ttk.Window(themename='superhero')
window.title('conversor')
window.geometry('300x150')
title_label=ttk.Label(master=window,text='Milhas para kilometros',font='arial 16 bold')
title_label.pack()
frame=ttk.Frame(master=window)
input_int=tk.IntVar()
input_1=ttk.Entry(master=frame,textvariable=input_int)
button_1=ttk.Button(master=frame,text='Converter',command=convert,)
input_1.pack(side='left',padx='10')
button_1.pack(side='left')
frame.pack(pady='10')
output_string=tk.StringVar()
output_1=ttk.Label(master=window,text='saida:',font='arial 24 bold',textvariable=output_string)
output_1.pack()


window.mainloop()