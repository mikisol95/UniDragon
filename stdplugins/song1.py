"get music from .imusic/.spotbot <music query>  Credits https://t.me/By_Azade"
import logging
from uniborg.util import admin_cmd
from uniborg import MODULE
MODULE.append("song1")

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)


@borg.on(admin_cmd(pattern="imusic ?(.*)"))  # pylint:disable=E0602
async def music_find(event):
    if event.fwd_from:
        return

    music_name = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if music_name:
        await event.delete()
        song_result = await event.client.inline_query("deezermusicbot", music_name)

        await song_result[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            hide_via=True
        )
    elif msg:
        await event.delete()
        song_result = await event.client.inline_query("deezermusicbot", msg.message)

        await song_result[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            hide_via=True
        )


@borg.on(admin_cmd(pattern="spotbot ?(.*)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    msg = await event.get_reply_message()
    await event.delete()

    music_name = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if music_name:
        await event.delete()
        song_result = await event.client.inline_query("spotify_to_mp3_bot", music_name)

        for res in range(len(song_result)):

            if "(FLAC)" in song_result[res].title:

                j = await song_result[res].click(event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True)
                k = await event.respond(j)
                await j.delete()
                await k.edit("`Error Sar`")
                break

            elif "(MP3_320)" in song_result[res].title:

                j = await song_result[res].click(event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True)
                k = await event.respond(j)
                await j.delete()
                await k.edit("`Error Sar`")
                break

            elif "(MP3_128)" in song_result[res].title:

                j = await song_result[res].click(event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True)
                k = await event.respond(j)
                await j.delete()
                await k.edit("`Error Sar`")
                break

    elif msg:

        await event.delete()
        song_result = await event.client.inline_query("spotify_to_mp3_bot", msg.message)
        for res in range(len(song_result)):

            if "(FLAC)" in song_result[res].title:

                j = await song_result[res].click(event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True)
                k = await event.respond(j)
                await j.delete()
                await k.edit("`Error Sar`")
                break

            elif "(MP3_320)" in song_result[res].title:

                j = await song_result[res].click(event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True)
                k = await event.respond(j)
                await j.delete()
                await k.edit("`Error Sar`")
                break

            elif "(MP3_128)" in song_result[res].title:

                j = await song_result[res].click(event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True)
                k = await event.respond(j)
                await j.delete()
                await k.edit("`Error Sar`")
                break
