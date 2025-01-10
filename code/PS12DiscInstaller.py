import customtkinter as ctk
import PS12DiscInstaller as PS
from PIL import Image
from urllib.request import urlretrieve
from shutil import rmtree
import os

#DESIGN DIFINITIONS
APP_ICON = "img/PS1DiscInstaller_icon.png"
APP_TITLE = "PS1-PS2 Disc Installer"
MODE = "dark"
COLOR_THEME = "dark-blue"

#BUTTONS COLORS
BT_SELECTED_COLOR = "#1f538d"
BT_UNSELECTED_COLOR = "transparent"

#CONFIGURATIONS IMPORT
CONFIG_FILE = PS.READ_CONFIG("config.cfg")

ISO_MAKER_PATH, DISC_VOLUME = PS.CONFIG_ISO(CONFIG_FILE)
PS1_OUTPUT, PS1_COVER_DIR, PS1_COVER_URL = PS.CONFIG_PS1(CONFIG_FILE)
PS2_OUTPUT, PS2_COVER_DIR, PS2_COVER_URL = PS.CONFIG_PS2(CONFIG_FILE)
BT_UP, BT_DOWN, BT_LEFT, BT_RIGHT, BT_CONFIRM, BT_CANCEL, BT_QUIT = PS.CONFIG_BUTTONS(CONFIG_FILE)

