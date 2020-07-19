from datetime import datetime
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="ping", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    ed = await event.reply("Pong!")
    start = datetime.now()
    await ed.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await ed.edit("**Pong!**\n`{}` __ms__".format(ms))
