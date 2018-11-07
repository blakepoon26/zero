"""Valid users for the system"""
import pandas as pd

USERS = {"KCB": "Krisna Chandra Bhargava",
         "BP": "Bin Pan",
         "ZF": "Zoey Ferguson"}

USERS = pd.DataFrame(list(USERS.items()), columns=["Initials", "Name"])
