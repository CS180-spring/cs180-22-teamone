import customtkinter as ctk
from tkinter import messagebox
from Functions import load_users, hash_password

users = load_users()


def SignUp():
    signup_window = ctk.CTk()
    signup_window.geometry("400x300")
    signup_window.title("Sign Up")

    username_label = ctk.CTkLabel(master=signup_window, text="Username")
    username_label.pack(pady=10)

    username_entry = ctk.CTkEntry(master=signup_window)
    username_entry.pack()

    password_label = ctk.CTkLabel(master=signup_window, text="Password")
    password_label.pack(pady=10)

    password_entry = ctk.CTkEntry(master=signup_window, show="*")
    password_entry.pack()

    # Add more GUI elements as needed

    signup_button = ctk.CTkButton(master=signup_window, text="Sign Up")
    signup_button.pack(pady=10)

    signup_window.mainloop()



# code for creating the database and GUI 
def createDatabase():
    print("Creating a Database...")

# Code for showiung the current database selected // This can be changed to always show the current database at the top
def currentDatabase():
    print("Current Database...")

# maybe another window showing all the databases they can pick. OR dropdown list of some sort
def chooseDatabase():
    print("Choose Database...")
    ## when the pick a database it shows the following options
    ## Create Record
    ## Read Record
    ## Update Record
    ## Delete Record 
    ## Also other options such as Search and View Table? 
    


# pick and delete a database gui/code
def deleteDatabase():
    print("Delete Database...")


def mainMenuGUI():
    main_menu_window = ctk.CTk()
    main_menu_window.geometry("400x300")
    main_menu_window.title("Main Menu")

    create_button = ctk.CTkButton(master=main_menu_window, text="Create a Database", command=createDatabase)
    create_button.pack(pady=10)

    current_button = ctk.CTkButton(master=main_menu_window, text="Current Database", command=currentDatabase)
    current_button.pack(pady=10)

    choose_button = ctk.CTkButton(master=main_menu_window, text="Choose Database", command=chooseDatabase)
    choose_button.pack(pady=10)

    delete_button = ctk.CTkButton(master=main_menu_window, text="Delete Database", command=deleteDatabase)
    delete_button.pack(pady=10)

    main_menu_window.mainloop()


def Login():
    username = entry1.get()
    password = entry2.get()
    password = hash_password(password)

    if username in users and users[username]['password'] == password:
        #messagebox.showinfo("Login Successful", "Welcome, " + username)
        mainMenuGUI()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


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

button = ctk.CTkButton(master=frame, text="Login", command=Login)
button.pack(pady=12, padx=10)

signUpButton = ctk.CTkButton(master=frame, text="Sign Up", command=SignUp)
signUpButton.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()
