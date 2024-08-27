from tkinter import *
from tkinter import filedialog
import customtkinter
import os
import hashlib
import shutil
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x500")
root.title("Dupe Daster DD")
def cancel ():
    root.destroy()
frame = customtkinter.CTkFrame(master=root,)
frame.pack(padx=60,fill="both")
frame2 = customtkinter.CTkFrame(master=root,)
frame2.pack(padx=60,fill="both",expand=True)
Label = customtkinter.CTkLabel(master=frame,text="Click start to start or Click Cancel to cancel")
Label.pack(pady=12,padx=10)

#startting window
def start ():
     # Get the path to the desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

     # Specify the folder name
    folder_name = "duplicates"

     # Combine the desktop path and folder name
    folder_path = os.path.join(desktop_path, folder_name)

     # Check if the folder doesn't exist already
    if not os.path.exists(folder_path):
      # Create the folder
        os.makedirs(folder_path)
        print(f"Folder '{folder_name}' created successfully on the desktop.")
    else:
        print(f"Folder '{folder_name}' already exists on the desktop.")

#choose folder to satrt   
    new1_folder = 'C:\\Users\\Admin\\Desktop\\duplicates'
    main_folder_path = filedialog.askdirectory(title="Choose where to start from")

#see if folders are hidden
    def is_hidden(filepath2):
            # Get the file attributes
            attrs = os.stat(filepath2).st_file_attributes
            # Check if the file is hidden
            return attrs & 2 != 0 

#go thrue all folders and sub folders
    file_reader = os.walk(main_folder_path)
    uniqueFiles = dict()

    for folder, sub_folder, files in file_reader:
        for file in files:
            filepath2 = os.path.join(folder, file)
            filehash = hashlib.md5(open(filepath2, "rb").read()).hexdigest()

        
            #if folder is hidden
            if is_hidden(folder):
                print("folder is hidden, can't be opend")
            #else 
            elif filehash in uniqueFiles:
            # Move the duplicate file to new1_folder
                shutil.move(filepath2, os.path.join(new1_folder, file))
                print(f"{filepath2} has been moved to -duplicats-")
            else:
            # Store the filehash and folder path in uniqueFiles
                uniqueFiles[filehash] = folder
#last massage
print("program ran successfully, doesn't mean that every thing went well...")  

start = customtkinter.CTkButton(master=frame,text = "start",command = start )
start.pack(side=LEFT, anchor=NE)

cancel = customtkinter.CTkButton(master=frame,text="cancel",command=cancel)
cancel.pack(side=RIGHT, anchor=NW)

Lable2 = customtkinter.CTkLabel(master=frame2,text="This app will go through all of your files and folders")
Lable2.pack(anchor=S)

Lable3 = customtkinter.CTkLabel(master=frame2,text="moving duplicates in the folder -duplicates- on your desktop")
Lable3.pack(anchor=S)

root.mainloop()