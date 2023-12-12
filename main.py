import customtkinter
import rokokoStartRecording as start
import RecordBrekel as brekel
from datetime import datetime
import time
import os
from PIL import Image

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        IP_ADDRESS = ""
        CLIP_NAME = ""
        SCENE_NAME = ""
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        
        def button_startRecordAll():
            TAKE_NUMBER = take_number.get().zfill(2)
            PART_NUMBER = part_number.get().zfill(2)
            NOW = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
            self.status_textbox.insert("0.0", "Recording Started\n")
            self.timer_label.configure(text=time.time)
            if brekel_checkbox.get() == 1:
                self.brekel_frame.configure(border_color="red", border_width=3)
                brekel.click_Brekel()
            if suit_checkbox1.get() == 1:
                self.suit_frame1.configure(border_color="red", border_width=3)
                IP_ADDRESS = suit_Ip1.get()
                CLIP_NAME = suit_Name1.get() + "_P" + PART_NUMBER + "_Take" + str(TAKE_NUMBER) + "_" + NOW
                start.start_Recording(IP_ADDRESS,CLIP_NAME)
            if suit_checkbox2.get() == 1:
                self.suit_frame2.configure(border_color="red", border_width=3)
                IP_ADDRESS = suit_Ip2.get()
                CLIP_NAME = suit_Name2.get() + "_P" + PART_NUMBER + "_Take" + str(TAKE_NUMBER) + "_" + NOW
                start.start_Recording(IP_ADDRESS,CLIP_NAME)
            if suit_checkbox3.get() == 1:
                self.suit_frame3.configure(border_color="red", border_width=3)
                IP_ADDRESS = suit_Ip3.get()
                CLIP_NAME = suit_Name3.get() + "_P" + PART_NUMBER + "_Take" + str(TAKE_NUMBER) + "_" + NOW
                start.start_Recording(IP_ADDRESS,CLIP_NAME)
            if suit_checkbox4.get() == 1:
                self.suit_frame4.configure(border_color="red", border_width=3)
                IP_ADDRESS = suit_Ip4.get()
                CLIP_NAME = suit_Name4.get() + "_P" + PART_NUMBER + "_Take" + str(TAKE_NUMBER) + "_" + NOW
                start.start_Recording(IP_ADDRESS,CLIP_NAME)
            if suit_checkbox5.get() == 1:
                self.suit_frame5.configure(border_color="red", border_width=3)
                IP_ADDRESS = suit_Ip5.get()
                CLIP_NAME = suit_Name5.get() + "_P" + PART_NUMBER + "_Take" + str(TAKE_NUMBER) + "_" + NOW
                start.start_Recording(IP_ADDRESS,CLIP_NAME)
            if suit_checkbox6.get() == 1:
                self.suit_frame6.configure(border_color="red", border_width=3)
                IP_ADDRESS = suit_Ip6.get()
                CLIP_NAME = suit_Name6.get() + "_P" + PART_NUMBER + "_Take" + str(TAKE_NUMBER) + "_" + NOW
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
        self.sidebar_frame.grid(row=0, column=0, rowspan=19, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(0, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Settings", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=1, column=0, padx=10, pady=0)

        scene_Name_label = customtkinter.CTkLabel(self.sidebar_frame, text="Scene Name", fg_color="transparent")
        scene_Name_label.grid(row=2, column=0, padx=10, pady=0)
        scene_Name = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="")
        scene_Name.grid(row=3, column=0, rowspan=1, sticky="nsew", padx=10, pady=0)
        
        take_number_label = customtkinter.CTkLabel(self.sidebar_frame, text="Take Number", fg_color="transparent")
        take_number_label.grid(row=4, column=0, padx=10, pady=0)
        take_number = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="")
        take_number.grid(row=5, column=0, rowspan=1, sticky="nsew", padx=10, pady=0)
        take_number.insert(0, 1)

        part_number_label = customtkinter.CTkLabel(self.sidebar_frame, text="Part Number", fg_color="transparent")
        part_number_label.grid(row=6, column=0, padx=10, pady=0)
        part_number = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="")
        part_number.grid(row=7, column=0, rowspan=1, sticky="nsew", padx=10, pady=0)
        part_number.insert(0, 1)

        frameRate_label = customtkinter.CTkLabel(self.sidebar_frame, text="Frame Rate", fg_color="transparent")
        frameRate_label.grid(row=8, column=0, padx=10, pady=0)
        frameRate = customtkinter.CTkComboBox(self.sidebar_frame, values=['60', '100'])
        frameRate.grid(row=9, column=0, padx=10, pady=0)

        api_Key_label = customtkinter.CTkLabel(self.sidebar_frame, text="API Key", fg_color="transparent")
        api_Key_label.grid(row=10, column=0, padx=10, pady=0)
        api_Key = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="1234")
        api_Key.grid(row=11, column=0, padx=10, pady=0)
        api_Key.insert(0, 1234)

        port_label = customtkinter.CTkLabel(self.sidebar_frame, text="Network Port", fg_color="transparent")
        port_label.grid(row=12, column=0, padx=10, pady=0)
        port = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="80")
        port.grid(row=13, column=0, padx=10, pady=(0, 20))
        port.insert(0, 14053)

        # Configure suit frames

        self.title_frame = customtkinter.CTkFrame(self, height=50, width=0, corner_radius=16, fg_color="transparent", bg_color="transparent")
        self.title_frame.grid(row=1, column=2, rowspan=1, columnspan=3, sticky="nsew", padx=50)
        self.title_frame.grid_rowconfigure(1, weight=1)
        self.title_label = customtkinter.CTkLabel(self.title_frame, text="Rokoko Remote Multi Recorder", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.title_label.grid(row=1, column=1, padx=10, pady=10)
        
        self.timer_frame = customtkinter.CTkFrame(self.title_frame, height=70, width=200, corner_radius=8, border_color="grey", border_width=3, fg_color="transparent", bg_color="transparent")
        self.timer_frame.grid(row=1, column=2, rowspan=1, columnspan=1, sticky="nsew", padx=180)
        self.timer_label = customtkinter.CTkLabel(self.timer_frame, text="00:00:00", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.timer_label.grid(row=1, column=1, padx=30, pady=(20,0))
        
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
        
        #self.brekel_frame = customtkinter.CTkFrame(self, height=0, width=0, corner_radius=10)
        #self.brekel_frame.grid(row=15, column=2, rowspan=1, columnspan=1, sticky="nsew", padx=50)
        #self.brekel_frame.grid_rowconfigure(1, weight=1)
        
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
        suit_checkbox1.grid(row=0, column=0, rowspan=1, sticky="nsew", padx=(10, 0), pady=(15, 0))
        suit_Ip1 = customtkinter.CTkEntry(self.suit_frame1, placeholder_text="IP Address")
        suit_Ip1.grid(row=0, column=1, rowspan=1, sticky="nsew", padx=(0, 0), pady=(15, 0))
        suit_Name1 = customtkinter.CTkEntry(self.suit_frame1, placeholder_text="Character Name")
        suit_Name1.grid(row=0, column=2, rowspan=1, sticky="nsew", padx=5, pady=(15, 0))
        buttonCalibrate1 = customtkinter.CTkButton(self.suit_frame1, text="Calibrate", command=calibrate1, width=50)
        buttonCalibrate1.grid(row=0, column=3, rowspan=1, sticky="nsew", padx=5, pady=(15, 0))
        buttonGetInfo1 = customtkinter.CTkButton(self.suit_frame1, text="Info", command=getInfo1, width=50)
        buttonGetInfo1.grid(row=0, column=4, padx=5, pady=(15, 0), sticky="n")
        #calibratePose1 = customtkinter.CTkComboBox(self.suit_frame1, values=["straight-arms-down", "straight-arms-forward", "tpose"])
        #calibratePose1.grid(row=0, column=4, rowspan=1, sticky="n", padx=5, pady=10)
        
        suit_checkbox2 = customtkinter.CTkCheckBox(self.suit_frame2, text="Suit 2")
        suit_checkbox2.grid(row=0, column=0, rowspan=1, sticky="nsew", padx=(10, 0), pady=(15, 0))
        suit_Ip2 = customtkinter.CTkEntry(self.suit_frame2, placeholder_text="IP Address")
        suit_Ip2.grid(row=0, column=1, rowspan=1, sticky="nsew", padx=(0, 0), pady=(15, 0))
        suit_Name2 = customtkinter.CTkEntry(self.suit_frame2, placeholder_text="Character Name")
        suit_Name2.grid(row=0, column=2, rowspan=1, sticky="nsew", padx=5, pady=(15, 0))
        buttonCalibrate2 = customtkinter.CTkButton(self.suit_frame2, text="Calibrate", command=calibrate2, width=50)
        buttonCalibrate2.grid(row=0, column=3, rowspan=1, sticky="nsew", padx=5, pady=(15, 0))
        buttonGetInfo2 = customtkinter.CTkButton(self.suit_frame2, text="Info", command=getInfo2, width=50)
        buttonGetInfo2.grid(row=0, column=4, padx=5, pady=(15, 0), sticky="n")

        suit_checkbox3 = customtkinter.CTkCheckBox(self.suit_frame3, text="Suit 3")
        suit_checkbox3.grid(row=0, column=0, rowspan=1, sticky="nsew", padx=(10, 0), pady=(15, 0))
        suit_Ip3 = customtkinter.CTkEntry(self.suit_frame3, placeholder_text="IP Address")
        suit_Ip3.grid(row=0, column=1, rowspan=1, sticky="nsew", padx=(0, 0), pady=(15, 0))
        suit_Name3 = customtkinter.CTkEntry(self.suit_frame3, placeholder_text="Character Name")
        suit_Name3.grid(row=0, column=2, rowspan=1, sticky="nsew", padx=5, pady=(15, 0))
        buttonCalibrate3 = customtkinter.CTkButton(self.suit_frame3, text="Calibrate", command=calibrate3, width=50)
        buttonCalibrate3.grid(row=0, column=3, rowspan=1, sticky="nsew", padx=5, pady=(15, 0))
        buttonGetInfo3 = customtkinter.CTkButton(self.suit_frame3, text="Info", command=getInfo3, width=50)
        buttonGetInfo3.grid(row=0, column=4, padx=5, pady=(15, 0), sticky="n")

        suit_checkbox4 = customtkinter.CTkCheckBox(self.suit_frame4, text="Suit 4")
        suit_checkbox4.grid(row=0, column=0, rowspan=1, sticky="nsew", padx=(10, 0), pady=(15, 0))
        suit_Ip4 = customtkinter.CTkEntry(self.suit_frame4, placeholder_text="IP Address")
        suit_Ip4.grid(row=0, column=1, rowspan=1, sticky="nsew", padx=(0, 0), pady=(15, 0))
        suit_Name4 = customtkinter.CTkEntry(self.suit_frame4, placeholder_text="Character Name")
        suit_Name4.grid(row=0, column=2, rowspan=1, sticky="nsew", padx=5, pady=(15, 0))
        buttonCalibrate4 = customtkinter.CTkButton(self.suit_frame4, text="Calibrate", command=calibrate4, width=50)
        buttonCalibrate4.grid(row=0, column=3, rowspan=1, sticky="nsew", padx=5, pady=(15, 0))
        buttonGetInfo4 = customtkinter.CTkButton(self.suit_frame4, text="Info", command=getInfo4, width=50)
        buttonGetInfo4.grid(row=0, column=4, padx=5, pady=(15, 0), sticky="n")

        suit_checkbox5 = customtkinter.CTkCheckBox(self.suit_frame5, text="Suit 5")
        suit_checkbox5.grid(row=0, column=0, rowspan=1, sticky="nsew", padx=(10, 0), pady=(15, 0))
        suit_Ip5 = customtkinter.CTkEntry(self.suit_frame5, placeholder_text="IP Address")
        suit_Ip5.grid(row=0, column=1, rowspan=1, sticky="nsew", padx=(0, 0), pady=(15, 0))
        suit_Name5 = customtkinter.CTkEntry(self.suit_frame5, placeholder_text="Character Name")
        suit_Name5.grid(row=0, column=2, rowspan=1, sticky="nsew", padx=5, pady=(15, 0))
        buttonCalibrate5 = customtkinter.CTkButton(self.suit_frame5, text="Calibrate", command=calibrate5, width=50)
        buttonCalibrate5.grid(row=0, column=3, rowspan=1, sticky="nsew", padx=5, pady=(15, 0))
        buttonGetInfo5 = customtkinter.CTkButton(self.suit_frame5, text="Info", command=getInfo5, width=50)
        buttonGetInfo5.grid(row=0, column=4, padx=5, pady=(15, 0), sticky="n")

        suit_checkbox6 = customtkinter.CTkCheckBox(self.suit_frame6, text="Suit 6")
        suit_checkbox6.grid(row=0, column=0, rowspan=1, sticky="nsew", padx=(10, 0), pady=(15, 0))
        suit_Ip6 = customtkinter.CTkEntry(self.suit_frame6, placeholder_text="IP Address")
        suit_Ip6.grid(row=0, column=1, rowspan=1, sticky="nsew", padx=(0, 0), pady=(15, 0))
        suit_Name6 = customtkinter.CTkEntry(self.suit_frame6, placeholder_text="Character Name")
        suit_Name6.grid(row=0, column=2, rowspan=1, sticky="nsew", padx=5, pady=(15, 0))
        buttonCalibrate6 = customtkinter.CTkButton(self.suit_frame6, text="Calibrate", command=calibrate6, width=50)
        buttonCalibrate6.grid(row=0, column=3, rowspan=1, sticky="nsew", padx=5, pady=(15, 0))
        buttonGetInfo6 = customtkinter.CTkButton(self.suit_frame6, text="Info", command=getInfo6, width=50)
        buttonGetInfo6.grid(row=0, column=4, padx=5, pady=(15, 0), sticky="n")

        #brekel_checkbox = customtkinter.CTkCheckBox(self.brekel_frame, text="Brekel")
        #brekel_checkbox.grid(row=0, column=0, rowspan=1, sticky="nsew", padx=(10, 0), pady=(15, 0))
        #brekel_Ip = customtkinter.CTkEntry(self.brekel_frame, placeholder_text="127.0.0.1")
        #brekel_Ip.grid(row=0, column=1, rowspan=1, sticky="nsew", padx=(0, 0), pady=(15, 0))
        #brekel_Ip.configure(state="disabled")
        #brekel_label = customtkinter.CTkLabel(self.brekel_frame, text="Not currently implemented with API, Requires AutoHotKey", fg_color="transparent", bg_color="transparent")
        #brekel_label.grid(row=0, column=2, rowspan=1, sticky="nsew", padx=5, pady=(15, 0))

        self.status_textbox = customtkinter.CTkTextbox(self.text_frame, height=100, width=700)
        self.status_textbox.grid(row=0, column=2, padx=(0, 0), pady=(0, 0), sticky="nsew")
        
        
        suitImage1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "human.png")), size=(26, 26))
        suitImage1_label = customtkinter.CTkLabel(self.suit_frame1, image=suitImage1, text="")
        suitImage1_label.grid(row=0, column=5, padx=1, pady=(15, 0), sticky="n")
        gloveLImage1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hand-back-left-outline.png")), size=(26, 26))
        gloveLImage1_label = customtkinter.CTkLabel(self.suit_frame1, image=gloveLImage1, text="")
        gloveLImage1_label.grid(row=0, column=6, padx=1, pady=(15, 0), sticky="n")
        gloveRImage1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hand-back-right-outline.png")), size=(26, 26))
        gloveRImage1_label = customtkinter.CTkLabel(self.suit_frame1, image=gloveRImage1, text="")
        gloveRImage1_label.grid(row=0, column=7, padx=1, pady=(15, 0), sticky="n")
        
        suitImage2 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "human.png")), size=(26, 26))
        suitImage2_label = customtkinter.CTkLabel(self.suit_frame2, image=suitImage2, text="")
        suitImage2_label.grid(row=0, column=5, padx=1, pady=(15, 0), sticky="n")
        gloveLImage2 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hand-back-left-outline.png")), size=(26, 26))
        gloveLImage2_label = customtkinter.CTkLabel(self.suit_frame2, image=gloveLImage2, text="")
        gloveLImage2_label.grid(row=0, column=6, padx=1, pady=(15, 0), sticky="n")
        gloveRImage2 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hand-back-right-outline.png")), size=(26, 26))
        gloveRImage2_label = customtkinter.CTkLabel(self.suit_frame2, image=gloveRImage2, text="")
        gloveRImage2_label.grid(row=0, column=7, padx=1, pady=(15, 0), sticky="n")
        
        suitImage3 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "human.png")), size=(26, 26))
        suitImage3_label = customtkinter.CTkLabel(self.suit_frame3, image=suitImage3, text="")
        suitImage3_label.grid(row=0, column=5, padx=1, pady=(15, 0), sticky="n")
        gloveLImage3 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hand-back-left-outline.png")), size=(26, 26))
        gloveLImage3_label = customtkinter.CTkLabel(self.suit_frame3, image=gloveLImage3, text="")
        gloveLImage3_label.grid(row=0, column=6, padx=1, pady=(15, 0), sticky="n")
        gloveRImage3 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hand-back-right-outline.png")), size=(26, 26))
        gloveRImage3_label = customtkinter.CTkLabel(self.suit_frame3, image=gloveRImage3, text="")
        gloveRImage3_label.grid(row=0, column=7, padx=1, pady=(15, 0), sticky="n")
        
        suitImage4 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "human.png")), size=(26, 26))
        suitImage4_label = customtkinter.CTkLabel(self.suit_frame4, image=suitImage1, text="")
        suitImage4_label.grid(row=0, column=5, padx=1, pady=(15, 0), sticky="n")
        gloveLImage4 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hand-back-left-outline.png")), size=(26, 26))
        gloveLImage4_label = customtkinter.CTkLabel(self.suit_frame4, image=gloveLImage4, text="")
        gloveLImage4_label.grid(row=0, column=6, padx=1, pady=(15, 0), sticky="n")
        gloveRImage4 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hand-back-right-outline.png")), size=(26, 26))
        gloveRImage4_label = customtkinter.CTkLabel(self.suit_frame4, image=gloveRImage4, text="")
        gloveRImage4_label.grid(row=0, column=7, padx=1, pady=(15, 0), sticky="n")
        
        suitImage5 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "human.png")), size=(26, 26))
        suitImage5_label = customtkinter.CTkLabel(self.suit_frame5, image=suitImage5, text="")
        suitImage5_label.grid(row=0, column=5, padx=1, pady=(15, 0), sticky="n")
        gloveLImage5 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hand-back-left-outline.png")), size=(26, 26))
        gloveLImage5_label = customtkinter.CTkLabel(self.suit_frame5, image=gloveLImage5, text="")
        gloveLImage5_label.grid(row=0, column=6, padx=1, pady=(15, 0), sticky="n")
        gloveRImage5 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hand-back-right-outline.png")), size=(26, 26))
        gloveRImage5_label = customtkinter.CTkLabel(self.suit_frame5, image=gloveRImage5, text="")
        gloveRImage5_label.grid(row=0, column=7, padx=1, pady=(15, 0), sticky="n")
        
        suitImage6 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "human.png")), size=(26, 26))
        suitImage6_label = customtkinter.CTkLabel(self.suit_frame6, image=suitImage6, text="")
        suitImage6_label.grid(row=0, column=5, padx=1, pady=(15, 0), sticky="n")
        gloveLImage6 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hand-back-left-outline.png")), size=(26, 26))
        gloveLImage6_label = customtkinter.CTkLabel(self.suit_frame6, image=gloveLImage6, text="")
        gloveLImage6_label.grid(row=0, column=6, padx=1, pady=(15, 0), sticky="n")
        gloveRImage6 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hand-back-right-outline.png")), size=(26, 26))
        gloveRImage6_label = customtkinter.CTkLabel(self.suit_frame6, image=gloveRImage6, text="")
        gloveRImage6_label.grid(row=0, column=7, padx=1, pady=(15, 0), sticky="n")
        
        #buttonAttachTracker = customtkinter.CTkButton(self.suit_frame6, text="Attach Tracker", command=attachTracker)
        #buttonAttachTracker.grid(row=0, column=4, padx=(0, 0), pady=(0, 0), sticky="nsew")
        
        


if __name__ == "__main__":
    app = App()
    app.mainloop()