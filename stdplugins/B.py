from telethon import events
import random
import asyncio

@borg.on(events.NewMessage(pattern=r"\.b(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str in "nani":
            emoticons = ["┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛",
                                "╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯"
                                ]
    index = random.randint(0, len(emoticons))
    output_str = emoticons[index]
    await event.edit(output_str)