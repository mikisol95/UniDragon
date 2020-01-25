from telethon import events

@borg.on(events.NewMessage(pattern=r"\.test", outgoing=True))
async def test(event):
    if event.fwd_from:
        return 
    await event.edit("`Test Successfull`")      
