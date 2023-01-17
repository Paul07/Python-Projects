import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import *



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Names the GUI window
        self.master.title("File Transfer")

        #Select button for files in the directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Position source button
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))
        #creates select button for files from source directory

        #entry for directory selection
        self.source_dir = Entry(width=75)
        #positions the buttons
        #on the same line
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        #Button to select the destination of files from the destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #places the destination button
        #on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        #entry for destination selection
        self.destination_dir = Entry(width=75)
        #places entry button
        #in a line with the select button
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))

        #creates tranfer files button
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #place transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        #creates the exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #postion the exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    #function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #.delete(0, END) clears the entry widget
        #allows the path to be inserted in the entry widget properly
        self.source_dir.delete(0, END)
        #.insert will insert the user selection into the source_dir entry
        self.source_dir.insert(0, selectSourceDir)

    #function to select destination directory
    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        #.delete(0, END) clears the entry widget
        #allows the path to be inserted in the entry widget properly
        self.destination_dir.delete(0, END)
        #.insert will insert the user selection into the destination_dir entry
        self.destination_dir.insert(0, selectDestDir)

    #function to transfer files from one dir to another
    def transferFiles(self):
        #gets source dir
        source = self.source_dir.get()
        #gets destination dir
        destination = self.destination_dir.get()
        #gets a list of files in the source directory
        source_files = os.listdir(source)
        #runs through each file in the source dir
        for i in source_files:
            filePath = os.path.join(source, i)
            modTime = os.path.getmtime(filePath)
            if ((datetime.now() - datetime.fromtimestamp(modTime)) <= timedelta(hours=24)):
            #moves each file from source to destination
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')

    #Function to exit the program
    def exit_program(self):
        #root is the main GUI window
        #tells python to end mainloop and all widgets in the window
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
