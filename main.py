import tkinter
import customtkinter
import rokokoStartRecording as start
import RecordBrekel as brekel
from datetime import datetime


IP_ADDRESS_1 = ""
IP_ADDRESS_2 = ""
IP_ADDRESS_3 = ""
IP_ADDRESS_4 = ""
IP_ADDRESS_5 = ""
IP_ADDRESS_6 = ""
CLIP_NAME_1 = ""
CLIP_NAME_2 = ""
CLIP_NAME_3 = ""
CLIP_NAME_4 = ""
CLIP_NAME_5 = ""
CLIP_NAME_6 = ""

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
app.geometry("1000x800")
app.title("Rokoko Multi Remote Recorder")
app.grid_rowconfigure(10, weight=1)
app.grid_columnconfigure(10, weight=1)

def button_startRecordAll():
    now = datetime.now()
    NOW = now.strftime("%d_%m_%Y_%H_%M_%S")
    print(NOW)
    
    IP_ADDRESS_1 = suit1_Ip.get()
    CLIP_NAME_1 = suit1_Name.get()
    CLIP_NAME_1 = CLIP_NAME_1 + NOW
    start.start_Recording(IP_ADDRESS=IP_ADDRESS_1,CLIP_NAME=CLIP_NAME_1)
    IP_ADDRESS_2 = suit2_Ip.get()
    CLIP_NAME_2 = suit2_Name.get()
    start.start_Recording(IP_ADDRESS=IP_ADDRESS_2,CLIP_NAME=CLIP_NAME_2)
    IP_ADDRESS_3 = suit3_Ip.get()
    CLIP_NAME_3 = suit3_Name.get()
    start.start_Recording(IP_ADDRESS=IP_ADDRESS_3,CLIP_NAME=CLIP_NAME_3)
    IP_ADDRESS_4 = suit4_Ip.get()
    CLIP_NAME_4 = suit4_Name.get()
    start.start_Recording(IP_ADDRESS=IP_ADDRESS_4,CLIP_NAME=CLIP_NAME_4)
    IP_ADDRESS_5 = suit5_Ip.get()
    CLIP_NAME_5 = suit5_Name.get()
    start.start_Recording(IP_ADDRESS=IP_ADDRESS_5,CLIP_NAME=CLIP_NAME_5)
    IP_ADDRESS_6 = suit6_Ip.get()
    CLIP_NAME_6 = suit6_Name.get()
    start.start_Recording(IP_ADDRESS=IP_ADDRESS_6,CLIP_NAME=CLIP_NAME_6)

def button_stopRecordAll():
    IP_ADDRESS_1 = suit1_Ip.get()
    start.stop_Recording(IP_ADDRESS=IP_ADDRESS_1,CLIP_NAME=CLIP_NAME_1)
    IP_ADDRESS_2 = suit2_Ip.get()
    start.stop_Recording(IP_ADDRESS=IP_ADDRESS_2,CLIP_NAME=CLIP_NAME_2)
    IP_ADDRESS_3 = suit3_Ip.get()
    start.stop_Recording(IP_ADDRESS=IP_ADDRESS_3,CLIP_NAME=CLIP_NAME_3)
    IP_ADDRESS_4 = suit4_Ip.get()
    start.stop_Recording(IP_ADDRESS=IP_ADDRESS_4,CLIP_NAME=CLIP_NAME_4)
    IP_ADDRESS_5 = suit5_Ip.get()
    start.stop_Recording(IP_ADDRESS=IP_ADDRESS_5,CLIP_NAME=CLIP_NAME_5)
    IP_ADDRESS_6 = suit6_Ip.get()
    start.stop_Recording(IP_ADDRESS=IP_ADDRESS_6,CLIP_NAME=CLIP_NAME_6)

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
    
def calibrate_1():
    IP_ADDRESS_1 = suit1_Ip.get()
    start.calibrate_Suit(IP_ADDRESS=IP_ADDRESS_1)
    
