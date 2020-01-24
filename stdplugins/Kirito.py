"""Emoji
Available Commands:
.kirito
.nikita
.eye
.netflix"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 30)

    input_str = event.pattern_match.group(1)

    if input_str == "kirito":

        await event.edit(input_str)

        animation_chars = [

            "😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "◼️◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "◼️◼️◼️️😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "◼️◼️◼️◼️😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "‎◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️◼️",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️◼️\n◼️😈kirito, Eyepatch😈◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️😈kirito, Eyepatch😈◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",

            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",

            "◼️◼️\n◼️◼️",

            "◼️"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 30])

  
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
 
async def _(event):
 
    if event.fwd_from:
 
        return
 
    animation_interval = 2
 
    animation_ttl = range(0, 11)
 
    input_str = event.pattern_match.group(1)
 
    if input_str == "netflix":
 
        await event.edit(input_str)
 
        animation_chars = [
        
            "`Cracking some Netflix account.....`",
           
            "`Cracking ... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Cracking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Cracking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Cracking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Cracking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Cracking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Cracking... 84%\n█████████████████████▒▒▒▒ `",
        "`Cracked... 100%\n█████████Cracked ███████████ `",
        "`I'd :- *************@gmail.com\n\nPassword:-**********`",   
 
 "`Account Cracked ..\n\n Pay 2$ to @kirito6969 for I'd and Password`"
        ]
 
        for i in animation_ttl:
 
            await asyncio.sleep(animation_interval)
 
            await event.edit(animation_chars[i % 11])
 
 
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
 
async def _(event):
 
    if event.fwd_from:
 
        return
 
    animation_interval = 0.3
 
    animation_ttl = range(0, 30)
 
    input_str = event.pattern_match.group(1)
 
    if input_str == "nikita":
 
        await event.edit(input_str)
 
        animation_chars = [
 
            "👑Nikita👑👑👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",
 
            "◼️👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",
 
            "◼️◼️👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",
 
            "◼️◼️◼️️👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",
 
            "◼️◼️◼️◼️👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",
 
            "‎◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",
 
            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",
 
            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",
 
            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",
 
            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️",
 
            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑◼️◼️",
 
            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑◼️◼️◼️",
 
            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑◼️◼️◼️◼️",
 
            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️◼️◼️◼️◼️",
 
            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️◼️◼️◼️◼️",
 
            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️◼️◼️◼️◼️",
 
            "◼️◼️◼️◼️◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️◼️◼️◼️◼️",
 
            "◼️◼️◼️◼️◼️\n◼️◼️👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️◼️◼️◼️◼️",
 
            "◼️◼️◼️◼️◼️\n◼️◼️◼️👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️◼️◼️◼️◼️",
 
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️◼️◼️◼️◼️",
 
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Nikita👑👑Nikita👑◼️◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️◼️◼️◼️◼️",
 
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Nikita👑👑Nikita👑◼️◼️\n◼️👑Nikita👑👑Nikita👑◼️◼️\n◼️◼️◼️◼️◼️",
 
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Nikita👑👑Nikita👑◼️◼️\n◼️👑Nikita👑◼️◼️◼️\n◼️◼️◼️◼️◼️",
 
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Nikita👑👑Nikita👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
 
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️👑Nikita👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
 
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
 
            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",
 
            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",
 
            "◼️◼️\n◼️◼️",
 
            "◼️",
            "👑 Nikita 👑"
        ]
 
        for i in animation_ttl:
 
            await asyncio.sleep(animation_interval)
 
            await event.edit(animation_chars[i % 31])
    
    
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "eye":

        await event.edit(input_str)

        animation_chars = [

            "👁👁\n  👄  =====> Abey Ja Na Gandu",
            "👁👁\n  👅  =====> Abey Ja Na Madarchod",    
            "👁👁\n  💋  =====> Abey Ja Na Randi",
            "👁👁\n  👄  =====> Abey Ja Na Betichod",
            "👁👁\n  👅  =====> Abey Ja Na Behenchod",    
            "👁👁\n  💋  =====> Abey Ja Na Na Mard",
            "👁👁\n  👄  =====> Abey Ja Na Randi",
            "👁👁\n  👅  =====> Abey Ja Na Bhosdk",    
            "👁👁\n  💋  =====> Abey Ja Na Chutiye",
            "👁👁\n  👄  =====> Hi All, How Are You Guys..."
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 9])
