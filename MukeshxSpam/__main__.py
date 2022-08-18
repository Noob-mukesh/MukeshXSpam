#MukeshxSpam By @itz_mst_boi

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from MukeshxSpam.utils import load_plugins
import logging
from telethon import events
from . import Mlk, Mlk2, Mlk3, Mlk4, Mlk5, Mlk6, Mlk7, Mlk8, Mlk9, Mlk10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "MukeshxSpam/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Mukesh Bot Spam Successfully deployed -!")
print("Enjoy! Do visit @mr_sukkun")

if __name__ == "__main__":
    Mlk.run_until_disconnected()
    
if __name__ == "__main__":
    Mlk2.run_until_disconnected()

if __name__ == "__main__":
    Mlk3.run_until_disconnected()
    
if __name__ == "__main__":
    Mlk4.run_until_disconnected()

if __name__ == "__main__":
    Mlk5.run_until_disconnected()
    
if __name__ == "__main__":
    Mlk6.run_until_disconnected()
    
if __name__ == "__main__":
    Mlk7.run_until_disconnected()

if __name__ == "__main__":
    Mlk8.run_until_disconnected()
    
if __name__ == "__main__":
    Mlk9.run_until_disconnected()

if __name__ == "__main__":
    Mlk10.run_until_disconnected()    