def calibrate_2():
    IP_ADDRESS_2 = suit2_Ip.get()
    start.calibrate_Suit(IP_ADDRESS=IP_ADDRESS_2)

def calibrate_3():
    IP_ADDRESS_3 = suit3_Ip.get()
    start.calibrate_Suit(IP_ADDRESS=IP_ADDRESS_3)

def calibrate_4():
    IP_ADDRESS_4 = suit4_Ip.get()
    start.calibrate_Suit(IP_ADDRESS=IP_ADDRESS_4)

def calibrate_5():
    IP_ADDRESS_5 = suit5_Ip.get()
    start.calibrate_Suit(IP_ADDRESS=IP_ADDRESS_5)

def calibrate_6():
    IP_ADDRESS_6 = suit6_Ip.get()
    start.calibrate_Suit(IP_ADDRESS=IP_ADDRESS_6)
    
def calibrate_All():
    calibrate_1()
    calibrate_2()
    calibrate_3()
    calibrate_4()
    calibrate_5()
    calibrate_6()



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

combobox = customtkinter.CTkComboBox(app, values=['60', '100'], command=combobox_callback)
combobox.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

# calibrate suits
buttonCalibrateAll = customtkinter.CTkButton(master=app, text="Calibrate All Suits", command=calibrate_All)
buttonCalibrateAll.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

buttonCalibrate1 = customtkinter.CTkButton(master=app, text="Calibrate Suit 1", command=calibrate_1)
buttonCalibrate1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

buttonCalibrate2 = customtkinter.CTkButton(master=app, text="Calibrate Suit 2", command=calibrate_2)
buttonCalibrate2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

buttonCalibrate3 = customtkinter.CTkButton(master=app, text="Calibrate Suit 3", command=calibrate_3)
buttonCalibrate3.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

buttonCalibrate4 = customtkinter.CTkButton(master=app, text="Calibrate Suit 4", command=calibrate_4)
buttonCalibrate4.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

buttonCalibrate5 = customtkinter.CTkButton(master=app, text="Calibrate Suit 5", command=calibrate_5)
buttonCalibrate5.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

buttonCalibrate6 = customtkinter.CTkButton(master=app, text="Calibrate Suit 6", command=calibrate_6)
buttonCalibrate6.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

# Create entry widget for suit IP Addresses
suit1_Ip = customtkinter.CTkEntry(app, placeholder_text="0.0.0.0")
suit1_Ip.place(relx=0.3, rely=0.2, anchor=tkinter.CENTER)
suit1_Ip_label = customtkinter.CTkLabel(app, text="Suit 1 IP Address", fg_color="transparent")
suit1_Ip_label.place(relx=0.15, rely=0.2, anchor=tkinter.CENTER)
suit1_Name = customtkinter.CTkEntry(app, placeholder_text="Character Name")
suit1_Name.place(relx=0.9, rely=0.2, anchor=tkinter.CENTER)
suit1_Name_label = customtkinter.CTkLabel(app, text="Character Name", fg_color="transparent")
suit1_Name_label.place(relx=0.75, rely=0.2, anchor=tkinter.CENTER)

suit2_Ip = customtkinter.CTkEntry(app, placeholder_text="0.0.0.0")
suit2_Ip.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)
suit2_Ip_label = customtkinter.CTkLabel(app, text="Suit 2 IP Address", fg_color="transparent")
suit2_Ip_label.place(relx=0.15, rely=0.3, anchor=tkinter.CENTER)
suit2_Name = customtkinter.CTkEntry(app, placeholder_text="Character Name")
suit2_Name.place(relx=0.9, rely=0.3, anchor=tkinter.CENTER)
suit2_Name_label = customtkinter.CTkLabel(app, text="Character Name", fg_color="transparent")
suit2_Name_label.place(relx=0.75, rely=0.3, anchor=tkinter.CENTER)

