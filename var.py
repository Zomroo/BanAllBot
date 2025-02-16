import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "16844842"))
    API_HASH = os.getenv("API_HASH", "f6b0ceec5535804be7a56ac71d08a5d4")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5619054777:AAF_XsEHxhJ7aXRRKowWzCR6R2u3vC1Hsi8")
    sudo = os.getenv("SUDO")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
