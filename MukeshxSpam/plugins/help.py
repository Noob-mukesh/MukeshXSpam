from MukeshxSpam import Mlk, Mlk2, Mlk3, Mlk4, Mlk5, Mlk6, Mlk7, Mlk8, Mlk9, Mlk10, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from MukeshxSpam import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/a9a73fc9aafcf47a79412.jpg"

Mlk_Help = "__ᴄʟɪᴄᴋ  ᴏɴ  ʙᴇʟᴏᴡ  ʙᴜᴛᴛᴏɴs  ғᴏʀ ʜᴇʟᴘ__"


@Mlk.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mlk2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mlk3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mlk4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mlk5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mlk6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mlk7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mlk8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mlk9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mlk10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Mlk_Help,
                                  buttons=[
           [
            Button.inline("• sᴘᴀᴍ •", data="spam"),
            Button.inline("• ʀᴀɪᴅ •", data="raid"),
           ],
           [
            Button.inline("• ᴇxᴛʀᴀ •", data="extra"),
            Button.inline("ʟᴏᴠᴇ", data="love"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/mukeshbotzone")
           ],
           ],
           )              

  
  
extra_msg = f"""
**ʜᴇʟᴘ  ᴇxᴛʀᴀ  ᴄᴍᴅs**

**Userbot**: ᴜsᴇʀʙᴏᴛ ᴄᴍᴅs
command:
i) {hl}ping 
ii) {hl}alive
iii) {hl}restart
iv) {hl}addsudo <reply to user> : ᴏᴡɴᴇʀ ᴄᴍᴅ

**Echo**: ᴛᴏ  ᴀᴄᴛɪᴠᴇ  ᴇᴄʜᴏ  ᴏɴ ᴀɴʏ ᴜsᴇʀ
command:
i) {hl}addecho <reply to user>
ii) {hl}rmecho <reply to user>

**Leave**: ᴛᴏ ʟᴇᴀᴠᴇ  ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ
command:
i) {hl}leave <group/chat id>
ii) {hl}leave : ᴛʏᴘᴇ ɪɴ ᴛʜᴇ  ɢʀᴏᴜᴘ ʙᴏᴛ ᴡɪʟʟ  ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ

**Packspam**: sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ  sᴘᴀᴍ
i) {hl}packspam (replying to any sticker)

**© @itz_mst_boi**
"""
love_msg = f"""
**ʟᴏᴠᴇ ʀᴀɪᴅ ᴄᴍᴅs **
**ʟᴏᴠᴇʀᴀɪᴅ:** ʟᴏᴠᴇᴇᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴsɪᴠɪᴅᴜᴀʟ ғᴏᴇ ᴀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ.
command:
i) {h1}loveraid <Count> username
"""

                 
raid_msg = f"""
**ʜᴇʟᴘ ʀᴀɪᴅ ᴄᴍᴅs **


**raid:** Activates raid on any individual user for given range.
command:
i) {hl}raid <count> <username
ii) {hl}raid <count> <reply to user>

**Delayraid**: ᴀᴄᴛɪᴠᴀᴛᴇs ʀᴀɪᴅ  ᴏɴ  ᴀɴʏ  ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsᴇʀ  ғᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ.
Command:
i) {hl}delayraid <delay> <count> <Username of User>
ii) {hl}delayraid <delay> <count> <reply to a User>

**replyraid:** ᴀᴄᴛɪᴠᴀᴛᴇs ʀᴇᴘʟʏ  ʀᴀɪᴅ  ᴏɴ  ᴛʜᴇ  ᴜsᴇʀ!!
command:
i) {hl}replyraid <replying to user>
ii) {hl}dreplyraid <username>

**dreplyraid:** ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇs ʀᴇᴘʟʏ  ʀᴀɪᴅ ᴏɴ  ᴛʜᴇ ᴜsᴇʀ!!
command:
i) {hl}dreplyraid <replying to user>
ii) {hl}dreplyraid <username>


**© @itz_mst_boi**
"""

