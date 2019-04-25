import os
from time import sleep
import random

import os
from time import sleep
import platform
import sys


logo = ("""

           /$$
          |__/
  /$$$$$$  /$$  /$$$$$$  /$$   /$$ /$$   /$$
 /$$__  $$| $$ /$$__  $$|  $$ /$$/| $$  | $$
| $$  \ $$| $$| $$  \ $$ \  $$$$/ | $$  | $$
| $$  | $$| $$| $$  | $$  >$$  $$ | $$  | $$
| $$$$$$$/| $$|  $$$$$$/ /$$/\  $$|  $$$$$$$
| $$____/ |__/ \______/ |__/  \__/ \____  $$
| $$                               /$$  | $$
| $$                              |  $$$$$$/
|__/                               \______/
--------------------------------------------
""")

logo2 = ("""

           /$$
          |__/
  /$$$$$$  /$$  /$$$$$$  /$$   /$$ /$$   /$$
 /$$__  $$| $$ /$$__  $$|  $$ /$$/| $$  | $$
| $$  \ $$| $$| $$  \ $$ \  $$$$/ | $$  | $$
| $$  | $$| $$| $$  | $$  >$$  $$ | $$  | $$
| $$$$$$$/| $$|  $$$$$$/ /$$/\  $$|  $$$$$$$
| $$____/ |__/ \______/ |__/  \__/ \____  $$
| $$                               /$$  | $$
| $$                              |  $$$$$$/
|__/                               \______/
--------------------------------------------
""")


if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, Run 'sudo !!' and run the script.\nExiting.")
os.system("clear")


ans=True
while ans:
    print()
    print(logo)
    print ("""
    1.Start Proxy server
    2.Go back
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
      os.system("python3 assets/packages/proxy.py")
      print(logo2)
    if ans=="2":
      os.system("clear")
      sys.exit()
    elif ans !="":
      print("\n Not Valid Choice Try again")
      sleep(2)
      os.system("clear")
      print(logo2)
