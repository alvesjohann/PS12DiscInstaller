import os
from urllib.request import urlretrieve

def gamesList(GAME_DIR):
    GAMES = []
    for root, dirs, files in os.walk(GAME_DIR):
        for GAME in files:
            if ".cue" in GAME:
                continue
            elif ".bin" in GAME:
                GAMES.append(GAME[:-4])
            elif ".iso" in GAME:
                GAMES.append(GAME[:-4])
    
    return GAMES

def deleteCover(GAME_ID, COVER_OUTPUT):
    COVER_TO_DELETE = f"{COVER_OUTPUT}{GAME_ID}.jpg"

    if os.path.exists(COVER_TO_DELETE):
        os.remove(COVER_TO_DELETE)
        print("Cover file deleted.")
    else:
        print("The cover does not exist.")

def excludePS1game(GAME_ID, GAME_DIR):
    BIN_TO_DELETE = f"{GAME_DIR}{GAME_ID}.bin"
    CUE_TO_DELETE = f"{GAME_DIR}{GAME_ID}.cue"

    if os.path.exists(BIN_TO_DELETE):
        os.remove(BIN_TO_DELETE)
        print(".bin file deleted.")
    else:
        print("The .bin file does not exist.")

    if os.path.exists(CUE_TO_DELETE):
        os.remove(CUE_TO_DELETE)
        print(".cue file deleted.")
    else:
        print("The .cue file does not exist.")

def excludePS2game(GAME_ID, GAME_DIR):
    GAME_TO_DELETE = f"{GAME_DIR}{GAME_ID}.iso"

    if os.path.exists(GAME_TO_DELETE):
        os.remove(GAME_TO_DELETE)
        print(".iso file deleted.")
    else:
        print("The .iso file does not exist.")