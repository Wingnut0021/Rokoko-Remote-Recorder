import customtkinter
import rokokoStartRecording as start
import RecordBrekel as brekel
from datetime import datetime
import time
from PIL import Image

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        IP_ADDRESS = ""
        CLIP_NAME = ""
        SCENE_NAME = ""

        def button_startRecordAll():
            TAKE_NUMBER = take_number.get()
            now = datetime.now()
            NOW = now.strftime("%d_%m_%Y_%H_%M_%S")
            suit1_ready = suit_checkbox1.get()
            suit2_ready = suit_checkbox2.get()
            suit3_ready = suit_checkbox3.get()
            suit4_ready = suit_checkbox4.get()
            suit5_ready = suit_checkbox5.get()
            suit6_ready = suit_checkbox6.get()
            brekel_ready = brekel_checkbox.get()
            self.status_textbox.insert("0.0", "Recording Started\n")
            self.timer_label.configure(text=time.time)
            if brekel_ready == 1:
                self.brekel_frame.configure(border_color="red", border_width=3)
                brekel.click_Brekel()
            if suit1_ready == 1:
                self.suit_frame1.configure(border_color="red", border_width=3)
                IP_ADDRESS = suit_Ip1.get()
                CLIP_NAME = suit_Name1.get()
                if int(TAKE_NUMBER) < 10:
                    CLIP_NAME = CLIP_NAME + "_Take0" + str(TAKE_NUMBER) + "_" + NOW
                else:
                    CLIP_NAME = CLIP_NAME + "_Take" + str(TAKE_NUMBER) + "_" + NOW
                start.start_Recording(IP_ADDRESS,CLIP_NAME)
            if suit2_ready == 1:
                self.suit_frame2.configure(border_color="red", border_width=3)
                IP_ADDRESS = suit_Ip2.get()
                CLIP_NAME = suit_Name2.get()
                if int(TAKE_NUMBER) < 10:
                    CLIP_NAME = CLIP_NAME + "_Take0" + str(TAKE_NUMBER) + "_" + NOW
                else:
                    CLIP_NAME = CLIP_NAME + "_Take" + str(TAKE_NUMBER) + "_" + NOW
                start.start_Recording(IP_ADDRESS,CLIP_NAME)
            if suit3_ready == 1:
                self.suit_frame3.configure(border_color="red", border_width=3)
                IP_ADDRESS = suit_Ip3.get()
                CLIP_NAME = suit_Name3.get()
                if int(TAKE_NUMBER) < 10:
                    CLIP_NAME = CLIP_NAME + "_Take0" + str(TAKE_NUMBER) + "_" + NOW
                else:
                    CLIP_NAME = CLIP_NAME + "_Take" + str(TAKE_NUMBER) + "_" + NOW
                start.start_Recording(IP_ADDRESS,CLIP_NAME)
            if suit4_ready == 1:
                self.suit_frame4.configure(border_color="red", border_width=3)
                IP_ADDRESS = suit_Ip4.get()
                CLIP_NAME = suit_Name4.get()
                if int(TAKE_NUMBER) < 10:
                    CLIP_NAME = CLIP_NAME + "_Take0" + str(TAKE_NUMBER) + "_" + NOW
                else:
                    CLIP_NAME = CLIP_NAME + "_Take" + str(TAKE_NUMBER) + "_" + NOW
                start.start_Recording(IP_ADDRESS,CLIP_NAME)
            if suit5_ready == 1:
                self.suit_frame5.configure(border_color="red", border_width=3)
                IP_ADDRESS = suit_Ip5.get()
                CLIP_NAME = suit_Name5.get()
                if int(TAKE_NUMBER) < 10:
                    CLIP_NAME = CLIP_NAME + "_Take0" + str(TAKE_NUMBER) + "_" + NOW
                else:
                    CLIP_NAME = CLIP_NAME + "_Take" + str(TAKE_NUMBER) + "_" + NOW
                start.start_Recording(IP_ADDRESS,CLIP_NAME)
            if suit6_ready == 1:
                self.suit_frame6.configure(border_color="red", border_width=3)
                IP_ADDRESS = suit_Ip6.get()
                CLIP_NAME = suit_Name6.get()
                if int(TAKE_NUMBER) < 10:
                    CLIP_NAME = CLIP_NAME + "_Take0" + str(TAKE_NUMBER) + "_" + NOW
                else:
                    CLIP_NAME = CLIP_NAME + "_Take" + str(TAKE_NUMBER) + "_" + NOW
                start.start_Recording(IP_ADDRESS,CLIP_NAME)
            else:
                print("No devices selected")
                self.timer_label.configure(text="00:00:00")
                self.status_textbox.insert("0.0", "No devices Selected\n")
            return
        def button_stopRecordAll():
            TAKE_NUMBER = take_number.get()
            print(TAKE_NUMBER)
            take_number.delete(first_index=0, last_index=1)
            take_number.delete(first_index=0, last_index=1)
            TAKE_NUMBER = int(TAKE_NUMBER) + 1
            TAKE_NUMBER = str(TAKE_NUMBER)
            take_number.insert(0, TAKE_NUMBER)
            self.timer_label.configure(text="00:00:00")
            self.status_textbox.insert("0.0", "Recording Stopped\n")
            brekel_ready = brekel_checkbox.get()
            self.suit_frame1.configure(border_color="red", border_width=0)
            self.suit_frame2.configure(border_color="red", border_width=0)
            self.suit_frame3.configure(border_color="red", border_width=0)
            self.suit_frame4.configure(border_color="red", border_width=0)
            self.suit_frame5.configure(border_color="red", border_width=0)
            self.suit_frame6.configure(border_color="red", border_width=0)
            self.brekel_frame.configure(border_color="red", border_width=0)
            if brekel_ready == 1:
                brekel.click_Brekel()
            IP_ADDRESS = suit_Ip1.get()
            CLIP_NAME = suit_Name1.get()
            start.stop_Recording(IP_ADDRESS, CLIP_NAME)
            IP_ADDRESS = suit_Ip2.get()
            CLIP_NAME = suit_Name1.get()
            start.stop_Recording(IP_ADDRESS, CLIP_NAME)
            IP_ADDRESS = suit_Ip3.get()
            CLIP_NAME = suit_Name1.get()
            start.stop_Recording(IP_ADDRESS, CLIP_NAME)
            IP_ADDRESS = suit_Ip4.get()
            CLIP_NAME = suit_Name1.get()
            start.stop_Recording(IP_ADDRESS, CLIP_NAME)
            IP_ADDRESS = suit_Ip5.get()
            CLIP_NAME = suit_Name1.get()
            start.stop_Recording(IP_ADDRESS, CLIP_NAME)
            IP_ADDRESS = suit_Ip6.get()
            CLIP_NAME = suit_Name1.get()
            start.stop_Recording(IP_ADDRESS, CLIP_NAME)
            return

        def calibrate1():
            self.status_textbox.insert("0.0", "Calibrating Suit 1\n")
            IP_ADDRESS = suit_Ip1.get()
            start.calibrate_Suit(IP_ADDRESS)

        def calibrate2():
            self.status_textbox.insert("0.0", "Calibrating Suit 2\n")
            IP_ADDRESS = suit_Ip2.get()
            start.calibrate_Suit(IP_ADDRESS)       

        def calibrate3():
            self.status_textbox.insert("0.0", "Calibrating Suit 3\n")
            IP_ADDRESS = suit_Ip3.get()
            start.calibrate_Suit(IP_ADDRESS)  

        def calibrate4():
            self.status_textbox.insert("0.0", "Calibrating Suit 4\n")
            IP_ADDRESS = suit_Ip4.get()
            start.calibrate_Suit(IP_ADDRESS)   

        def calibrate5():
            self.status_textbox.insert("0.0", "Calibrating Suit 5\n")
            IP_ADDRESS = suit_Ip5.get()
            start.calibrate_Suit(IP_ADDRESS)

        def calibrate6():
            self.status_textbox.insert("0.0", "Calibrating Suit 6\n")
            IP_ADDRESS = suit_Ip6.get()
            start.calibrate_Suit(IP_ADDRESS)

        def calibrate():
            self.status_textbox.insert("0.0", "Calibrating All Suits\n")
            IP_ADDRESS = suit_Ip1.get()
            start.calibrate_Suit(IP_ADDRESS)
            IP_ADDRESS = suit_Ip2.get()
            start.calibrate_Suit(IP_ADDRESS)
            IP_ADDRESS = suit_Ip3.get()
            start.calibrate_Suit(IP_ADDRESS)
            IP_ADDRESS = suit_Ip4.get()
            start.calibrate_Suit(IP_ADDRESS)
            IP_ADDRESS = suit_Ip5.get()
            start.calibrate_Suit(IP_ADDRESS)
            IP_ADDRESS = suit_Ip6.get()
            start.calibrate_Suit(IP_ADDRESS)

        def attachTracker():
            IP_ADDRESS = suit_Ip1.get()
            start.attach_tracker(IP_ADDRESS)

        def getInfo1():
            IP_ADDRESS = suit_Ip1.get()
            start.device_info(IP_ADDRESS)
            self.status_textbox.insert("0.0", "Requires upgrade in subscription\n")
        def getInfo2():
            IP_ADDRESS = suit_Ip2.get()
            start.device_info(IP_ADDRESS)
        def getInfo3():
            IP_ADDRESS = suit_Ip3.get()
            start.device_info(IP_ADDRESS)
        def getInfo4():
            IP_ADDRESS = suit_Ip4.get()
            start.device_info(IP_ADDRESS)
        def getInfo5():
            IP_ADDRESS = suit_Ip5.get()
            start.device_info(IP_ADDRESS)
        def getInfo6():
            IP_ADDRESS = suit_Ip6.get()
            start.device_info(IP_ADDRESS)
        
        # Configure Window
        self.title("Rokoko Multi Remote Recorder")
        self.geometry("1100x800")
        self.resizable(True, True)

        # Configure grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3, 4, 5, 6), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19), weight=1)

        # Configure sidebar frame
        self.sidebar_frame = customtkinter.CTkFrame(self, height=800, width=300, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=20, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(0, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Settings", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=1, column=0, padx=20, pady=10)

        scene_Name_label = customtkinter.CTkLabel(self.sidebar_frame, text="Scene Name", fg_color="transparent")
        scene_Name_label.grid(row=2, column=0, padx=20, pady=10)
        scene_Name = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="")
        scene_Name.grid(row=3, column=0, rowspan=1, sticky="nsew", padx=20, pady=10)
        
        take_number_label = customtkinter.CTkLabel(self.sidebar_frame, text="Take Number", fg_color="transparent")
        take_number_label.grid(row=4, column=0, padx=20, pady=10)
        take_number = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="")
        take_number.grid(row=5, column=0, rowspan=1, sticky="nsew", padx=20, pady=10)
        take_number.insert(0, 1)
        
        frameRate_label = customtkinter.CTkLabel(self.sidebar_frame, text="Frame Rate", fg_color="transparent")
        frameRate_label.grid(row=6, column=0, padx=20, pady=10)
        frameRate = customtkinter.CTkComboBox(self.sidebar_frame, values=['60', '100'])
        frameRate.grid(row=7, column=0, padx=20, pady=10)

        api_Key_label = customtkinter.CTkLabel(self.sidebar_frame, text="API Key", fg_color="transparent")
        api_Key_label.grid(row=8, column=0, padx=20, pady=10)
        api_Key = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="1234")
        api_Key.grid(row=9, column=0, padx=20, pady=20)
        api_Key.insert(0, 1234)

        port_label = customtkinter.CTkLabel(self.sidebar_frame, text="Network Port", fg_color="transparent")
        port_label.grid(row=10, column=0, padx=20, pady=10)
        port = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="80")
        port.grid(row=11, column=0, padx=20, pady=20)
        port.insert(0, 14053)

        # Configure suit frames

        self.title_frame = customtkinter.CTkFrame(self, height=50, width=0, corner_radius=16, fg_color="transparent", bg_color="transparent")
        self.title_frame.grid(row=1, column=2, rowspan=1, columnspan=1, sticky="nsew", padx=50)
        self.title_frame.grid_rowconfigure(1, weight=1)
        self.title_label = customtkinter.CTkLabel(self.title_frame, text="Rokoko Remote Multi Recorder", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.title_label.grid(row=1, column=3, padx=10, pady=10)
        
        self.timer_frame = customtkinter.CTkFrame(self, height=70, width=200, corner_radius=8, border_color="grey", border_width=3, fg_color="transparent", bg_color="transparent")
        self.timer_frame.grid(row=1, column=5, rowspan=1, columnspan=1, sticky="nsew", padx=10)
        self.timer_label = customtkinter.CTkLabel(self, text="00:00:00", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.timer_label.grid(row=1, column=5, padx=10, pady=10)
        
        self.suit_frame1 = customtkinter.CTkFrame(self, height=50, width=0, corner_radius=10)   
        self.suit_frame1.grid(row=3, column=2, rowspan=1, columnspan=1, sticky="nsew", padx=50)
        self.suit_frame1.grid_rowconfigure(1, weight=1)
        
        self.suit_frame2 = customtkinter.CTkFrame(self, height=0, width=0, corner_radius=10)
        self.suit_frame2.grid(row=5, column=2, rowspan=1, columnspan=1, sticky="nsew", padx=50)
        self.suit_frame2.grid_rowconfigure(1, weight=1)
        
        self.suit_frame3 = customtkinter.CTkFrame(self, height=0, width=0, corner_radius=10)
        self.suit_frame3.grid(row=7, column=2, rowspan=1, columnspan=1, sticky="nsew", padx=50)
        self.suit_frame3.grid_rowconfigure(1, weight=1)
        
        self.suit_frame4 = customtkinter.CTkFrame(self, height=0, width=0, corner_radius=10)
        self.suit_frame4.grid(row=9, column=2, rowspan=1, columnspan=1, sticky="nsew", padx=50)
        self.suit_frame4.grid_rowconfigure(1, weight=1)
        
        self.suit_frame5 = customtkinter.CTkFrame(self, height=0, width=0, corner_radius=10)
        self.suit_frame5.grid(row=11, column=2, rowspan=1, columnspan=1, sticky="nsew", padx=50)
        self.suit_frame5.grid_rowconfigure(1, weight=1)
        
        self.suit_frame6 = customtkinter.CTkFrame(self, height=0, width=0, corner_radius=10)
        self.suit_frame6.grid(row=13, column=2, rowspan=1, columnspan=1, sticky="nsew", padx=50)
        self.suit_frame6.grid_rowconfigure(1, weight=1)
        
        self.brekel_frame = customtkinter.CTkFrame(self, height=0, width=0, corner_radius=10)
        self.brekel_frame.grid(row=15, column=2, rowspan=1, columnspan=1, sticky="nsew", padx=50)
        self.brekel_frame.grid_rowconfigure(1, weight=1)
        
        self.record_frame = customtkinter.CTkFrame(self, height=0, width=0, corner_radius=10, fg_color="transparent", bg_color="transparent")
        self.record_frame.grid(row=17, column=2, rowspan=1, columnspan=2, sticky="nsew", padx=50)
        self.record_frame.grid_rowconfigure(1, weight=1)
        
        self.text_frame = customtkinter.CTkFrame(self, height=0, width=0, corner_radius=10, fg_color="transparent", bg_color="transparent")
        self.text_frame.grid(row=19, column=2, rowspan=1, columnspan=2, sticky="nsew", padx=50)
        self.text_frame.grid_rowconfigure(1, weight=1)

        buttonStartAll = customtkinter.CTkButton(self.record_frame, text="Start Recording", command=button_startRecordAll)
        buttonStartAll.grid(row=0, column=7, rowspan=1, sticky="nsew", padx=5, pady=10)
        buttonStopAll = customtkinter.CTkButton(self.record_frame, text="Stop Recording", command=button_stopRecordAll)
        buttonStopAll.grid(row=0, column=10, rowspan=1, sticky="nsew", padx=5, pady=10)
        buttonCalibrateAll = customtkinter.CTkButton(self.record_frame, text="Calibrate All", command=calibrate)
        buttonCalibrateAll.grid(row=0, column=13, rowspan=1, sticky="nsew", padx=125, pady=10)

        suit_checkbox1 = customtkinter.CTkCheckBox(self.suit_frame1, text="Suit 1")
        suit_checkbox1.grid(row=0, column=0, rowspan=1, sticky="n", padx=10, pady=10)
        suit_Ip1 = customtkinter.CTkEntry(self.suit_frame1, placeholder_text="IP Address")
        suit_Ip1.grid(row=0, column=1, rowspan=1, sticky="n", padx=5, pady=10)
        suit_Name1 = customtkinter.CTkEntry(self.suit_frame1, placeholder_text="Character Name")
        suit_Name1.grid(row=0, column=2, rowspan=1, sticky="n", padx=5, pady=10)
        buttonCalibrate1 = customtkinter.CTkButton(self.suit_frame1, text="Calibrate", command=calibrate1, width=50)
        buttonCalibrate1.grid(row=0, column=3, rowspan=1, sticky="n", padx=5, pady=10)
        buttonGetInfo1 = customtkinter.CTkButton(self.suit_frame1, text="Info", command=getInfo1, width=50)
        buttonGetInfo1.grid(row=0, column=4, padx=5, pady=10, sticky="n")
        #calibratePose1 = customtkinter.CTkComboBox(self.suit_frame1, values=["straight-arms-down", "straight-arms-forward", "tpose"])
        #calibratePose1.grid(row=0, column=4, rowspan=1, sticky="n", padx=5, pady=10)
        
        suit_checkbox2 = customtkinter.CTkCheckBox(self.suit_frame2, text="Suit 2")
        suit_checkbox2.grid(row=0, column=0, rowspan=1, sticky="nsew", padx=10, pady=10)
        suit_Ip2 = customtkinter.CTkEntry(self.suit_frame2, placeholder_text="IP Address")
        suit_Ip2.grid(row=0, column=1, rowspan=1, sticky="nsew", padx=5, pady=10)
        suit_Name2 = customtkinter.CTkEntry(self.suit_frame2, placeholder_text="Character Name")
        suit_Name2.grid(row=0, column=2, rowspan=1, sticky="nsew", padx=5, pady=10)
        buttonCalibrate2 = customtkinter.CTkButton(self.suit_frame2, text="Calibrate", command=calibrate2, width=50)
        buttonCalibrate2.grid(row=0, column=3, rowspan=1, sticky="nsew", padx=5, pady=10)
        buttonGetInfo2 = customtkinter.CTkButton(self.suit_frame2, text="Info", command=getInfo2, width=50)
        buttonGetInfo2.grid(row=0, column=4, padx=5, pady=10, sticky="n")

        suit_checkbox3 = customtkinter.CTkCheckBox(self.suit_frame3, text="Suit 3")
        suit_checkbox3.grid(row=0, column=0, rowspan=1, sticky="nsew", padx=10, pady=10)
        suit_Ip3 = customtkinter.CTkEntry(self.suit_frame3, placeholder_text="IP Address")
        suit_Ip3.grid(row=0, column=1, rowspan=1, sticky="nsew", padx=5, pady=10)
        suit_Name3 = customtkinter.CTkEntry(self.suit_frame3, placeholder_text="Character Name")
        suit_Name3.grid(row=0, column=2, rowspan=1, sticky="nsew", padx=5, pady=10)
        buttonCalibrate3 = customtkinter.CTkButton(self.suit_frame3, text="Calibrate", command=calibrate3, width=50)
        buttonCalibrate3.grid(row=0, column=3, rowspan=1, sticky="nsew", padx=5, pady=10)
        buttonGetInfo3 = customtkinter.CTkButton(self.suit_frame3, text="Info", command=getInfo3, width=50)
        buttonGetInfo3.grid(row=0, column=4, padx=5, pady=10, sticky="n")

        suit_checkbox4 = customtkinter.CTkCheckBox(self.suit_frame4, text="Suit 4")
        suit_checkbox4.grid(row=0, column=0, rowspan=1, sticky="nsew", padx=10, pady=10)
        suit_Ip4 = customtkinter.CTkEntry(self.suit_frame4, placeholder_text="IP Address")
        suit_Ip4.grid(row=0, column=1, rowspan=1, sticky="nsew", padx=5, pady=10)
        suit_Name4 = customtkinter.CTkEntry(self.suit_frame4, placeholder_text="Character Name")
        suit_Name4.grid(row=0, column=2, rowspan=1, sticky="nsew", padx=5, pady=10)
        buttonCalibrate4 = customtkinter.CTkButton(self.suit_frame4, text="Calibrate", command=calibrate4, width=50)
        buttonCalibrate4.grid(row=0, column=3, rowspan=1, sticky="nsew", padx=5, pady=10)
        buttonGetInfo4 = customtkinter.CTkButton(self.suit_frame4, text="Info", command=getInfo4, width=50)
        buttonGetInfo4.grid(row=0, column=4, padx=5, pady=10, sticky="n")

        suit_checkbox5 = customtkinter.CTkCheckBox(self.suit_frame5, text="Suit 5")
        suit_checkbox5.grid(row=0, column=0, rowspan=1, sticky="nsew", padx=10, pady=10)
        suit_Ip5 = customtkinter.CTkEntry(self.suit_frame5, placeholder_text="IP Address")
        suit_Ip5.grid(row=0, column=1, rowspan=1, sticky="nsew", padx=5, pady=10)
        suit_Name5 = customtkinter.CTkEntry(self.suit_frame5, placeholder_text="Character Name")
        suit_Name5.grid(row=0, column=2, rowspan=1, sticky="nsew", padx=5, pady=10)
        buttonCalibrate5 = customtkinter.CTkButton(self.suit_frame5, text="Calibrate", command=calibrate5, width=50)
        buttonCalibrate5.grid(row=0, column=3, rowspan=1, sticky="nsew", padx=5, pady=10)
        buttonGetInfo5 = customtkinter.CTkButton(self.suit_frame5, text="Info", command=getInfo5, width=50)
        buttonGetInfo5.grid(row=0, column=4, padx=5, pady=10, sticky="n")

        suit_checkbox6 = customtkinter.CTkCheckBox(self.suit_frame6, text="Suit 6")
        suit_checkbox6.grid(row=0, column=0, rowspan=1, sticky="nsew", padx=10, pady=10)
        suit_Ip6 = customtkinter.CTkEntry(self.suit_frame6, placeholder_text="IP Address")
        suit_Ip6.grid(row=0, column=1, rowspan=1, sticky="nsew", padx=5, pady=10)
        suit_Name6 = customtkinter.CTkEntry(self.suit_frame6, placeholder_text="Character Name")
        suit_Name6.grid(row=0, column=2, rowspan=1, sticky="nsew", padx=5, pady=10)
        buttonCalibrate6 = customtkinter.CTkButton(self.suit_frame6, text="Calibrate", command=calibrate6, width=50)
        buttonCalibrate6.grid(row=0, column=3, rowspan=1, sticky="nsew", padx=5, pady=10)
        buttonGetInfo6 = customtkinter.CTkButton(self.suit_frame6, text="Info", command=getInfo6, width=50)
        buttonGetInfo6.grid(row=0, column=4, padx=5, pady=10, sticky="n")

        brekel_checkbox = customtkinter.CTkCheckBox(self.brekel_frame, text="Brekel")
        brekel_checkbox.grid(row=0, column=0, rowspan=1, sticky="nsew", padx=10, pady=10)
        brekel_Ip = customtkinter.CTkEntry(self.brekel_frame, placeholder_text="127.0.0.1")
        brekel_Ip.grid(row=0, column=1, rowspan=1, sticky="nsew", padx=5, pady=10)
        brekel_Ip.configure(state="disabled")
        brekel_label = customtkinter.CTkLabel(self.brekel_frame, text="Not currently implemented with API, Requires AutoHotKey", fg_color="transparent", bg_color="transparent")
        brekel_label.grid(row=0, column=2, rowspan=1, sticky="nsew", padx=5, pady=10)

        self.status_textbox = customtkinter.CTkTextbox(self.text_frame, height=100, width=700)
        self.status_textbox.grid(row=0, column=2, padx=(0, 0), pady=(0, 0), sticky="nsew")
        
        
        suitImage = customtkinter.CTkImage(self.suit_frame1, dark_image=Image.open("human.svg"), size=(30, 30))
        suitImage.grid(row=0, column=2, padx=(0, 0), pady=(0, 0), sticky="nsew")
        #buttonAttachTracker = customtkinter.CTkButton(self.suit_frame6, text="Attach Tracker", command=attachTracker)
        #buttonAttachTracker.grid(row=0, column=4, padx=(0, 0), pady=(0, 0), sticky="nsew")
        
        


if __name__ == "__main__":
    app = App()
    app.mainloop()