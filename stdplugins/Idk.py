from telethon import events

import random, re

from uniborg.util import admin_cmd


NOOBSTR = [
    "`YOU PRO NIMBA DONT MESS WIDH MEH`",
    "`Haha yes`",
    "`NOOB NIMBA TRYING TO BE FAMOUS KEK`",
    "`Sometimes one middle finger isn’t enough to let someone know how you feel. That’s why you have two hands`",
    "`Some Nimbas need to open their small minds instead of their big mouths`",
    "`UH DONT KNOW MEH SO STAY AWAY LAWDE`",
    "`Kysa kysaaaa haaan? Phir MAAR nhi Khayega tu?`",
    "`Zikr Jinka hota hai galiyo meh woh bhosdika ajj paya gya naliyo me`",
]


@borg.on(admin.cmd("peru ?(.*)"))
async def _(event):
    if  event.fwd_from:
                   return
bro = random.randint(0, len(NOOBSTR) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = NOOBSTR[bro]
    await event.edit(reply_text)
