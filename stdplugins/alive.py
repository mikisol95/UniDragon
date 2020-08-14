# For UniBorg
# Syntax .alive
import sys
import platform
import psutil
from telethon import __version__
from uniborg.util import admin_cmd
from sql_helpers.global_variables_sql import SYNTAX, BUILD


@borg.on(admin_cmd(pattern="alive ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Config.USER is not None:
        user = f"\n**User: {Config.USER}**"
    else:
        user = ""
    uname = platform.uname()
    memory = psutil.virtual_memory()
    specs = f"System: {uname.system}\nRelease: {uname.release}\nVersion: {uname.version}\nProcessor: {uname.processor}\nMemory [RAM]: {get_size(memory.total)}"
    help_string = f"**General Info:**\n**Build: {BUILD}**\nUSER: {str(user)}\n**System Specifications:**\n{specs}\n**Python {sys.version}**\n**Telethon {__version__}**"
    # await event.client.send_file(event.chat_id,
    # file="CAADBQADgAEAAiriyVcBvpocd4kH1QI")
    await event.edit(help_string + "\n\n")
    # await event.delete()


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


SYNTAX.update({
    "alive": "\
**Requested Module --> alive**\
\n\n**Detailed usage of fuction(s):**\
\n\n```.alive```\
\nUsage: Returns userbot's system stats, user's name (only if set).\
"
})
