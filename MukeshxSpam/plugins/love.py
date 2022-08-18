import asyncio
import random
import os
from telethon import filters, Message
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from MukeshxSpam import Mlk, Mlk2, Mlk3, Mlk4, Mlk5 , Mlk6, Mlk7, Mlk8, Mlk9, Mlk10, SUDO_USERS
from MukeshxSpam import CMD_HNDLR as hl
from telethon import utils
from resources.data import LOVESPAM

@Mlk.on_message(filters.command(lovespam))
@Mlk2.on_message(filters.command(lovespam))
@Mlk3.on_message(filters.command(lovespam))
@Mlk4.on_message(filters.command(lovespam))
@Mlk5.on_message(filters.command(lovespam))
@Mlk6.on_message(filters.command(lovespam))
@Mlk7.on_message(filters.command(lovespam))
@Mlk8.on_message(filters.command(lovespam))
@Mlk9.on_message(filters.command(lovespam))
@Mlk10.on_message(filters.command(lovespam))
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
