import ttkbootstrap as ttk
import tkinter as tk

def calcular():
    n1=input_int1.get()
    n2=input_int2.get()
    soma=n1+n2
    output_string.set(soma)

janela=ttk.Window(themename='superhero',resizable=False)
janela.geometry('500x500')
frame=ttk.Frame(janela)
label1=ttk.Label(frame,text='primeiro numero')
label2=ttk.Label(frame,text='segundo numero')
input_int1=tk.IntVar()
input_int2=tk.IntVar()
input1=ttk.Entry(frame,textvariable=input_int1)
input2=ttk.Entry(frame,textvariable=input_int2)
frame.pack(pady='20')
label1.pack()
input1.pack()
label2.pack()
input2.pack(pady='20')
output_string=tk.StringVar()
output=ttk.Label(frame,textvariable=output_string,text='output')
output.pack()
botao=ttk.Button(frame,text='calcular',bootstyle='info-outline',command=calcular)
botao.pack()
janela.mainloop()