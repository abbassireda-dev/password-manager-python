import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x150")
app.title("Test Window")

label = ctk.CTkLabel(app, text="CustomTkinter Works!")
label.pack(pady=20)

app.mainloop()
