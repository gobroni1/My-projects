#librarys neded for the code - 0
from tkinter import *
from tkinter import filedialog
import os
import time
from pathlib import Path

# - 1 
def openpswcommand():
    
    # Function to open a note file and display its content in a new window
    # Create a new window
    window_open = Tk()

    # Get the selected note file from the listbox
    selected_note_index = notelist.curselection()
    if selected_note_index:
        selected_note = notelist.get(selected_note_index[0])

        # Construct the file path
        script_directory = "\\Users\\delluser\\Documents\\code_file_for_pws_managment"
        file_path = os.path.join(script_directory, selected_note)

        # name os the winsow
        modified_name = file_path
        name_for_window_wo = "youre_note"

        # Read the content of the selected note file
        with open(file_path, 'r') as file:
            note_content = file.read()

        # Set up the properties of the new window
        window_open.title(name_for_window_wo)
        window_open.geometry("420x520")
        window_open.config(bg="#FFFFFF")

        # Create a Text widget to display the note content
        note_text = Text(window_open,
                         font=("Arial", 12),
                         fg="black",
                         bg="#FFFFFF",
                         borderwidth=0,
                         )
        note_text.pack()
        note_text.insert(END, note_content)  # Insert the content of the note into the Text widget
           
    def save_wo():
        content = note_text.get("1.0", END)
        script_directory = "\\Users\\delluser\\Documents\\code_file_for_pws_managment"
        
        file_path = os.path.join(script_directory, modified_name)
    
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)
                refresh_list()
                window_open.destroy()
               
    #save button properties
    button1_wo = Button(window_open,
                     text="Save",
                     command=save_wo,
                     bg="#FFFFFF",
                     borderwidth=0,
                     highlightthickness=10,
                    )
    button1_wo.pack(side=BOTTOM)
# - 2
def refresh_list():
    script_directory = "\\Users\\delluser\\Documents\\code_file_for_pws_managment"
    notelist.delete(0, END)
    txt_files = [file for file in os.listdir(script_directory) if file.endswith('.txt')]
    
    for txt_file in txt_files:
        notelist.insert(END, txt_file)
# - 3 
def new():
     window2 = Tk()
     window2.geometry ("200x200")

     maintext = Entry(window2,)
     maintext.pack()

     pswfor = Entry(window2)
     pswfor.pack()
    

     def save_2 ():
         nameofpsw = "organisation: " + maintext.get() 
         psw = "password for it: " + pswfor.get()
         if 1==1:
          file_name_raw = f"note_{maintext.get()}.txt"
          file_name = file_name_raw.replace(" ","_")
     
          script_directory = "\\Users\\delluser\\Documents\\code_file_for_pws_managment"
          file_path = os.path.join(script_directory, file_name)
    
          if script_directory:
           with open(file_path, "w") as file:
        
            with open(file_path, "w") as file:
             file.write(nameofpsw)
             file.write("\n")
             file.write(psw)

             maintext.delete(0,END)
             pswfor.delete(0,END)
      
     save2= Button (window2,
                    command=save_2,
                     text="save3" )
     save2.pack()
     window2.mainloop()

# - 4
     
def gmailw():
    window3 = Tk()
    window3.geometry("200x200")

    gmailname = Entry (window3, )
    gmailname.pack()

    gmailpsw = Entry(window3,)
    gmailpsw.pack()

    def save (): 
    #code to get date and to trim it to size
     current_time = time.localtime(time.time())
     timeasname = time.strftime("%Y-%m-%d", current_time)

     bugname = (gmailpsw.get() + "  :this is you corespondig password")
     bugname2 = (gmailname.get() + "  :this is your G-mail")
     #code to set the title
     if gmailname.get() == "":
      file_name = f"note_{timeasname}.txt"

     else:
      file_name_raw = f"note_{gmailname.get()}.txt"
      file_name = file_name_raw.replace(" ","_")
     
     script_directory = "\\Users\\delluser\\Documents\\code_file_for_pws_managment"
     file_path = os.path.join(script_directory, file_name)

     

     
     with open(file_path, "w") as file:
            file.write(bugname2)
            file.write("\n")
            file.write(bugname)
            
            gmailname.delete(0,END)
            gmailpsw.delete(0,END)

    printname = Button(window3,
                   command=save,
                   text="save")
    printname.pack()

    window3.mainloop()

   
# -5 
window1 = Tk()

notelist = Listbox(window1,)
notelist.pack(side=LEFT,anchor="w",expand=True)
notelist.config(height=20,width=30,borderwidth=0,highlightbackground="black",highlightthickness=0,selectbackground="#dedede",selectforeground="black",activestyle="none") 
refresh_list()

Bnew = Button(window1, text="new",command= new)
Bnew.pack()

gmailpass = Button (window1,
                    text="G-mail password",
                    command=gmailw)
gmailpass.pack()

open_psw = Button (window1,text = "open", command=openpswcommand)
open_psw.pack()

window1.mainloop()