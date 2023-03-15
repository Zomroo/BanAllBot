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
    API_ID = int(os.getenv("API_ID", "5148561602"))
    API_HASH = os.getenv("API_HASH", "b8105dc4c17419dfd4165ecf1d0bc100")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5619054777:AAF_XsEHxhJ7aXRRKowWzCR6R2u3vC1Hsi8")
    sudo = os.getenv("SUDO")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
