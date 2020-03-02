"""IX.IO pastebin like site
Syntax: .paste
        .getp <to get the dogbin content>"""
import asyncio
from datetime import datetime
import os
import requests
from requests import get, exceptions
from uniborg.util import admin_cmd
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.WARN)


def progress(current, total):
    logger.info("Downloaded {} of {}\nCompleted {}".format(current, total, (current / total) * 100))

DOGBIN_URL = "https://del.dog/"
BOTLOG = Config.PM_LOGGR_BOT_API_ID

@borg.on(admin_cmd(pattern="paste ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    input_str = event.pattern_match.group(1)
    message = "SYNTAX: `.paste <long text to include>`"
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await borg.download_media(
                previous_message,
                Config.TMP_DOWNLOAD_DIRECTORY,
                progress_callback=progress
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8") + "\r\n"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        message = "SYNTAX: `.paste <long text to include>`"
    url = "https://del.dog/documents"
    r = requests.post(url, data=message.encode("UTF-8")).json()
    url = f"https://del.dog/{r['key']}"
    end = datetime.now()
    ms = (end - start).seconds
    if r["isUrl"]:
        nurl = f"https://del.dog/v/{r['key']}"
        await event.edit("Dogged to {} in {} seconds. GoTo Original URL: {}".format(url, ms, nurl))
    else:
        await event.edit("`Pasted Successfully!..` \n[Here you Go BSDK]({})\n__Link Generated In__ **{}** __seconds__".format(url, ms))


@borg.on(admin_cmd(pattern="getp(?: |$)(.*)"))
async def get_dogbin_content(dog_url):
    """ For .get_dogbin_content command,
        fetches the content of a dogbin URL. """
    textx = await dog_url.get_reply_message()
    message = dog_url.pattern_match.group(1)
    await dog_url.edit("`Getting dogbin content . . .`")

    if textx:
        message = str(textx.message)

    format_normal = f'{DOGBIN_URL}'
    format_view = f'{DOGBIN_URL}v/'

    if message.startswith(format_view):
        message = message[len(format_view):]
    elif message.startswith(format_normal):
        message = message[len(format_normal):]
    elif message.startswith("del.dog/"):
        message = message[len("del.dog/"):]
    else:
        await dog_url.edit("`Are you sure you're \
                            using a valid dogbin URL?`")
        return

    resp = get(f'{DOGBIN_URL}raw/{message}')

    try:
        resp.raise_for_status()
    except exceptions.HTTPError as HTTPErr:
        await dog_url.edit(
            "Request returned an unsuccessful status code.\n\n" + str(HTTPErr))
        return
    except exceptions.Timeout as TimeoutErr:
        await dog_url.edit("Request timed out." + str(TimeoutErr))
        return
    except exceptions.TooManyRedirects as RedirectsErr:
        await dog_url.edit("Request exceeded the configured \
                        number of maximum redirections." + str(RedirectsErr))
        return

    reply_text = "`Fetched dogbin URL content "
    reply_text += "successfully!`\n\n`Content:` " + resp.text

    await dog_url.edit(reply_text)
    if BOTLOG:
        await dog_url.client.send_message(
            BOTLOG,
            "Get dogbin content query for `" + message + "` was \
executed successfully",
        )
