import tkinter as tk
import tkinter.font as tkFont

class StartScreen:
    def __init__(self, root):
        #setting title
        root.title("Start Screen")
        #setting window size
        width=772
        height=487
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)

        logInButton=tk.Button(root)
        logInButton["bg"] = "#5ffb0e"
        logInButton["cursor"] = "mouse"
        ft = tkFont.Font(family='Times',size=10)
        logInButton["font"] = ft
        logInButton["fg"] = "#000000"
        logInButton["justify"] = "center"
        logInButton["text"] = "Log in"
        logInButton.place(x=260,y=240,width=197,height=43)
        logInButton["command"] = self.GButton_134_command

        newUserButton=tk.Button(root)
        newUserButton["bg"] = "#5ffb0e"
        ft = tkFont.Font(family='Times',size=10)
        newUserButton["font"] = ft
        newUserButton["fg"] = "#000000"
        newUserButton["justify"] = "center"
        newUserButton["text"] = "New User"
        newUserButton.place(x=260,y=300,width=197,height=41)
        newUserButton["command"] = self.GButton_421_command

        Logo=tk.Label(root)
        Logo["bg"] = "#5ffb0e"
        Logo["cursor"] = "mouse"
        ft = tkFont.Font(family='Times',size=38)
        Logo["font"] = ft
        Logo["fg"] = "#333333"
        Logo["justify"] = "center"
        Logo["text"] = "Workout Analytics"
        Logo.place(x=180,y=20,width=374,height=56)

    def GButton_134_command(self):
        print("command") #insert commands here


    def GButton_421_command(self):
        print("command") #insert commands here

if __name__ == "__main__":
    root = tk.Tk()
    app = StartScreen(root)
    root.mainloop()


class LogIN:
    def __init__(self, root):
        #setting title
        root.title("Log In Screen")
        #setting window size
        width=767
        height=329
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        Logo=tk.Label(root)
        Logo["bg"] = "#5ffb0e"
        Logo["cursor"] = "mouse"
        ft = tkFont.Font(family='Times',size=36)
        Logo["font"] = ft
        Logo["fg"] = "#000000"
        Logo["justify"] = "center"
        Logo["text"] = "Workout Analytics"
        Logo.place(x=210,y=20,width=380,height=49)

        UsernameEntry=tk.Entry(root)
        UsernameEntry["anchor"] = "center"
        UsernameEntry["borderwidth"] = "1px"
        UsernameEntry["cursor"] = "mouse"
        ft = tkFont.Font(family='Times',size=10)
        UsernameEntry["font"] = ft
        UsernameEntry["fg"] = "#333333"
        UsernameEntry["justify"] = "center"
        UsernameEntry["text"] = "Username:"
        UsernameEntry.place(x=360,y=160,width=70,height=25)

        PasswordEntry=tk.Entry(root)
        PasswordEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        PasswordEntry["font"] = ft
        PasswordEntry["fg"] = "#333333"
        PasswordEntry["justify"] = "center"
        PasswordEntry["text"] = "Password:"
        PasswordEntry["show"] = "*"
        PasswordEntry.place(x=360,y=190,width=70,height=25)

        CancelButton=tk.Button(root)
        CancelButton["bg"] = "#f0f0f0"
        CancelButton["cursor"] = "mouse"
        ft = tkFont.Font(family='Times',size=10)
        CancelButton["font"] = ft
        CancelButton["fg"] = "#000000"
        CancelButton["justify"] = "center"
        CancelButton["text"] = "Cancel"
        CancelButton.place(x=210,y=270,width=169,height=38)
        CancelButton["command"] = self.GButton_985_command

        OKButton=tk.Button(root)
        OKButton["bg"] = "#f0f0f0"
        OKButton["cursor"] = "mouse"
        ft = tkFont.Font(family='Times',size=10)
        OKButton["font"] = ft
        OKButton["fg"] = "#000000"
        OKButton["justify"] = "center"
        OKButton["text"] = "OK"
        OKButton.place(x=390,y=270,width=171,height=38)
        OKButton["command"] = self.GButton_138_command

    def GButton_985_command(self):
        print("command")


    def GButton_138_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = LogIN(root)
    root.mainloop()


