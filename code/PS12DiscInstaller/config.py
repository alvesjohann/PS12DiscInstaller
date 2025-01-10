def READ_CONFIG(CFG_FILE):
    with open(CFG_FILE) as FILE:
        CONFIG_FILE = FILE.readlines()

    for INDEX, CONFIG in enumerate(CONFIG_FILE):
        if "\n" == CONFIG[-1:]:
            CONFIG_FILE[INDEX] = CONFIG[:-1]

    return CONFIG_FILE

def CONFIG_ISO(CONFIG_FILE):
    for CONFIG in CONFIG_FILE:
        CONFIG = CONFIG.replace(" = ","=").split("=")

        #COMMENTARIES
        if CONFIG[0][:1] == "#":
            continue
        
        #ISO MAKER CONFIGS
        elif "ISO_MAKER_PATH" in CONFIG:
            ISO_MAKER_PATH = CONFIG[1]
        elif "DISC_VOLUME" in CONFIG:
            DISC_VOLUME = CONFIG[1]

    return ISO_MAKER_PATH, DISC_VOLUME

def CONFIG_PS1(CONFIG_FILE):
    for CONFIG in CONFIG_FILE:
        CONFIG = CONFIG.replace(" = ","=").split("=")

        #COMMENTARIES
        if CONFIG[0][:1] == "#":
            continue

        #PS1 CONFIGS
        elif "PS1_OUTPUT" in CONFIG:
            PS1_OUTPUT = CONFIG[1]
        elif "PS1_COVER_DIR" in CONFIG:
            PS1_COVER_DIR = CONFIG[1]
        elif "PS1_COVER_URL" in CONFIG:
            PS1_COVER_URL = CONFIG[1]

    return PS1_OUTPUT, PS1_COVER_DIR, PS1_COVER_URL

def CONFIG_PS2(CONFIG_FILE):
    for CONFIG in CONFIG_FILE:
        CONFIG = CONFIG.replace(" = ","=").split("=")

        #COMMENTARIES
        if CONFIG[0][:1] == "#":
            continue

        #PS2 CONFIGS
        elif "PS2_OUTPUT" in CONFIG:
            PS2_OUTPUT = CONFIG[1]
        elif "PS2_COVER_DIR" in CONFIG:
            PS2_COVER_DIR = CONFIG[1]
        elif "PS2_COVER_URL" in CONFIG:
            PS2_COVER_URL = CONFIG[1]

    return PS2_OUTPUT, PS2_COVER_DIR, PS2_COVER_URL

def CONFIG_BUTTONS(CONFIG_FILE):
    for CONFIG in CONFIG_FILE:
        CONFIG = CONFIG.replace(" = ","=").split("=")

        #COMMENTARIES
        if CONFIG[0][:1] == "#":
            continue

        #BUTTONS CONFIG
        elif "BT_UP" in CONFIG:
            BT_UP = f"<{CONFIG[1]}>"
        elif "BT_DOWN" in CONFIG:
            BT_DOWN = f"<{CONFIG[1]}>"
        elif "BT_LEFT" in CONFIG:
            BT_LEFT = f"<{CONFIG[1]}>"
        elif "BT_RIGHT" in CONFIG:
            BT_RIGHT = f"<{CONFIG[1]}>"
        elif "BT_CONFIRM" in CONFIG:
            BT_CONFIRM = f"<{CONFIG[1]}>"
        elif "BT_CANCEL" in CONFIG:
            BT_CANCEL = f"<{CONFIG[1]}>"
        elif "BT_QUIT" in CONFIG:
            BT_QUIT = f"<{CONFIG[1]}>"

    return BT_UP, BT_DOWN, BT_LEFT, BT_RIGHT, BT_CONFIRM, BT_CANCEL, BT_QUIT