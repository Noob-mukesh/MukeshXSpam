import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import Mlk, Mlk2, Mlk3, Mlk4, Mlk5, Mlk6, Mlk7, Mlk8, Mlk9, Mlk10, ALIVE_PIC, OWNER_ID
from MukeshxSpam.plugins.help import *


MLK_IMG = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/a9a73fc9aafcf47a79412.jpg"

Mlk_Button = [
        [
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/the_support_chat")
        ],
        [
        Button.inline("• ᴄᴍᴅs •", data="help_back")
        ]
        ]
               
MlkX_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/mr_sukkun"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/the_support_chat")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/Noob-Mukesh/MukeshxSpam")
        ]
        ]
        
        
#USERS 


@Mlk.on(events.NewMessage(pattern="/start"))
@Mlk2.on(events.NewMessage(pattern="/start"))
@Mlk3.on(events.NewMessage(pattern="/start"))
@Mlk4.on(events.NewMessage(pattern="/start"))
@Mlk5.on(events.NewMessage(pattern="/start"))
@Mlk6.on(events.NewMessage(pattern="/start"))
@Mlk7.on(events.NewMessage(pattern="/start"))
@Mlk7.on(events.NewMessage(pattern="/start"))
@Mlk8.on(events.NewMessage(pattern="/start"))
@Mlk9.on(events.NewMessage(pattern="/start"))
@Mlk10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       MlkBot = await event.client.get_me()
       bot_id = MlkBot.first_name
       bot_username = MlkBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheMukesh = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**ʜɪ ᴍᴀsᴛᴇʀ, ɪᴛs ᴍᴇ {bot_id}, ʏᴏᴜʀ sᴘᴀᴍ ʙᴏᴛ!! \n\n ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ғᴏʀ ʜᴇʟᴘ**"
       usermsg = f"**ʜᴇʟʟᴏ, {firstname} ! ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ, ᴡᴇʟʟ ɪ ᴀᴍ {bot_id}, ᴀɴ ᴘᴏᴡᴇʀғᴜʟʟ sᴘᴀᴍ ʙᴏᴛ.** \n\n**ɪғ ʏᴏᴜ ᴡᴀɴᴛ ʏᴏᴜʀ ᴏᴡɴ sᴘᴀᴍ ʙᴏᴛs ʏᴏᴜ ᴄᴀɴ ᴅᴇᴘʟᴏʏ ғʀᴏᴍ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [ᴍᴜᴋᴇsʜ ʙᴏᴛ ᴢᴏɴᴇ](https://t.me/mukeshbotzone)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheMukesh,
                  MLK_IMG,
                  caption=ownermsg, 
                  buttons=Mlk_Button)
       else:
            await event.client.send_file(TheMukesh,
                  MLK_IMG,
                  caption=usermsg, 
                  buttons=MlkX_Button)
                