suit3_Ip = customtkinter.CTkEntry(app, placeholder_text="0.0.0.0")
suit3_Ip.place(relx=0.3, rely=0.4, anchor=tkinter.CENTER)
suit3_Ip_label = customtkinter.CTkLabel(app, text="Suit 2 IP Address", fg_color="transparent")
suit3_Ip_label.place(relx=0.15, rely=0.4, anchor=tkinter.CENTER)
suit3_Name = customtkinter.CTkEntry(app, placeholder_text="Character Name")
suit3_Name.place(relx=0.9, rely=0.4, anchor=tkinter.CENTER)
suit3_Name_label = customtkinter.CTkLabel(app, text="Character Name", fg_color="transparent")
suit3_Name_label.place(relx=0.75, rely=0.4, anchor=tkinter.CENTER)

suit4_Ip = customtkinter.CTkEntry(app, placeholder_text="0.0.0.0")
suit4_Ip.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)
suit4_Ip_label = customtkinter.CTkLabel(app, text="Suit 4 IP Address", fg_color="transparent")
suit4_Ip_label.place(relx=0.15, rely=0.5, anchor=tkinter.CENTER)
suit4_Name = customtkinter.CTkEntry(app, placeholder_text="Character Name")
suit4_Name.place(relx=0.9, rely=0.5, anchor=tkinter.CENTER)
suit4_Name_label = customtkinter.CTkLabel(app, text="Character Name", fg_color="transparent")
suit4_Name_label.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

suit5_Ip = customtkinter.CTkEntry(app, placeholder_text="0.0.0.0")
suit5_Ip.place(relx=0.3, rely=0.6, anchor=tkinter.CENTER)
suit5_Ip_label = customtkinter.CTkLabel(app, text="Suit 5 IP Address", fg_color="transparent")
suit5_Ip_label.place(relx=0.15, rely=0.6, anchor=tkinter.CENTER)
suit5_Name = customtkinter.CTkEntry(app, placeholder_text="Character Name")
suit5_Name.place(relx=0.9, rely=0.6, anchor=tkinter.CENTER)
suit5_Name_label = customtkinter.CTkLabel(app, text="Character Name", fg_color="transparent")
suit5_Name_label.place(relx=0.75, rely=0.6, anchor=tkinter.CENTER)

suit6_Ip = customtkinter.CTkEntry(app, placeholder_text="0.0.0.0")
suit6_Ip.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)
suit6_Ip_label = customtkinter.CTkLabel(app, text="Suit 6 IP Address", fg_color="transparent")
suit6_Ip_label.place(relx=0.15, rely=0.7, anchor=tkinter.CENTER)
suit6_Name = customtkinter.CTkEntry(app, placeholder_text="Character Name")
suit6_Name.place(relx=0.9, rely=0.7, anchor=tkinter.CENTER)
suit6_Name_label = customtkinter.CTkLabel(app, text="Character Name", fg_color="transparent")
suit6_Name_label.place(relx=0.75, rely=0.7, anchor=tkinter.CENTER)

api_Key = customtkinter.CTkEntry(app, placeholder_text="1234")
api_Key.place(relx=0.3, rely=0.8, anchor=tkinter.CENTER)
api_Key_label = customtkinter.CTkLabel(app, text="API Key", fg_color="transparent")
api_Key_label.place(relx=0.15, rely=0.8, anchor=tkinter.CENTER)

port = customtkinter.CTkEntry(app, placeholder_text="80")
port.place(relx=0.3, rely=0.9, anchor=tkinter.CENTER)
api_Key_label = customtkinter.CTkLabel(app, text="Network Port", fg_color="transparent")
api_Key_label.place(relx=0.15, rely=0.9, anchor=tkinter.CENTER)

#IP_ADDRESS_1 = suit1_Ip.get()
#IP_ADDRESS_2 = suit2_Ip.get()

app.bind('<Return>', lambda event:button_startRecordAll())
app.mainloop()