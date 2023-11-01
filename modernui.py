import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
janela=ctk.CTk()
janela.geometry('500x300')
button = ctk.CTkButton(master=janela, text="CTkButton",corner_radius=32)
button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
janela.mainloop()