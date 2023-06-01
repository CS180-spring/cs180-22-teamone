import customtkinter as ctk
from Functions import *

users = load_users()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("500x350")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="OneDB", font=("calibre", 24))
label.pack(pady=12, padx=10)

entry1 = ctk.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text="Login")
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()

def sign_up_window():
    sign_up_window = ctk.CTk()
    sign_up_window.geometry("300x200")

    username_label = ctk.CTkLabel(master=sign_up_window, text="Username")
    username_label.pack()

    username_entry = ctk.CTkEntry(master=sign_up_window)
    username_entry.pack()

    password_label = ctk.CTkLabel(master=sign_up_window, text="Password")
    password_label.pack()

    password_entry = ctk.CTkEntry(master=sign_up_window, show="*")
    password_entry.pack()

    # Add more widgets and functionality as needed

    sign_up_window.mainloop()
