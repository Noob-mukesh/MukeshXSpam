import os
import asyncio
import sys
import git
import heroku3
from MukeshxSpam import Mlk, Mlk2, Mlk3, Mlk4, Mlk5 , Mlk6, Mlk7, Mlk8, Mlk9, Mlk10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, mukeshversion
from MukeshxSpam import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
from MukeshxSpam import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

MLK_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/558fac9d590fa4cdd7a52.jpg"
  

mukesh = "✯ᴍᴜᴋᴇsʜ x sᴘᴀᴍ ʜᴇʀᴇ✯\n\n"
mukesh += f"═══════════════════\n"
mukesh += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"
mukesh += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
mukesh += f"• **ᴍᴜᴋᴇsʜxsᴘᴀᴍ  ᴠᴇʀsɪᴏɴ**  : `{mukeshversion}`\n"
mukesh += f"═══════════════════\n\n"   

                                  
@Mlk.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mlk2.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mlk3.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mlk4.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mlk5.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mlk6.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mlk7.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mlk8.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mlk9.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mlk10.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
     await event.client.send_file(event.chat_id,
                                  MLK_PIC,
                                  caption=mukesh,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/mukeshbotzone"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/the_support_chat")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/Noob-Mukesh/Spambotfather")
        ]
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@Mlk.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mlk2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mlk3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mlk4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mlk5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mlk6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mlk7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mlk8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mlk9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mlk10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "ᴘᴏɴɢ ʙᴀʙʏ!🏓"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀\n▒█▀▀▄ ▒█░░▒█ ░▒█░░\n▒█▄▄█ ▒█▄▄▄█ ░▒█░░\n\nϟ ᴍᴜᴋᴇsʜ X sᴘᴀᴍ ϟ︎ `{ms}` ᴍs")
        
        

@Mlk.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mlk2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mlk3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mlk4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mlk5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mlk6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mlk7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mlk8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mlk9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mlk10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "**ʀᴇsᴛᴀʀᴛɪɴɢ  ʏᴏᴜʀ ᴍᴜᴋᴇsʜ  x  sᴘᴀᴍ**.. ᴘʟᴇᴀsᴇ  ᴡᴀɪᴛ  ᴜɴᴛɪʟ  ɪᴛ  sᴛᴀʀᴛs ᴀɢᴀɪɴ"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Mlk.disconnect()
        except Exception:
            pass
        try:
            await Mlk2.disconnect()
        except Exception:
            pass
        try:
            await Mlk3.disconnect()
        except Exception:
            pass
        try:
            await Mlk4.disconnect()
        except Exception:
            pass
        try:
            await Mlk5.disconnect()
        except Exception:
            pass
        try:
            await Mlk6.disconnect()
        except Exception:
            pass
        try:
            await Mlk7.disconnect()
        except Exception:
            pass
        try:
            await Mlk8.disconnect()
        except Exception:
            pass
        try:
            await Mlk9.disconnect()
        except Exception:
            pass
        try:
            await Mlk10.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)

@Mlk.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply("Adding user as a sudo...")
        mukesh = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply to a user.")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**ᴀᴅᴅᴇᴅ  `{target}` ** ᴀs ᴀ  sᴜᴅᴏ ᴜsᴇʀ 😌👀 ʀᴇsᴛᴀʀᴛɪɴɢ.. ᴘʟᴇᴀsᴇ  ᴡᴀɪᴛ  ᴀ  ᴍɪɴᴜᴛᴇ ʙʙ..")
        heroku_var[mukesh] = newsudo   
   
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target
