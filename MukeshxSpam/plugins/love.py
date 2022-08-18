import asyncio
import random
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from MukeshxSpam import Mlk, Mlk2, Mlk3, Mlk4, Mlk5 , Mlk6, Mlk7, Mlk8, Mlk9, Mlk10, SUDO_USERS
from MukeshxSpam import CMD_HNDLR as hl
from telethon import utils
from resources.data import LOVESPAM

@Mlk.on(events.NewMessage(incoming=True, pattern=r"\%lovespam(?: |$)(.*)"%hl))
@Mlk2.on(events.NewMessage(incoming=True, pattern=r"\%lovespam(?: |$)(.*)"%hl))
@Mlk3.on(events.NewMessage(incoming=True, pattern=r"\%lovespam(?: |$)(.*)"%hl))
@Mlk4.on(events.NewMessage(incoming=True, pattern=r"\%lovespam(?: |$)(.*)"%hl))
@Mlk5.on(events.NewMessage(incoming=True, pattern=r"\%lovespam(?: |$)(.*)"%hl))
@Mlk6.on(events.NewMessage(incoming=True, pattern=r"\%lovespam(?: |$)(.*)"%hl))
@Mlk7.on(events.NewMessage(incoming=True, pattern=r"\%lovespam(?: |$)(.*)"%hl))
@Mlk8.on(events.NewMessage(incoming=True, pattern=r"\%lovespam(?: |$)(.*)"%hl))
@Mlk9.on(events.NewMessage(incoming=True, pattern=r"\%lovespam(?: |$)(.*)"%hl))
@Mlk10.on(events.NewMessage(incoming=True, pattern=r"\%lovespam(?: |$)(.*)"%hl))
async def lovespam(e):
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(rizoel) == 1:
            counter = int(rizoel[0])
            if int(e.chat_id) in GROUP:
                text = f"Sorry !! I can't spam here"
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                 love = random.choice(LOVESPAM)
                 for _ in range(counter):
                     async with e.client.action(e.chat_id, "document"):
                         smex = await e.client.send_file(e.chat_id, lovex) 
                     await asyncio.sleep(0.4)
        else:
            usage = f"**MODULE NAME : LOVE SPAM** \n\n command: `{hl}lovespam <count>`"
            await e.reply(usage, parse_mode=None, link_preview=None )
