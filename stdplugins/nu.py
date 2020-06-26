import jikanpy
import html
from uniborg.util import admin_cmd
import datetime
import requests
import bs4
import textwrap

@borg.on(admin_cmd(pattern="user ?(.*)"))
async def user(event):
    search_query = event.pattern_match.group(1)
    message = await event.get_reply_message()
    if search_query:
    	pass
    elif message:
    	search_query = message.text
    else:
    	await event.edit("Format : .user <username>")
    	return

    jikan = jikanpy.jikan.Jikan()

    try:
        user = jikan.user(search_query)
    except jikanpy.APIException:
        await event.edit("Username not found.")
        return

    await event.edit("Searching.... ")

    date_format = "%Y-%m-%d"
    if user['image_url'] is None:
        img = "https://cdn.myanimelist.net/images/questionmark_50.gif"
    else:
        img = user['image_url']

    try:
        user_birthday = datetime.datetime.fromisoformat(user['birthday'])
        user_birthday_formatted = user_birthday.strftime(date_format)
    except:
        user_birthday_formatted = "Unknown"

    user_joined_date = datetime.datetime.fromisoformat(user['joined'])
    user_joined_date_formatted = user_joined_date.strftime(date_format)

    for entity in user:
        if user[entity] == None:
            user[entity] = "Unknown"

    about = user['about'].split(" ", 60)

    try:
        about.pop(60)
    except IndexError:
        pass

    about_string = ' '.join(about)
    about_string = about_string.replace("<br>", "").strip().replace("\r\n", "\n")

    caption = ""

    caption += textwrap.dedent(f"""
    *Username*: [{user['username']}]({user['url']})

    *Gender*: `{user['gender']}`
    *Birthday*: `{user_birthday_formatted}`
    *Joined*: `{user_joined_date_formatted}`
    *Days wasted watching anime*: `{user['anime_stats']['days_watched']}`
    *Days wasted reading manga*: `{user['manga_stats']['days_read']}`

    """)

    caption += f"*About*: {about_string}"
    await event.client.send_file(event.chat_id, file = user['url'],  caption=caption)

@borg.on(admin_cmd(pattern="s (kaizoku|kayo) ?(.*)"))    
async def site_search(event):
    message = await event.get_reply_message()
    search_query= event.pattern_match.group(2)
    site = event.pattern_match.group(1)
    if search_query:
    	pass
    elif message:
    	search_query = message.text
    else:
    	await event.edit("uff brah.")
    	return

    if site == "kaizoku":
        search_url = f"https://animekaizoku.com/?s={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "post-title"})

        if search_result:
            result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>AnimeKaizoku</code>: \n"
            for entry in search_result:
                post_link = entry.a['href']
                post_name = html.escape(entry.text)
                result += f"• <a href='{post_link}'>{post_name}</a>\n"
                await event.edit(result, parse_mode = 'HTML')
        else:
            result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>AnimeKaizoku</code>"
            await event.edit(result, parse_mode='HTML')

    elif site == "kayo":
        search_url = f"https://animekayo.com/?s={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "title"})

        result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>AnimeKayo</code>: \n"
        for entry in search_result:

            if entry.text.strip() == "Nothing Found":
                result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>AnimeKayo</code>"
                break

            post_link = entry.a['href']
            post_name = html.escape(entry.text.strip())
            result += f"• <a href='{post_link}'>{post_name}</a>\n"
            await event.edit(result, parse_mode='HTML')
    
