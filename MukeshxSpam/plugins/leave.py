import asyncio
from MukeshxSpam import Mlk, Mlk2, Mlk3, Mlk4, Mlk5, Mlk6, Mlk7, Mlk8, Mlk9, Mlk10, SUDO_USERS
from MukeshxSpam import CMD_HNDLR as hl
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon import events
import os
import random
import sys

@Mlk.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Mlk2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Mlk3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Mlk4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Mlk5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Mlk6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Mlk7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Mlk8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Mlk9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@Mlk10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def leave(e):
    if e.sender_id in SUDO_USERS:
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = rizoel[0]
            Xd = int(bc)
            text = "ʟᴇᴀᴠɪɴɢ😔...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(Xd))
                await event.edit("sᴜᴄᴄᴇsғᴜʟʟʏ ʟᴇғᴛ ✅")
            except Exception as e:
                await event.edit(str(e))
         
        else:
             bc = e.chat_id
             Xd = int(bc)
             text = "ɪ'ᴍ ʟᴇᴀᴠɪɴɢ ᴛʜɪs ɢʀᴏᴜᴘ......"
             if e.is_private:
                  dik = f"ʏᴏᴜ  ᴄᴀɴ'ᴛ  ᴅᴏ ᴛʜɪs ʜᴇʀᴇ !! \n\n {hl}leave <Channel or Chat ID> \n {hl}leave : ᴛʏᴘᴇ ɪɴ  ᴛʜᴇ ɢʀᴏᴜᴘ  ʙᴏᴛ  ᴡɪʟʟ ᴀᴜᴛᴏ  ʟᴇᴀᴠᴇ  ᴛʜᴀᴛ ɢʀᴏᴜᴘ !"
                  await e.reply(dik, parse_mode=None, link_preview=None )
             else:
                  event = await e.reply(text, parse_mode=None, link_preview=None )
                  try:
                      await event.client(LeaveChannelRequest(Xd))
                  except Exception as e:
                      await event.edit(str(e))
