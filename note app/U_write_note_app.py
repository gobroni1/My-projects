#librarys neded for the code 
from tkinter import *
from tkinter import filedialog
import os
import time 
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#maintext = None

#define new function 
def new():
    global maintext,new_window
    new_window = Tk()

    # Properties of new_window
    new_window.title("New note")
    new_window.geometry("400x520")
    new_window.config(bg="#FFFFFF")

    #make the name global so code abov it can read it

   
    #title for new note
    
 
    
    #properties of text area
    maintext = Text(new_window,
                 font=("Arial", 12),
                 fg="black",
                 bg="#FFFFFF",
                 borderwidth=0,
                 padx=20,
                 pady=20
                 )
    maintext.pack(expand=True,fill="both")

    #save button properties
    button1 = Button(new_window,
                     text="Save",
                     command=save,
                     bg="#FFFFFF",
                     borderwidth=0,
                     highlightthickness=10,
                    )
    button1.pack(side=BOTTOM)

    new_window.mainloop()
    
#main UI window properies 
main_window = Tk()
main_window.title("note app")
main_window.geometry("420x520")
main_window.config(bg="#FFFFFF")
plus_image_1 = PhotoImage(file=resource_path("C:\\Users\\delluser\\Desktop\\note app folder\\new_note_pic.png"))
delete_n = PhotoImage(file=resource_path("C:\\Users\\delluser\\Desktop\\note app folder\\delet_button_x.png"))
save_n = PhotoImage(file=resource_path("C:\\Users\\delluser\\Desktop\\note app folder\\save_buton.png"))
open_n = PhotoImage(file=resource_path("C:\\Users\\delluser\\Desktop\\note app folder\\open_n.png"))

tfn_n = Entry(main_window, 
              font=("Arial",12),
                fg="black",
                bg="white",
                borderwidth=1
                )
tfn_n.pack()
tfn_n.insert(END, "        new note name ")

def save():

    #code to get date and to trim it to size
    content = maintext.get("1.0", END)
    current_time = time.localtime(time.time())
    timeasname = time.strftime("%Y-%m-%d", current_time)
    new_window.destroy()

    #code to set the title
    if tfn_n.get() == "":
     file_name = f"note_{timeasname}.txt"

    else:
     file_name_raw = f"note_{tfn_n.get()}.txt"
     file_name = file_name_raw.replace(" ","_")
     
    script_directory = os.path.dirname(__file__)
    file_path = os.path.join(script_directory, file_name)
    
    if file_path:
        with open(file_path, "w") as file:
            file.write(content)
            refresh_notes_list()
            tfn_n.delete(0,END)
def open_note():
    # Function to open a note file and display its content in a new window
    # Create a new window
    window_open = Tk()

    # Get the selected note file from the listbox
    selected_note_index = notelist.curselection()
    if selected_note_index:
        selected_note = notelist.get(selected_note_index[0])

        # Construct the file path
        script_directory = os.path.dirname(__file__)
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
        script_directory = os.path.dirname(__file__)
        file_path = os.path.join(script_directory, modified_name)
    
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)
                refresh_notes_list()
                window_open.destroy()
                tfn_n.delete(0,END)

    #save button properties
    button1_wo = Button(window_open,
                     text="Save",
                     command=save_wo,
                     bg="#FFFFFF",
                     borderwidth=0,
                     highlightthickness=10,
                    )
    button1_wo.pack(side=BOTTOM)

    window_open.mainloop()

def delete_note():
    selected_note = notelist.curselection()
    if selected_note:
        selected_note = notelist.get(selected_note)
        script_directory = os.path.dirname(__file__)
        file_to_delete = os.path.join(script_directory, selected_note)
        os.remove(file_to_delete)
        refresh_notes_list()

def refresh_notes_list():
    notelist.delete(0, END)
    txt_files = [file for file in os.listdir(os.path.dirname(__file__)) if file.endswith('.txt')]
    
    for txt_file in txt_files:
        notelist.insert(END, txt_file)

# Delete button properties
delete_button = Button(main_window,
                       text="Delete", 
                       command=delete_note,
                       bg="#FFFFFF",
                       padx=0,
                       pady=0,
                       borderwidth=0,
                       highlightbackground="#FFFFFF",
                       image=delete_n,
                       compound='top'
                       )
delete_button.pack(side=LEFT, anchor="nw")

#open button
open_b = Button(main_window,
                text = "Open",
                command=open_note,
                bg="#FFFFFF",
                padx=0,
                pady=0,
                borderwidth=0,
                highlightbackground="#FFFFFF",
                image=open_n,
                compound='top'
                )
open_b.pack(side=TOP, anchor="ne")

#new button properties  
new_button = Button(main_window,
                    text="New note",
                    font=("Arial", 8),  
                    command=new,
                    bg="#FFFFFF",
                    padx=0,
                    pady=0,
                    image=plus_image_1,
                    compound='top',
                    relief=RAISED,  
                    borderwidth=0,
                    highlightthickness=10,  
                    highlightbackground="#FFFFFF",  
                    )
new_button.pack(side=BOTTOM,)

#list of notes and list properties 
notelist = Listbox(main_window)
notelist.pack(side=LEFT,anchor="w",expand=True)
notelist.config(height=500,
                width=30,
                borderwidth=0,
                highlightbackground="black",
                highlightthickness=0,
                selectbackground="#dedede",
                selectforeground="black",
                activestyle="none"
                )

refresh_notes_list()

main_window.mainloop()
