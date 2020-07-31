"""Restart or Terminate the bot from any chat
Available Commands:
.reboot
.shutdown"""
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.reboot", outgoing=True))
async def _(event):
    if event.fwd_from:
        return

    await event.edit("`Bye... *windows XP shut down sound*`")
    await asyncio.sleep(10)
    await event.edit("`Me Back! Try .on`")
    asyncio.get_event_loop().create_task(restart())


@borg.on(events.NewMessage(pattern=r"\.shutdown", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await asyncio.sleep(3)
    await event.edit("✅🔓🔓🔓🔓🔓🔓🔓")
    await asyncio.sleep(3)
    await event.edit("☑️🔐🔐🔐🔐🔐🔐🔐")
    await asyncio.sleep(3)
    await event.edit("❌🔒🔒🔒🔒🔒🔒🔒")
    await borg.disconnect()


async def restart():
    await borg.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
