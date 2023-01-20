from euc_lb import *
import getpass
import os

winuser = getpass.getuser()
winpcname = os.environ["COMPUTERNAME"]


prompt = f"""{gray("╭──")} {red(f"{winuser}")} {gray("on")} {yellow(f"{winpcname}")}
{gray("╰─")} {blue("» ")}"""

logo = r"""
 _       ____
| |     |  _ \                                             
| |     | |_) |  __ _  ___   __ _  _   _  _ __  _   _  ___  
| |     |  _ <  / _` |/ __| / _` || | | || '__|| | | |/ __|
| |____ | |_) || (_| |\__ \| (_| || |_| || |   | |_| |\__ \
|______||____/  \__,_||___/ \__,_| \__,_||_|    \__,_||___/
"""

cls()
print(logo)

while True:
    cmd = input(prompt)
    args = cmd.split()

    if len(args) == 0: continue  # blank command, or space
    else:
        
        cmd = args[0]
        
        if cmd == "" or cmd.startswith(" "):
            print("instructions will go here soon™")

        elif cmd == "cls":
            cls()

        elif cmd == ("uwu"):
            uwu()
            
            
            
            
