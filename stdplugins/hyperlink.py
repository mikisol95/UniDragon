# For UniBorg
# By Priyam Kalra
# Syntax (.link <text_to_highlight> <link>)

"""HyperLink module for Uniborg
\nType .hl <text to highlight> <link>
"""
from telethon import events
from uniborg.util import admin_cmd
import asyncio
from telethon.tl import functions, types

@borg.on(admin_cmd(pattern="hl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    string = event.pattern_match.group(1)
    strings = string.split()
    link = strings[-1]
    strings = strings[:-1]
    string = " ".join(strings)
    output = f"[{string}]({link})"
    await event.edit(output)