spam_msg = f"""
**ʜᴇʟᴘ sᴘᴀᴍ ᴄᴍᴅs**

**spam**: sᴘᴀᴍs  ᴀ  ᴍᴇssᴀɢᴇ ғᴏʀ ɢɪᴠᴇɴ  ᴄᴏᴜɴᴛᴇʀ(<= 100).
command:
i) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}spam <count> <replying any message>

**bigspam**: sᴘᴀᴍs ᴀ  ᴍᴇssᴀɢᴇ ғᴏʀ  ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ.
command:
i) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}bigspam <count> <replying any message>

**delayspam**: ᴅᴇʟᴀʏ  sᴘᴀᴍ ᴀ ᴛᴇxᴛ ғᴏʀ  ɢɪᴠᴇɴ  ᴄᴏᴜɴᴛᴇʀ ᴀғᴛᴇʀ ɢɪᴠᴇɴ ᴛɪᴍᴇ.
command:
i) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}delayspam <delay> <count> <replying any message>

**pornspam**: ᴘᴏʀɴᴏɢʀᴀᴘʜʏ sᴘᴀᴍ.
command:
i) {hl}pornspam <count>

**hang**: sᴘᴀᴍs ʜᴀɴɢɪɴɢ ᴍᴇssᴀɢᴇ ғᴏʀ  ɢɪᴠᴇɴ  ᴄᴏᴜɴᴛᴇʀ.
command:
i) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

** © @itz_mst_boi**
"""                     
           
           
@Mlk.on(events.CallbackQuery(pattern=r"help_back"))
@Mlk2.on(events.CallbackQuery(pattern=r"help_back"))
@Mlk3.on(events.CallbackQuery(pattern=r"help_back"))
@Mlk4.on(events.CallbackQuery(pattern=r"help_back"))
@Mlk5.on(events.CallbackQuery(pattern=r"help_back"))
@Mlk6.on(events.CallbackQuery(pattern=r"help_back"))
@Mlk7.on(events.CallbackQuery(pattern=r"help_back"))
@Mlk8.on(events.CallbackQuery(pattern=r"help_back"))
@Mlk9.on(events.CallbackQuery(pattern=r"help_back"))
@Mlk10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            Mlk_Help,
            buttons=[
                [
            Button.inline("sᴘᴀᴍ", data="spam"),
            Button.inline("ʀᴀɪᴅ", data="raid"),
           ],
           [
            Button.inline("ᴇxᴛʀᴀ ᴄᴍᴅs ", data="extra"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/mukeshbotzone")
           ],
           ],
        )           
   else:
        Alert = (
                "ɴᴏᴏʙ !! ᴍᴀᴋᴇ  ʏᴏᴜʀ   ᴏᴡɴ ᴍᴜᴋᴇsʜ X sᴘᴀᴍ  ʙᴏᴛs  ᴄᴏɴᴛᴀᴄᴛ ғᴏʀ ʀᴇᴘᴏ @itz_mst_boi !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@Mlk.on(events.CallbackQuery(pattern=r"spam"))
@Mlk2.on(events.CallbackQuery(pattern=r"spam"))
@Mlk3.on(events.CallbackQuery(pattern=r"spam"))
@Mlk4.on(events.CallbackQuery(pattern=r"spam"))
@Mlk5.on(events.CallbackQuery(pattern=r"spam"))
@Mlk6.on(events.CallbackQuery(pattern=r"spam"))
@Mlk7.on(events.CallbackQuery(pattern=r"spam"))
@Mlk8.on(events.CallbackQuery(pattern=r"spam"))
@Mlk9.on(events.CallbackQuery(pattern=r"spam"))
@Mlk10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< ʙᴀᴄᴋ ", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "ɴᴏᴏʙ !! ᴍᴀᴋᴇ ʏᴏᴜʀ  ᴏᴡɴ  ᴍᴜᴋᴇsʜ X sᴘᴀᴍ  ʙᴏᴛs  !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@Mlk.on(events.CallbackQuery(pattern=r"raid"))
@Mlk2.on(events.CallbackQuery(pattern=r"raid"))
@Mlk3.on(events.CallbackQuery(pattern=r"raid"))
@Mlk4.on(events.CallbackQuery(pattern=r"raid"))
@Mlk5.on(events.CallbackQuery(pattern=r"raid"))
@Mlk6.on(events.CallbackQuery(pattern=r"raid"))
@Mlk7.on(events.CallbackQuery(pattern=r"raid"))
@Mlk8.on(events.CallbackQuery(pattern=r"raid"))
@Mlk9.on(events.CallbackQuery(pattern=r"raid"))
@Mlk10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< ʙᴀᴄᴋ ", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "ɴᴏᴏʙ !! ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ᴍᴜᴋᴇsʜ X sᴘᴀᴍ ʙᴏᴛs !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       
@Mlk.on(events.NewMessage(incoming=True, pattern=r"\%slovereplyraid(?: |$)(.*)" % hl))
@Mlk2.on(events.NewMessage(incoming=True, pattern=r"\%slovereplyraid(?: |$)(.*)" % hl))
@Mlk3.on(events.NewMessage(incoming=True, pattern=r"\%slovereplyraid(?: |$)(.*)" % hl))
@Mlk4.on(events.NewMessage(incoming=True, pattern=r"\%slovereplyraid(?: |$)(.*)" % hl))
@Mlk5.on(events.NewMessage(incoming=True, pattern=r"\%slovereplyraid(?: |$)(.*)" % hl))
@Mlk6.on(events.NewMessage(incoming=True, pattern=r"\%slovereplyraid(?: |$)(.*)" % hl))
@Mlk7.on(events.NewMessage(incoming=True, pattern=r"\%slovereplyraid(?: |$)(.*)" % hl))
@Mlk8.on(events.NewMessage(incoming=True, pattern=r"\%slovereplyraid(?: |$)(.*)" % hl))
@Mlk9.on(events.NewMessage(incoming=True, pattern=r"\%slovereplyraid(?: |$)(.*)" % hl))
@Mlk10.on(events.NewMessage(incoming=True, pattern=r"\%slovereplyraid(?: |$)(.*)" % hl))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< ʙᴀᴄᴋ ", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "ɴᴏᴏʙ  !! ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ᴍᴜᴋᴇsʜ X sᴘᴀᴍ ʙᴏᴛs !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)

@Mlk.on(events.CallbackQuery(pattern=r"extra"))
@Mlk2.on(events.CallbackQuery(pattern=r"extra"))
@Mlk3.on(events.CallbackQuery(pattern=r"extra"))
@Mlk4.on(events.CallbackQuery(pattern=r"extra"))
@Mlk5.on(events.CallbackQuery(pattern=r"extra"))
@Mlk6.on(events.CallbackQuery(pattern=r"extra"))
@Mlk7.on(events.CallbackQuery(pattern=r"extra"))
@Mlk8.on(events.CallbackQuery(pattern=r"extra"))
@Mlk9.on(events.CallbackQuery(pattern=r"extra"))
@Mlk10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< ʙᴀᴄᴋ ", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "ɴᴏᴏʙ  !! ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ᴍᴜᴋᴇsʜ X sᴘᴀᴍ ʙᴏᴛs !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)

