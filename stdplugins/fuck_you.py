"""Emoji

Available Commands:

.think"""

from telethon import events

import asyncio


@borg.on(events.NewMessage(pattern=r"\/(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "chootyou":

        await event.edit(input_str)

        animation_chars = [
            "F̷̠͓̪̄̋̃̒̚Ǘ̴̟̲̲̗̟̻͚͓̙̳̰̟͎͉̤̞̠̖͔̘̫͔͙̈͌̾̐̀͑̍̃͆̈́͜͝Ċ̶̨̢͍̠̯̻͎̳̱̞̪̘̞̭͙͓̥̺̭̿̾̿̀͑̾̊̓̐͛͑̐́͛̇͐̃̀̄̅͆̀͊̏̉̈́̈́̀͌́͑͛̑́͐̐͝͠͝ͅK̷̨̨̛̛̜̤͉̬̜̖̪͎̞̗̺͇̜̥̹͖͍͍̮̙̭̼̀̐͑̒̏̆͂̆̑̚̚͝͠ͅͅ ̶̛̱̞̙̠͖͉̜̖̺̳͈̗̌̌͗͐̑̌͋̓̆͐̿͊̐̄̄͐́̋͛͑͝Ý̴̡̧̧̧̡̧̛̜͓͍̻̙̼̩̮̫̘͇̣͇̣̼͔͍͉̭͍̰̩̬̱̺̄̽̔̅̾̈́͌̈͂̈́̈̍́̑̾̕ͅǑ̵̡̧̱̤̼͔̜̰̺̣͓͇̂̾͌́̏̈̽̏́̐̊͑̂͌͛́́͑̕͝Ų̵̧̨̢̨̢͖̞͉̦͓͖̭͔̤͙̳̣̫̯̪̥̝̩͖͕̖̉̏̂͊͋̇̈̆́̈́̈́͗̇̍̍̃͜͜͜͠ͅ",
            "F̵̨̰͖̱̻̞̙̯̟̖͓̺̞͍̺̤̙͔̩̍̈́̀̆̉͑̉̒͜͜Ụ̴̡̢̜̥̙̱͓͈̹̼͕̠̫͎̰̞̟͓̦̗̜̫̦̞̀̇̽̏̀̍̃̉̒͐̆͐̆̄̆̎͂̈́͜ͅͅC̵̨̡̛͖̳͇̦̞͍̘͉͉͓̝̪̼̗̦̓̋̋̽̓̏̿̽͂͛́̋̒͌́̃̅͌́̊͌̈́͌͗̚͜͠ͅͅK̷̨̢̧̛̯̩͉̘͙̫̺͙̙̲̩̯̏̆̽̅̂͊͌̏̎͑͌͌͐͂̊̾̇̍̃̒̈ͅ ̷̨̢̤̲̬̲̙̻̳̺̠̲̪̻̫̝̫̼̩̠̻̘̠͓̹̒͜͝Y̶̙̻͙̬͚̐͂̇̋̿̐O̴̢̠̘̤̣̻̠̫͖̹̟͇͓̖̼̣̲͎̪̬̩̮̯̰̪̘̿͑͆̊͐̉̏̆̃Ǘ̴͇̻̲̣͍̠̟͚͔͎̝̬͊̅̏̕",
            "F̶̧͎̘̫̳͚̲͈̳̳̙̰͉̼͓̖͇̹̳̗͒͒̓̊̾̌̇͋͋͒̀̅̋̇̃̏̒̈̚̚̚͘͝͝U̴̢̺̺̯̥̺͔͚̬͉̝͈̖̳͓̘̺͖̰͒̾̾̽̏̂̇̽Ç̸̨̡͙̞̹̹̝̯͔̞̰̺̞̰̳͚̣̭͇͚͙͛͂͊̀͐̌̓͌͛̾͌̆̽̕͜͠K̵̛̛̙̲̹̯͇̣̱̭͐͂́ ̸̡̛̥̗̳͈̥͇̳̃͑̽ͅY̷̡̞̥͙͇̳̦̳̗̩͙̘̞̯̻̟̲̱̭͓͖͑̇͋͋̆̀̏͜Ȯ̴̼͖̤͓̥̤̖̦͔̝͔̳̰̼͍̳͇̝̞̟͕͙̟͂̏̎̚͜Ú̴̠͉̯͖̦͔̬͇̻͚̬̙̙̭͍̠͙̦̫̗̞̝͆͒̋̊͂̉̇̚͜͝",
            "F̷̛͕͈̹̟̭̲͙͚͇̅̃͑Ư̷̙̤̬͖͇̥̱̰̜̠̻͓̙̔̉͆̊̐͋̅̀̄̀͂̋̕C̵̛͈̭̺̪̯̣̟̣̼̟͎̭̾͒̍͌̄̄̊̐͑̉ͅK̷̨̨̲̲̤͚̻͎̱̞̆͂̊̉̍̅͑̈́̊̎̆̕͝͝͝ͅ ̴̧͈͚̜͔̮͉̭͓̥̯̭͎͚̮͒̓͐͜͠Y̵͇̯͑͆̂̉Õ̵̡̢̼̤͙̳̬̩͉͕̮͈̬͈̝̞̹̲̣̼̬͂̋̈́̀͌͊́̅̓̍̕̚̚U̸͎̗̫̣͍̩̘̮̦̤͎̝̰͖͓͐͗̈́͝",
            "F̷̢̢̧̛͕̬̞̙̼̳̗͕̮͇͇͉̣̘̦̀̈́̌͂̾̓́̄̒̆̈́̋́Ứ̸̡̡̮͍̗̮̲͙̣̪͕͖̰̞̼̗̱̦̼͙͖̪̘̗͙̹̇́̀͌͛̀̉̓͐̏̏̈̃̈́̐͛͛̒̉͋̿̄̽̇̃̍̍͒̄̇͋̑̆͗̊̅̑̅͗͌̌̅͋͛̇́͒̋̕̚͜͝͠ͅÇ̴̢̛̞͔̖̠̜̟̞̹͕̥̭̫̲̝̲̩̲̦̪͇͔̥̤̻̝̳̭̣̜̎́̓̋̒̊͆̀̄̌̈́̍͒́̋͌͌̒̉̈́̂̏͛̾̉̆̉̆̉͆̋͂̽̎̓̇͑̓́͊̚͘̕̕͘͠K̷̡̧̡̨̡̧̧̢̡̨̛̜̱͍͔̳͎̯͓͉̙͓̤̪̜͉̤̪̯̫͙͙̳̱̭͈̱̮̹̫͚͔͚̠̲̦̱̖̮̪̥̰͖͕̠̀̇̃̑͗̚ͅ ̶̨̡̡̧̨̛̛͓͉͔̖͍͙͉͖̪̳͈̹̪͇̬̙̫̫̦͈̱̪̘͈̲̬̯͚͖̣̮̲̪̫̩̱̟̲͎͈̤̫̭͎̳̱̩̗͇̔̔̔͊̒̃̑͊̈́̄̇̆͊̏̍̋͑̅͊̾̂͂̇̐͐̊̾̎͆͆̎̈́̓̓͂̊̍̔͐̑͊̋̇͒͊͂̒́̏̂̕̕͝͝͠͠Ÿ̷̨̟̝̱́͌̔̔̊̈́̈̃̋͋͛̎̓́̆̂̐̈́̊̒̇̎͛̓̈́̐͊͊͛̇̔̅̔̈́͒̈̈́̑̒͊̏̂̍̚̚̕͠͝͝O̶̧̨͚͇̘͉͉̙̲̹̯͕̙̱͙̲̹̺̟̪̼͙̹̦̙͍̮̘̮̬̺̮͖̭͊͒̓̋̄͆͌̄̂͑̇̕͜͠ͅŲ̵̨̢̧̹͚̙͚̜̠͈̫͔̠̹̤̺̮̰̩̳̲̘̞̙̦͕̳͕̰̺̜̜̳͖͙͎̗̃͐̍͊̎͌͑̈́̾̀͜͜͝"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 103])
