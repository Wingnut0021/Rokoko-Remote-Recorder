import tkinter
import customtkinter
import rokokoStartRecording as start

def combobox_callback(choice):
    print("combobox dropdown clicked!", choice)

def get_ip1_input():
    start.IP_ADDRESS = suit1_Ip.get()
    print(start.IP_ADDRESS)

def get_api_input():
    start.API_KEY = api_Key.get()
    print(start.API_KEY)

def get_port_input():
    start.PORT = port.get()
    print(start.PORT)

def get_fps_input():
    start.FRAME_RATE = combobox.get()
    print(start.FRAME_RATE)
    
def get_all_inputs():
    get_api_input()
    get_ip1_input()
    get_port_input()
    get_fps_input()

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("600x600")
app.title("Rokoko Remote Recorder")
app.grid_rowconfigure(10, weight=1)
app.grid_columnconfigure(10, weight=1)

def button_startRecord():
    start.start_Recording()
# Use CTkButton instead of tkinter Button
buttonStart = customtkinter.CTkButton(master=app, text="Start Recording", command=button_startRecord)
buttonStart.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

combobox = customtkinter.CTkComboBox(app, values=['30', '60', '100'], command=combobox_callback)
combobox.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Get input value", command=get_all_inputs)
button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

# Create entry widget for suit 1 IP Address
suit1_Ip = customtkinter.CTkEntry(app, placeholder_text="127.0.0.1")
suit1_Ip.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

suit2_Ip = customtkinter.CTkEntry(app, placeholder_text="Suit 2 IP Address")
suit2_Ip.place(relx=0.2, rely=0.6, anchor=tkinter.CENTER)

api_Key = customtkinter.CTkEntry(app, placeholder_text="1234")
api_Key.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

port = customtkinter.CTkEntry(app, placeholder_text="80")
port.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

app.mainloop()