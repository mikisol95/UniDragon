
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="sg ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```Reply to text message```")
        return
    chat = "@SangMataInfo_bot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=461843263))
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @sangmatainfo_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit("```can you kindly disable your forward privacy settings for good?```")
        else:
            await event.edit(f"{response.message.message}")


@borg.on(admin_cmd(pattern=("fakemail ?(.*)")))
async def _(event):
    if event.fwd_from:
        return
    chat = "@fakemailbot"
    await event.edit("```Fakemail Creating, wait```")
    async with borg.conversation(chat) as conv:
        try:
            await event.client.send_message("@fakemailbot", "/generate")
            await asyncio.sleep(5)
            k = await event.client.get_messages(entity="@fakemailbot", limit=1, reverse=False)
            mail = k[0].text
            # print(k[0].text)
        except YouBlockedUserError:
            await event.reply("```Please unblock @fakemailbot and try again```")
            return
        await event.edit(mail)


@borg.on(admin_cmd(pattern="mailid ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@fakemailbot"
    await event.edit("```Fakemail list getting```")
    async with borg.conversation(chat) as conv:
        try:
            await event.client.send_message("@fakemailbot", "/id")
            await asyncio.sleep(5)
            k = await event.client.get_messages(entity="@fakemailbot", limit=1, reverse=False)
            mail = k[0].text
            # print(k[0].text)
        except YouBlockedUserError:
            await event.reply("```Please unblock @fakemailbot and try again```")
            return
        await event.edit(mail)


@borg.on(admin_cmd(pattern="ub ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```reply to text message```")
        return
    chat = "@uploadbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=97342984))
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @sangmatainfo_bot and try again```")
            return
        if response.text.startswith("Hi!,"):
            await event.edit("```can you kindly disable your forward privacy settings for good?```")
        else:
            await event.edit(f"{response.message.message}")


@borg.on(admin_cmd(pattern="gid ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```reply to text message```")
        return
    chat = "@getidsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=186675376))
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Nikal Gendu```")
            return
        if response.text.startswith("Hello,"):
            await event.edit("```can you kindly disable your forward privacy settings for good?```")
        else:
            await event.edit(f"{response.message.message}")


@borg.on(admin_cmd(pattern="urban ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    bsdk = event.pattern_match.group(1)
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    if not bsdk:
        reply_message = await event.get_reply_message()
    bsdk = reply_message.text
    if not bsdk:
        await event.edit("```Reply to a Text message```")
        return
    chat = "@UrbanDictionaryBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Processing```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=185693644))
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Nikal Gendu```")
            return
        if response.text.startswith("Hello,"):
            await event.edit("```Can you Kindly disable your forward privacy settings for good?```")
        else:
            await event.edit(f"{response.message.message}")


@borg.on(admin_cmd(pattern="voicy ?(.*)"))
async def voicy(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Please reply to a Message`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`Reply to a Media`")
        return
    chat = "@Voicybot"
    reply_message.sender
    await event.edit("`Haha Wait...`")
    async with event.client.conversation(chat) as conv:
        try:
            await event.client.forward_messages(chat, reply_message)
        except YouBlockedUserError:
            await event.reply(f"`Mmmh sanırım` {chat} `engellemişsin. Lütfen engeli aç.`")
            return

        response = conv.wait_event(events.MessageEdited(
            incoming=True, from_users=259276793))
        response = await response
        if response.text.startswith("__👋"):
            await event.edit("`Botu başlatıp Türkçe yapmanız gerekmektedir.`")
        elif response.text.startswith("__👮"):
            await event.edit("`Ses bozuk, ne dediğini anlamadım.`")
        else:
            await event.edit(f"`{response.text}`")
