#
#
#
import tkinter as tk
from tkinter import ttk



class RecorderGUI:
    
    def __init__(self):
        
        
        self.root = tk.Tk()
        
        self.menubar = tk.Menu(self.root)
        
        self.filemenu = tk.Menu(self.root, tearoff=0)
        self.filemenu.add_command(label="Close", command=exit)
        
        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_message)
        
        
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")
        
        self.root.config(menu=self.menubar)
                        

        self.root.geometry("500x500")
        self.root.title("Rokoko Remote Recorder")

        self.label = tk.Label(self.root, text="Hello World!", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.textbox = tk.Text(self.root)
        self.textbox.pack(padx=20, pady=20)
        
        self.button = tk.Button(self.root, text="Click Me!", command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def show_message(self):
        print(self.textbox.get('1.0'))
    
RecorderGUI()