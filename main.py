import tkinter
import customtkinter
import rokokoStartRecording as start
import RecordBrekel as brekel
from datetime import datetime


IP_ADDRESS = ""
CLIP_NAME = ""
TAKE_NUMBER = 1

def get_ip_input():
    start.IP_ADDRESS = suit_Ip.get()
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

def button_startRecordAll():
    now = datetime.now()
    NOW = now.strftime("%d_%m_%Y_%H_%M_%S")
    print(NOW)

    IP_ADDRESS = suit_Ip.get()
    CLIP_NAME = suit_Name.get()
    CLIP_NAME = CLIP_NAME + TAKE_NUMBER + NOW
    start.start_Recording(IP_ADDRESS=IP_ADDRESS,CLIP_NAME=CLIP_NAME)

def button_stopRecordAll():
    TAKE_NUMBER = TAKE_NUMBER + 1
    IP_ADDRESS = suit_Ip.get()
    start.stop_Recording(IP_ADDRESS=IP_ADDRESS,CLIP_NAME=CLIP_NAME)

def button_startRecordBrekel():
    brekel.click_Brekel()
def button_stopRecordBrekel():
    brekel.click_Brekel()

def button_startRecordAllandBrekel():
    brekel.click_Brekel()
    button_startRecordAll()

def button_stopRecordAllandBrekel():
    brekel.click_Brekel()
    button_stopRecordAll()

def calibrate():
    IP_ADDRESS = suit_Ip.get()
    start.calibrate_Suit(IP_ADDRESS=IP_ADDRESS)

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1000x800")
app.title("Rokoko Multi Remote Recorder")
app.grid_rowconfigure(10, weight=1)
app.grid_columnconfigure(10, weight=1)

# Use CTkButton instead of tkinter Button
buttonStartAll = customtkinter.CTkButton(master=app, text="Start Recording All", command=button_startRecordAll)
buttonStartAll.place(relx=0.7, rely=0.1, anchor=tkinter.CENTER)

buttonStopAll = customtkinter.CTkButton(master=app, text="Stop Recording All", command=button_stopRecordAll)
buttonStopAll.place(relx=0.9, rely=0.1, anchor=tkinter.CENTER)

buttonStartAllandBrekel = customtkinter.CTkButton(master=app, text="Start Recording All and Brekel", command=button_startRecordAllandBrekel)
buttonStartAllandBrekel.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

buttonStopAllandBrekel = customtkinter.CTkButton(master=app, text="Stop Recording All and Brekel", command=button_stopRecordAllandBrekel)
buttonStopAllandBrekel.place(relx=0.7, rely=0.8, anchor=tkinter.CENTER)

buttonStartBrekel = customtkinter.CTkButton(master=app, text="Start Recording Brekel", command=button_startRecordBrekel)
buttonStartBrekel.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

buttonStopBrekel = customtkinter.CTkButton(master=app, text="Stop Recording Brekel", command=button_stopRecordBrekel)
buttonStopBrekel.place(relx=0.8, rely=0.9, anchor=tkinter.CENTER)

combobox = customtkinter.CTkComboBox(app, values=['60', '100'])
combobox.place(relx=0.3, rely=0.85, anchor=tkinter.CENTER)

# Create entry widget for suit IP Addresses
suit_checkbox = customtkinter.CTkCheckBox(app, text="")
suit_checkbox.place(relx=0.25, rely=0.2, anchor=tkinter.CENTER)
suit_Ip = customtkinter.CTkEntry(app, placeholder_text="0.0.0.0")
suit_Ip.place(relx=0.3, rely=0.2, anchor=tkinter.CENTER)
suit_Ip_label = customtkinter.CTkLabel(app, text="IP Address", fg_color="transparent")
suit_Ip_label.place(relx=0.3, rely=0.15, anchor=tkinter.CENTER)
suit_Name = customtkinter.CTkEntry(app, placeholder_text="")
suit_Name.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
suit_Name_label = customtkinter.CTkLabel(app, text="Character Name", fg_color="transparent")
suit_Name_label.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)
buttonCalibrate = customtkinter.CTkButton(master=app, text="Calibrate", command=calibrate)
buttonCalibrate.place(relx=0.7, rely=0.2, anchor=tkinter.CENTER)

api_Key = customtkinter.CTkEntry(app, placeholder_text="1234")
api_Key.place(relx=0.3, rely=0.8, anchor=tkinter.CENTER)
api_Key_label = customtkinter.CTkLabel(app, text="API Key", fg_color="transparent")
api_Key_label.place(relx=0.15, rely=0.8, anchor=tkinter.CENTER)

port = customtkinter.CTkEntry(app, placeholder_text="80")
port.place(relx=0.3, rely=0.9, anchor=tkinter.CENTER)
api_Key_label = customtkinter.CTkLabel(app, text="Network Port", fg_color="transparent")
api_Key_label.place(relx=0.15, rely=0.9, anchor=tkinter.CENTER)

take_number_label = customtkinter.CTkLabel(app, text=TAKE_NUMBER, fg_color="transparent")
take_number_label.place(relx=0.1, rely=0.9, anchor=tkinter.CENTER)

app.bind('<Return>', lambda event:button_startRecordAll())
app.mainloop()