# COPYRIGHT (C) 2021 BY RetroBot22 AND PROBOYX, ALAIN

"""
(((((((((((((((((((((((@RetroBot22)))))))))))))))))))))))))))
(((((((((((((((((((((((@RetroBot22)))))))))))))))))))))))))))
(((((((((((((((((((((((@RetroBot22)))))))))))))))))))))))))))
(((((((((((((((((((((((@RetroBot22)))))))))))))))))))))))))))
                 MADE BY RetroBot AND PROBOY X
                   DISIGNED BY ALAIN_CHAMPION
                   CREDITS #TEAMLEGEND 
                PLEASE DON'T REMOVE THIS LINES
"""

from telethon import events, Button, custom
import re, os
from RetroBot import PHOTO, xbot, BOT, VERSION
from userbot import bot
@xbot.on(events.NewMessage(pattern=("/alive|/start")))
async def awake(event):
  RetroBot = f"ʜᴇʟʟᴏ ᴛʜɪs ɪs  {BOT}\n\n"
  RetroBot += "ᴀʟʟ sʏsᴛᴇᴍ ɪs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ\n\n"
  RetroBot += f"{BOT} VERSION : {VERSION} ʟᴀsᴛᴇsᴛ\n\n"
  RetroBot += f"ᴍʏ ᴍᴀsᴛᴇʀ @{bot.me.username} ☺️\n\n"
  RetroBot += "ғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ\n\n"
  RetroBot += "ᴛᴇʟᴇᴛʜᴏɴ : 1.20 LATEST\n\n"
  RetroBot += "ᴛʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ"
  BUTTON = [[Button.url("𝙼𝙰𝚂𝚃𝙴𝚁", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} 𝚁𝙴𝙿𝙾", "https://github.com/RetroBotOP/LEGEND-BOT")]]
  BUTTON += [[custom.Button.inline("𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈", data="RetroBot")]]
  await xbot.send_file(event.chat_id, PHOTO, caption=RetroBot,  buttons=BUTTON)




@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"RetroBot")))
async def callback_query_handler(event):
# inline by RetroBot22 and PROBOY22 🔥
  PROBOYX = [[Button.url("REPO-LEGEND", "https://github.com/RetroBotOP/LEGEND-BOT")]]
  PROBOYX +=[[Button.url("DEPLOY-LEGEND", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FRetroBotOP%2Flegendpack&template=https%3A%2F%2Fgithub.com%2FRetroBotOP%2Flegendpack")]]
  PROBOYX +=[[Button.url("TUTORIAL", "https://youtu.be/rGCSSFPsS4Q"), Button.url("STRING-SESSION", "https://repl.it/@legendx22/LEGEND-BOT#main.py")]]
  PROBOYX +=[[Button.url("API_ID & HASH", "https://t.me/usetgxbot"), Button.url("REDIS", "https://redislabs.com")]]
  PROBOYX +=[[Button.url("SUPPORT CHANNEL", "https://t.me/LEGENDBOT_OFFICIAL"), Button.url("SUPPORT GROUP", "https://t.me/LEGEND_USERBOT_SUPPORT")]]
  PROBOYX +=[[custom.Button.inline("ALIVE", data="PROBOY")]]
  await event.edit(text=f"𝙰𝙻𝙻 𝙳𝙴𝚃𝙰𝙸𝙻𝚂 𝙾𝙵 𝚁𝙴𝙿𝙾𝚂", buttons=PROBOYX)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
# inline by RetroBot22 and PROBOY22 🔥
  RetroBot = f"ʜᴇʟʟᴏ ᴛʜɪs ɪs  {BOT}\n\n"
  RetroBot += "ᴀʟʟ sʏsᴛᴇᴍ ɪs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ\n\n"
  RetroBot += f"{BOT} OS : {VERSION} ʟᴀsᴛᴇsᴛ\n\n"
  RetroBot += f"ᴍʏ ᴍᴀsᴛᴇʀ @{bot.me.username} ☺️\n\n"
  RetroBot += "ғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ\n\n"
  RetroBot += "ᴛᴇʟᴇᴛʜᴏɴ : 1.20 LATEST\n\n"
  RetroBot += "ᴛʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ"
  BUTTONS = [[Button.url("𝙼𝙰𝚂𝚃𝙴𝚁", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} 𝚁𝙴𝙿𝙾", "https://github.com/RetroBotOP/LEGEND-BOT")]]
  BUTTONS += [[custom.Button.inline("𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈", data="RetroBot")]]
  await event.edit(text=RetroBot, buttons=BUTTONS)


@xbot.on(events.NewMessage(pattern=("/repo|#repo")))
async def repo(event):
  await xbot.send_message(event.chat, "ʀᴇᴘᴏ ᴏғ ʟᴇɢᴇɴᴅ-ʙᴏᴛ", buttons=[[Button.url("⚜️ ʀᴇᴘᴏ ⚜️", "https://github.com/RetroBotOP/LEGEND-BOT")]])
