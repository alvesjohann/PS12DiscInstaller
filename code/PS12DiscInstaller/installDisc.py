import os
from urllib.request import urlretrieve

def excludeChars(FILE, EXCLUDE_CHARS):
    for character in EXCLUDE_CHARS:
        FILE = FILE.replace(character, "")

    return FILE

def coverDownloader(GAME_ID, COVER_DIR, COVER_URL):
    #DOWNLOAD COVER OF THE GAME
    COVER_URL = f"{COVER_URL}{GAME_ID}.jpg"
    NEW_COVER = f"{COVER_DIR}{GAME_ID}.jpg"

    #SAVE THE COVER IN THE DUCKSTATION COVERS DIRECTORY
    urlretrieve(COVER_URL, NEW_COVER)

def PS1_makeISOfile(ISO_MAKER_PATH, DISC_VOLUME, PS1_OUTPUT, ISO_MAKER="ImgBurn.exe", CHARS_TO_EXCLUDE=["_", ".", "SYSTEM", "system"]):
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

    makeCopy = False
    for root, dirs, files in os.walk(DISC_VOLUME):
        for file in files:
            GAME_ID = excludeChars(file, CHARS_TO_EXCLUDE)

            if GAME_ID[:4] in IDs:
                makeCopy = True
                GAME_ID = f"{GAME_ID[:4]}-{GAME_ID[4:]}"
            elif GAME_ID[:3].lower() == "lsp":
                makeCopy = True
                GAME_ID = f"LSP-{GAME_ID[3:]}"
            elif GAME_ID[:2].lower() == "pl":
                makeCopy = True
                GAME_ID = f"PL-{GAME_ID[2:]}"

            if makeCopy:
                os.system("cls")
                print(f"Game found in {DISC_VOLUME} {GAME_ID}.\nThe game will be installed in {PS1_OUTPUT}.")
                
                #CREATE DISC ISO FILE
                os.chdir(ISO_MAKER_PATH)
                os.system(f"{ISO_MAKER} /MODE READ /OUTPUTMODE IMAGEFILE /SRC {DISC_VOLUME} /DEST \"{PS1_OUTPUT}{GAME_ID}.bin\" /EJECT YES /START /CLOSE /OVERWRITE")
                #makeCopy = False
                return GAME_ID
            
def PS2_makeISOfile(ISO_MAKER_PATH, DISC_VOLUME, PS2_OUTPUT, ISO_MAKER="ImgBurn.exe", CHARS_TO_EXCLUDE=["_", "."]):
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

    for root, dirs, files in os.walk(DISC_VOLUME):
        for file in files:
            GAME_ID = excludeChars(file, CHARS_TO_EXCLUDE)
            
            if GAME_ID[:4] in IDs:
                GAME_ID = F"{GAME_ID[:4]}-{GAME_ID[4:]}"
                os.system("cls")
                print(f"Game found in {DISC_VOLUME} {GAME_ID}.\nThe game will be installed in {PS2_OUTPUT}.")

                #CREATE DISC ISO FILE
                os.chdir(ISO_MAKER_PATH)
                os.system(f"{ISO_MAKER} /MODE READ /OUTPUTMODE IMAGEFILE /SRC {DISC_VOLUME} /DEST \"{PS2_OUTPUT}{GAME_ID}.iso\" /EJECT YES /START /CLOSE /OVERWRITE")
                #break
                return GAME_ID