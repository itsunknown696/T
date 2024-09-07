import logging   #Bot Created by @SudoR2spr
from logging.handlers import RotatingFileHandler   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
logging.basicConfig(   #Bot Created by @SudoR2spr
    level=logging.ERROR,   #Bot Created by @SudoR2spr
    format=   #Bot Created by @SudoR2spr
    "%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",   #Bot Created by @SudoR2spr
    datefmt="%d-%b-%y %H:%M:%S",   #Bot Created by @SudoR2spr
    handlers=[   #Bot Created by @SudoR2spr
        RotatingFileHandler("Assist.txt", maxBytes=50000000, backupCount=10),   #Bot Created by @SudoR2spr
        logging.StreamHandler(),   #Bot Created by @SudoR2spr
    ],   #Bot Created by @SudoR2spr
)   #Bot Created by @SudoR2spr
logging.getLogger("pyrogram").setLevel(logging.WARNING)   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
logging = logging.getLogger()   #Bot Created by @SudoR2spr
   #Bot Created by @SudoR2spr
