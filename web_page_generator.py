import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        #Setting up entry button for user input
        self.user_entry = Entry(width=100)
        self.user_entry.grid(row=0, column=0, columnspan=2, padx=(15,15), pady=(25,0))
        #Default button
        self.btn = Button(self.master, text="Default HTML Text", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10), pady=(10,10), sticky=E)
        #custom button
        self.btn = Button(self.master, text="Custom Text", width=30, height=2, command=self.customHTML)
        self.btn.grid(padx=(10,10), pady=(10,10), sticky=E)

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</html>\n</body>\n</h1>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    #Function for custom text entry
    def customHTML(self):
        ChtmlText = self.user_entry.get()#gets the user input from entry above and makes it the htmlText variable
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + ChtmlText + "</html>\n</body>\n</h1>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    
    




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
