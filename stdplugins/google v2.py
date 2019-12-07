import datetime
import asyncio
import shutil
from bs4 import BeautifulSoup
import re
from html import unescape
from re import findall
from selenium import webdriver
from urllib.parse import quote_plus
from urllib.error import HTTPError
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from requests import get
from search_engine_parser import GoogleSearch
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import asyncio
from telethon import events
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="google (.*)"))
async def gsearch(q_event):
    """ For .google command, do a Google search. """
    match = q_event.pattern_match.group(1)
    page = findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(11):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"{i}. [{title}]({link})\n`{desc}`\n\n"
        except IndexError:
            break
    await q_event.edit("**Search Query:**\n`" + match + "`\n\n**Results:**\n" +
                       msg,
                       link_preview=False)