class mainWINDOW():
    def __init__(self):
        #ISO MAKER SET
        self.ISO_MAKER_PATH = ISO_MAKER_PATH
        self.DISC_VOLUME = DISC_VOLUME

        #PS1 SET
        self.PS1_OUTPUT = PS1_OUTPUT
        self.PS1_COVER_DIR = PS1_COVER_DIR
        self.PS1_COVER_URL = PS1_COVER_URL

        #PS2 SET
        self.PS2_OUTPUT = PS2_OUTPUT
        self.PS2_COVER_DIR = PS2_COVER_DIR
        self.PS2_COVER_URL = PS2_COVER_URL

        self.BT_LIST = ["BT_INSTALL_PS1_GAME", "BT_UNINSTALL_PS1_GAME", "BT_INSTALL_PS2_GAME", "BT_UNINSTALL_PS2_GAME", "BT_CLOSE_APP"]
        self.BT_SELECTED = 0

        ctk.set_appearance_mode(MODE)
        ctk.set_default_color_theme(COLOR_THEME)

        #CREATE ROOT
        self.root = ctk.CTk()

        #SET ICON
        self.root.iconbitmap(APP_ICON)
        #HIDE CURSOR
        self.root.config(cursor="none")
        #SET FULLSCREEN
        self.root.attributes("-fullscreen", "True")

        self.BT_FRAME = ctk.CTkFrame(master=self.root)
        self.BT_FRAME.grid_columnconfigure(0, weight=1)
        self.BT_FRAME.pack(pady=20, padx=20,)

        #CREATE PS1 INSTALL DISC BUTTON
        self.BT_INSTALL_PS1_GAME = ctk.CTkButton(master=self.BT_FRAME, text="Install PS1 Disc", command=self.installPS1game, fg_color=BT_SELECTED_COLOR, hover=False)
        self.BT_INSTALL_PS1_GAME.grid(row=0, column=0, pady=6, padx=6)

        #CREATE PS1 UNINSTALL DISC BUTTON
        self.BT_UNINSTALL_PS1_GAME = ctk.CTkButton(master=self.BT_FRAME, text="Uninstall PS1 Disc", command=self.uninstallPS1game, fg_color=BT_UNSELECTED_COLOR, hover=False)
        self.BT_UNINSTALL_PS1_GAME.grid(row=0, column=1, pady=6, padx=6)

        #CREATE PS2 INSTALL DISC BUTTON
        self.BT_INSTALL_PS2_GAME = ctk.CTkButton(master=self.BT_FRAME, text="Install PS2 Disc", command=self.installPS2game, fg_color=BT_UNSELECTED_COLOR, hover=False)
        self.BT_INSTALL_PS2_GAME.grid(row=1, column=0, pady=6, padx=6)

        #CREATE PS2 UNINSTALL DISC BUTTON
        self.BT_UNINSTALL_PS2_GAME = ctk.CTkButton(master=self.BT_FRAME, text="Uninstall PS2 Disc", command=self.uninstallPS2game, fg_color=BT_UNSELECTED_COLOR, hover=False)
        self.BT_UNINSTALL_PS2_GAME.grid(row=1, column=1, pady=6, padx=6)

        #CLOSE APP BUTTON
        self.BT_CLOSE_APP = ctk.CTkButton(master=self.BT_FRAME, text="Exit", command=self.closeApp, fg_color=BT_UNSELECTED_COLOR, hover=False)
        self.BT_CLOSE_APP.grid(row=2, column=0, pady=6, padx=6, columnspan=2, sticky="ew")

    def installPS1game(self):
        GAME_ID = PS.PS1_makeISOfile(self.ISO_MAKER_PATH, self.DISC_VOLUME, self.PS1_OUTPUT)
        PS.coverDownloader(GAME_ID, self.PS1_COVER_DIR, self.PS1_COVER_URL)

    def uninstallPS1game(self):
        self.PS1Window()

    def installPS2game(self):
        GAME_ID = PS.PS2_makeISOfile(self.ISO_MAKER_PATH, self.DISC_VOLUME, self.PS2_OUTPUT)
        PS.coverDownloader(GAME_ID, self.PS2_COVER_DIR, self.PS2_COVER_URL)

    def uninstallPS2game(self):
        self.PS2Window()

    def closeApp(self):
        self.root.destroy()

    def updateSelectedButton(self, NUMBER_TO_SUM):
        #SET THE NEW INDEX OF SELECTED BUTTON   
        self.BT_SELECTED += NUMBER_TO_SUM

        if self.BT_SELECTED < 0:
            self.BT_SELECTED = 0
        elif self.BT_SELECTED >= len(self.BT_LIST):
            self.BT_SELECTED = len(self.BT_LIST) - 1

        #SET ALL BUTTONS TO UNSELECTED COLOR
        for BUTTON in self.BT_LIST:
            if BUTTON == "BT_INSTALL_PS1_GAME":
                self.BT_INSTALL_PS1_GAME.configure(fg_color=BT_UNSELECTED_COLOR)
            elif BUTTON == "BT_UNINSTALL_PS1_GAME":
                self.BT_UNINSTALL_PS1_GAME.configure(fg_color=BT_UNSELECTED_COLOR)
            elif BUTTON == "BT_INSTALL_PS2_GAME":
                self.BT_INSTALL_PS2_GAME.configure(fg_color=BT_UNSELECTED_COLOR)
            elif BUTTON == "BT_UNINSTALL_PS2_GAME":
                self.BT_UNINSTALL_PS2_GAME.configure(fg_color=BT_UNSELECTED_COLOR)
            elif BUTTON == "BT_CLOSE_APP":
                self.BT_CLOSE_APP.configure(fg_color=BT_UNSELECTED_COLOR)
        
        #SET ONLY THE SELECTED BUTTON WITH SELECTED COLOR
        for BT_INDEX, BUTTON in enumerate(self.BT_LIST):
            if BT_INDEX == self.BT_SELECTED:
                if BUTTON == "BT_INSTALL_PS1_GAME":
                    self.BT_INSTALL_PS1_GAME.configure(fg_color=BT_SELECTED_COLOR)
                    break
                elif BUTTON == "BT_UNINSTALL_PS1_GAME":
                    self.BT_UNINSTALL_PS1_GAME.configure(fg_color=BT_SELECTED_COLOR)
                    break
                elif BUTTON == "BT_INSTALL_PS2_GAME":
                    self.BT_INSTALL_PS2_GAME.configure(fg_color=BT_SELECTED_COLOR)
                    break
                elif BUTTON == "BT_UNINSTALL_PS2_GAME":
                    self.BT_UNINSTALL_PS2_GAME.configure(fg_color=BT_SELECTED_COLOR)
                    break
                elif BUTTON == "BT_CLOSE_APP":
                    self.BT_CLOSE_APP.configure(fg_color=BT_SELECTED_COLOR)
                    break
    
    def runSelectedButton(self):
        #RUN THE METHOD OF THE SELECTED BUTTON
        for BT_INDEX, BUTTON in enumerate(self.BT_LIST):
            if BT_INDEX == self.BT_SELECTED:
                if BUTTON == "BT_INSTALL_PS1_GAME":
                    self.installPS1game()
                    break
                elif BUTTON == "BT_UNINSTALL_PS1_GAME":
                    self.uninstallPS1game()
                    break
                elif BUTTON == "BT_INSTALL_PS2_GAME":
                    self.installPS2game()
                    break
                elif BUTTON == "BT_UNINSTALL_PS2_GAME":
                    self.uninstallPS2game()
                    break
                elif BUTTON == "BT_CLOSE_APP":
                    self.closeApp()
                    break

    def PS1Window(self):
        #CREATE WINDOW
        GAMES_WINDOW = ctk.CTkToplevel()
        #SET FULLSCREEN
        GAMES_WINDOW.attributes("-fullscreen", "True")
        #HIDE CURSOR
        GAMES_WINDOW.config(cursor="none")
        #FOCUS WINDOW
        GAMES_WINDOW.grab_set()
        GAMES_WINDOW.focus()

        #EVENTS
        def upEvent(event):
            #SET THE NEW INDEX OF SELECTED BUTTON  
            PREVIOUS_BUTON = self.BT_SELECTED
            self.BT_SELECTED -= NUMBER_OF_COLUMNS

            if self.BT_SELECTED < 0:
                self.BT_SELECTED = 0
            elif self.BT_SELECTED >= len(GAME_LIST):
                self.BT_SELECTED = len(GAME_LIST) - 1

            #SET PREVIOUS BUTTON TO UNSELECTED COLOR
            BT_GAME_LIST[PREVIOUS_BUTON].configure(fg_color=BT_UNSELECTED_COLOR)
            
            #SET ONLY THE SELECTED BUTTON WITH SELECTED COLOR
            BT_GAME_LIST[self.BT_SELECTED].configure(fg_color=BT_SELECTED_COLOR)

        def downEvent(event):
            #SET THE NEW INDEX OF SELECTED BUTTON  
            PREVIOUS_BUTON = self.BT_SELECTED
            self.BT_SELECTED += NUMBER_OF_COLUMNS

            if self.BT_SELECTED < 0:
                self.BT_SELECTED = 0
            elif self.BT_SELECTED >= len(GAME_LIST):
                self.BT_SELECTED = len(GAME_LIST) - 1

            #SET PREVIOUS BUTTON TO UNSELECTED COLOR
            BT_GAME_LIST[PREVIOUS_BUTON].configure(fg_color=BT_UNSELECTED_COLOR)
            
            #SET ONLY THE SELECTED BUTTON WITH SELECTED COLOR
            BT_GAME_LIST[self.BT_SELECTED].configure(fg_color=BT_SELECTED_COLOR)

        def leftEvent(event):
            #SET THE NEW INDEX OF SELECTED BUTTON  
            PREVIOUS_BUTON = self.BT_SELECTED
            self.BT_SELECTED -= 1

            if self.BT_SELECTED < 0:
                self.BT_SELECTED = 0
            elif self.BT_SELECTED >= len(GAME_LIST):
                self.BT_SELECTED = len(GAME_LIST) - 1

            #SET PREVIOUS BUTTON TO UNSELECTED COLOR
            BT_GAME_LIST[PREVIOUS_BUTON].configure(fg_color=BT_UNSELECTED_COLOR)
            
            #SET ONLY THE SELECTED BUTTON WITH SELECTED COLOR
            BT_GAME_LIST[self.BT_SELECTED].configure(fg_color=BT_SELECTED_COLOR)

        def rightEvent(event):
            #SET THE NEW INDEX OF SELECTED BUTTON  
            PREVIOUS_BUTON = self.BT_SELECTED
            self.BT_SELECTED += 1

            if self.BT_SELECTED < 0:
                self.BT_SELECTED = 0
            elif self.BT_SELECTED >= len(GAME_LIST):
                self.BT_SELECTED = len(GAME_LIST) - 1

            #SET PREVIOUS BUTTON TO UNSELECTED COLOR
            BT_GAME_LIST[PREVIOUS_BUTON].configure(fg_color=BT_UNSELECTED_COLOR)
            
            #SET ONLY THE SELECTED BUTTON WITH SELECTED COLOR
            BT_GAME_LIST[self.BT_SELECTED].configure(fg_color=BT_SELECTED_COLOR)

        def confirmEvent(event):
            if len(GAME_LIST) > 0:
                PS.deleteCover(GAME_LIST[self.BT_SELECTED], PS1_COVER_DIR)
                PS.excludePS1game(GAME_LIST[self.BT_SELECTED], PS1_OUTPUT)
                self.BT_SELECTED = 1
                GAMES_WINDOW.destroy()
                self.PS1Window()

        def cancelEvent(event):
            self.BT_SELECTED = 1
            GAMES_WINDOW.destroy()

        def quitEvent(event):
            self.BT_SELECTED = 1
            GAMES_WINDOW.destroy()

        #SET BIDINGS
        GAMES_WINDOW.bind(BT_UP, upEvent)
        GAMES_WINDOW.bind(BT_DOWN, downEvent)
        GAMES_WINDOW.bind(BT_LEFT, leftEvent)
        GAMES_WINDOW.bind(BT_RIGHT, rightEvent)
        GAMES_WINDOW.bind(BT_CONFIRM, confirmEvent)
        GAMES_WINDOW.bind(BT_CANCEL, cancelEvent)
        GAMES_WINDOW.bind(BT_QUIT, quitEvent)

        MAX_WIDTH = GAMES_WINDOW.winfo_screenwidth()
        MAX_HEIGHT = GAMES_WINDOW.winfo_screenheight()
        PAD_X = 6
        PAD_Y = 6
        COVER_WIDTH = 150
        COVER_HEIGHT = COVER_WIDTH

        IDs = ["SLPS",
            "SLPM",
            "SLES",
            "SLUS",
            "LSP",
            "SCUS",
            "SCES",
            "SIPS",
            "SCPS",
            "SLED",
            "PAPX",
            "PTPX",
            "PCPX",
            "PEPX",
            "PUPX",
            "SCED",
            "PL",
            "PBPX",
            "CPCS",
            "SCEs",
            "SCPM",
            "SCAJ",
            "ESPM",
            "SCZS",
            "PCPD",
            "SLKA",
            "PSRM",
            "HPS"]

        GAME_LIST = PS.gamesList(PS1_OUTPUT)
        BT_GAME_LIST = []


        NUMBER_OF_COLUMNS = int(MAX_WIDTH / (COVER_WIDTH + PAD_X))
        NUMBER_OF_ROWS = int(round(len(GAME_LIST) / NUMBER_OF_COLUMNS, 0))
        LENGHT_FIRST_ROW = NUMBER_OF_COLUMNS if len(GAME_LIST) > NUMBER_OF_COLUMNS else len(GAME_LIST)
        OFFSET_WIDTH = int((MAX_WIDTH - LENGHT_FIRST_ROW*(COVER_WIDTH+PAD_X))/2)
        OFFSET_HEIGHT = int((MAX_HEIGHT - NUMBER_OF_ROWS*(COVER_HEIGHT+PAD_Y))/2 - ((COVER_HEIGHT/2) if NUMBER_OF_ROWS < 1 else 0))

        for column in range(NUMBER_OF_COLUMNS):
            GAMES_WINDOW.grid_columnconfigure(column, weight=0)

        for row in range(NUMBER_OF_ROWS):
            GAMES_WINDOW.grid_rowconfigure(row, weight=0)

        if len(GAME_LIST) > 0:
            for index, item in enumerate(GAME_LIST):
                BT_ROW = int(index / NUMBER_OF_COLUMNS)
                BT_COLUMN = int(round(index % NUMBER_OF_COLUMNS,0))

                BT_COVER = None

                GAME_ID = item[:10]
                GAME_TITLE = None

                if GAME_ID[:4] in IDs:
                    urlretrieve(f'{PS1_COVER_URL}{GAME_ID}.jpg',f"temp/{GAME_ID}.jpg")
                    DOWNLOADED_COVER = f"temp/{GAME_ID}.jpg"
                    BT_COVER = ctk.CTkImage(light_image=Image.open(DOWNLOADED_COVER), size=(COVER_WIDTH-PAD_X, COVER_HEIGHT-PAD_Y))
                else:
                    GAME_TITLE = ""
                    for INDEX, CHAR in enumerate(item):
                        if INDEX % 15 == 0:
                            GAME_TITLE = f"{GAME_TITLE}\n"

                        GAME_TITLE += CHAR

                BT_GAME_LIST.append(ctk.CTkButton(GAMES_WINDOW, text=GAME_TITLE, width=COVER_WIDTH, height=COVER_HEIGHT, image=BT_COVER, border_spacing=0, corner_radius=0, fg_color=BT_UNSELECTED_COLOR))
                BT_GAME_LIST[index].place(x=OFFSET_WIDTH+(BT_COLUMN)*(COVER_WIDTH+PAD_X)+PAD_X, y=OFFSET_HEIGHT+(BT_ROW)*(COVER_HEIGHT+PAD_Y)+PAD_Y)

            BT_GAME_LIST[0].configure(fg_color=BT_SELECTED_COLOR)

        else:
            BT_GAME_LIST.append(ctk.CTkButton(GAMES_WINDOW, text="0 games installed.", width=COVER_WIDTH, height=COVER_HEIGHT, border_spacing=0, corner_radius=0, fg_color=BT_SELECTED_COLOR))
            BT_GAME_LIST[0].place(x=(MAX_WIDTH-COVER_WIDTH-PAD_X)/2, y=(MAX_HEIGHT-COVER_HEIGHT-PAD_Y)/2)

        self.BT_SELECTED = 0

        GAMES_WINDOW.mainloop()

        rmtree("temp")
        os.mkdir("temp")

    def PS2Window(self):
        #CREATE WINDOW
        GAMES_WINDOW = ctk.CTkToplevel()
        #SET FULLSCREEN
        GAMES_WINDOW.attributes("-fullscreen", "True")
        #HIDE CURSOR
        GAMES_WINDOW.config(cursor="none")
        #FOCUS WINDOW
        GAMES_WINDOW.grab_set()
        GAMES_WINDOW.focus()

        #EVENTS
        def upEvent(event):
            #SET THE NEW INDEX OF SELECTED BUTTON  
            PREVIOUS_BUTON = self.BT_SELECTED
            self.BT_SELECTED -= NUMBER_OF_COLUMNS

            if self.BT_SELECTED < 0:
                self.BT_SELECTED = 0
            elif self.BT_SELECTED >= len(GAME_LIST):
                self.BT_SELECTED = len(GAME_LIST) - 1

            #SET PREVIOUS BUTTON TO UNSELECTED COLOR
            BT_GAME_LIST[PREVIOUS_BUTON].configure(fg_color=BT_UNSELECTED_COLOR)
            
            #SET ONLY THE SELECTED BUTTON WITH SELECTED COLOR
            BT_GAME_LIST[self.BT_SELECTED].configure(fg_color=BT_SELECTED_COLOR)

        def downEvent(event):
            #SET THE NEW INDEX OF SELECTED BUTTON  
            PREVIOUS_BUTON = self.BT_SELECTED
            self.BT_SELECTED += NUMBER_OF_COLUMNS

            if self.BT_SELECTED < 0:
                self.BT_SELECTED = 0
            elif self.BT_SELECTED >= len(GAME_LIST):
                self.BT_SELECTED = len(GAME_LIST) - 1

            #SET PREVIOUS BUTTON TO UNSELECTED COLOR
            BT_GAME_LIST[PREVIOUS_BUTON].configure(fg_color=BT_UNSELECTED_COLOR)
            
            #SET ONLY THE SELECTED BUTTON WITH SELECTED COLOR
            BT_GAME_LIST[self.BT_SELECTED].configure(fg_color=BT_SELECTED_COLOR)

        def leftEvent(event):
            #SET THE NEW INDEX OF SELECTED BUTTON  
            PREVIOUS_BUTON = self.BT_SELECTED
            self.BT_SELECTED -= 1

            if self.BT_SELECTED < 0:
                self.BT_SELECTED = 0
            elif self.BT_SELECTED >= len(GAME_LIST):
                self.BT_SELECTED = len(GAME_LIST) - 1

            #SET PREVIOUS BUTTON TO UNSELECTED COLOR
            BT_GAME_LIST[PREVIOUS_BUTON].configure(fg_color=BT_UNSELECTED_COLOR)
            
            #SET ONLY THE SELECTED BUTTON WITH SELECTED COLOR
            BT_GAME_LIST[self.BT_SELECTED].configure(fg_color=BT_SELECTED_COLOR)

        def rightEvent(event):
            #SET THE NEW INDEX OF SELECTED BUTTON  
            PREVIOUS_BUTON = self.BT_SELECTED
            self.BT_SELECTED += 1

            if self.BT_SELECTED < 0:
                self.BT_SELECTED = 0
            elif self.BT_SELECTED >= len(GAME_LIST):
                self.BT_SELECTED = len(GAME_LIST) - 1

            #SET PREVIOUS BUTTON TO UNSELECTED COLOR
            BT_GAME_LIST[PREVIOUS_BUTON].configure(fg_color=BT_UNSELECTED_COLOR)
            
            #SET ONLY THE SELECTED BUTTON WITH SELECTED COLOR
            BT_GAME_LIST[self.BT_SELECTED].configure(fg_color=BT_SELECTED_COLOR)

        def confirmEvent(event):
            if len(GAME_LIST) > 0:
                PS.deleteCover(GAME_LIST[self.BT_SELECTED], PS2_COVER_DIR)
                PS.excludePS2game(GAME_LIST[self.BT_SELECTED], PS2_OUTPUT)
                self.BT_SELECTED = 3
                GAMES_WINDOW.destroy()
                self.PS2Window()

        def cancelEvent(event):
            self.BT_SELECTED = 3
            GAMES_WINDOW.destroy()

        def quitEvent(event):
            self.BT_SELECTED = 3
            GAMES_WINDOW.destroy()

        #SET BIDINGS
        GAMES_WINDOW.bind(BT_UP, upEvent)
        GAMES_WINDOW.bind(BT_DOWN, downEvent)
        GAMES_WINDOW.bind(BT_LEFT, leftEvent)
        GAMES_WINDOW.bind(BT_RIGHT, rightEvent)
        GAMES_WINDOW.bind(BT_CONFIRM, confirmEvent)
        GAMES_WINDOW.bind(BT_CANCEL, cancelEvent)
        GAMES_WINDOW.bind(BT_QUIT, quitEvent)

        MAX_WIDTH = GAMES_WINDOW.winfo_screenwidth()
        MAX_HEIGHT = GAMES_WINDOW.winfo_screenheight()
        PAD_X = 6
        PAD_Y = 6
        COVER_WIDTH = 150
        COVER_HEIGHT = int(COVER_WIDTH * 1.5)

        IDs = ["ALCH",
                "CPCS",
                "GUST",
                "PAPX",
                "PBGP",
                "PBPX",
                "PCPX",
                "PDPX",
                "PKP2",
                "SCAJ",
                "SCCS",
                "SCED",
                "SCES",
                "SCKA",
                "SCPM",
                "SCPN",
                "SCPS",
                "SCUS",
                "SLAJ",
                "SLED",
                "SLES",
                "SLKA",
                "SLPM",
                "SLPS",
                "SLUS",
                "TCES",
                "TCPS",
                "TLES",
                "VW067"]

        GAME_LIST = PS.gamesList(PS2_OUTPUT)
        BT_GAME_LIST = []


        NUMBER_OF_COLUMNS = int(MAX_WIDTH / (COVER_WIDTH + PAD_X))
        NUMBER_OF_ROWS = int(round(len(GAME_LIST) / NUMBER_OF_COLUMNS, 0))
        LENGHT_FIRST_ROW = NUMBER_OF_COLUMNS if len(GAME_LIST) > NUMBER_OF_COLUMNS else len(GAME_LIST)
        OFFSET_WIDTH = int((MAX_WIDTH - LENGHT_FIRST_ROW*(COVER_WIDTH+PAD_X))/2)
        OFFSET_HEIGHT = int((MAX_HEIGHT - NUMBER_OF_ROWS*(COVER_HEIGHT+PAD_Y))/2 - ((COVER_HEIGHT/2) if NUMBER_OF_ROWS < 1 else 0))

        for column in range(NUMBER_OF_COLUMNS):
            GAMES_WINDOW.grid_columnconfigure(column, weight=0)

        for row in range(NUMBER_OF_ROWS):
            GAMES_WINDOW.grid_rowconfigure(row, weight=0)

        if len(GAME_LIST) > 0:
            for index, item in enumerate(GAME_LIST):
                BT_ROW = int(index / NUMBER_OF_COLUMNS)
                BT_COLUMN = int(round(index % NUMBER_OF_COLUMNS,0))

                BT_COVER = None

                GAME_ID = item[:10]
                GAME_TITLE = None

                if GAME_ID[:4] in IDs:
                    urlretrieve(f'{PS2_COVER_URL}{GAME_ID}.jpg',f"temp/{GAME_ID}.jpg")
                    DOWNLOADED_COVER = f"temp/{GAME_ID}.jpg"
                    BT_COVER = ctk.CTkImage(light_image=Image.open(DOWNLOADED_COVER), size=(COVER_WIDTH-PAD_X, COVER_HEIGHT-PAD_Y))
                else:
                    GAME_TITLE = ""
                    for INDEX, CHAR in enumerate(item):
                        if INDEX % 15 == 0:
                            GAME_TITLE = f"{GAME_TITLE}\n"

                        GAME_TITLE += CHAR

                BT_GAME_LIST.append(ctk.CTkButton(GAMES_WINDOW, text=GAME_TITLE, width=COVER_WIDTH, height=COVER_HEIGHT, image=BT_COVER, border_spacing=0, corner_radius=0, fg_color=BT_UNSELECTED_COLOR))
                BT_GAME_LIST[index].place(x=OFFSET_WIDTH+(BT_COLUMN)*(COVER_WIDTH+PAD_X)+PAD_X, y=OFFSET_HEIGHT+(BT_ROW)*(COVER_HEIGHT+PAD_Y)+PAD_Y)

            BT_GAME_LIST[0].configure(fg_color=BT_SELECTED_COLOR)

        else:
            BT_GAME_LIST.append(ctk.CTkButton(GAMES_WINDOW, text="0 games installed.", width=COVER_WIDTH, height=COVER_HEIGHT, border_spacing=0, corner_radius=0, fg_color=BT_SELECTED_COLOR))
            BT_GAME_LIST[0].place(x=(MAX_WIDTH-COVER_WIDTH-PAD_X)/2, y=(MAX_HEIGHT-COVER_HEIGHT-PAD_Y)/2)

        self.BT_SELECTED = 0

        GAMES_WINDOW.mainloop()

        rmtree("temp")
        os.mkdir("temp")

#EVENTS
def upEvent(event):
    app.updateSelectedButton(-2)

def downEvent(event):
    app.updateSelectedButton(2)

def leftEvent(event):
    app.updateSelectedButton(-1)

def rightEvent(event):
    app.updateSelectedButton(1)

def confirmEvent(event):
    app.runSelectedButton()

def cancelEvent(event):
    pass

def quitEvent(event):
    app.closeApp()

app = mainWINDOW()

#SET BIDINGS
app.root.bind(BT_UP, upEvent)
app.root.bind(BT_DOWN, downEvent)
app.root.bind(BT_LEFT, leftEvent)
app.root.bind(BT_RIGHT, rightEvent)
app.root.bind(BT_CONFIRM, confirmEvent)
app.root.bind(BT_CANCEL, cancelEvent)
app.root.bind(BT_QUIT, quitEvent)

app.root.mainloop()