# Adapted from OpenUserBot

"""Download & Upload Images on Telegram
Syntax: `.img <Name>` or `.img (replied message)`
\n Upgraded by @NeoMatrix90 aka @kirito6969
"""

import os
import shutil
from uniborg.util import admin_cmd
from userbot.utils.google_images_download import googleimagesdownload

@borg.on(admin_cmd(pattern="img ?(.*)"))
async def img_sampler(event):
	 """For .img command, search and return images matching the query."""
	 await event.edit("`Processing...Bsdk...`")
	 reply = await event.get_reply_message()
	 if event.pattern_match.group(1):
	 	query = event.pattern_match.group(1)
	 elif reply:
	 		query = reply.message
	 else:
	 	await event.edit("`What I am Supposed to Search u Dumb Ass(Donkey)`")
	 	return
	 	
	 	lim = findall(r"lim=\d+", query)
	 	try:
	 		lim = lim[0]
	 		lim = lim.replace("lim=", "")
	 		query = query.replace("lim=" + lim[0], "")
	 	except IndexError:
	 		lim = 6
	 		response = googleimagesdownload()
	 		
	 # Creating List of Arguments
	 arguments = {
	 	"keywords": query,
	 	"limit": lim,
	 	"format": "jpg",
	 	"no_directory": "no_directory"
	 }	
	 
	 # passing the arguments to the function
	 paths = response.download(arguments)
	 lst = paths[0][query]
	 await event.client.send_file(
	 	await event.client.get_input_entity(event.chat_id), lst)
	 shutil.rmtree(os.path.dirname(os.pathabspath(lst[0])))
	 await event.delete()
