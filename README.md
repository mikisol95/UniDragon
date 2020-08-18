⚠️Warning: // **Multiple accounts are getting banned, // Hence, Use it at your own RISK .** :( /

#Click the ninja image below to deploy yo heroku.

[![Build](https://github.com/prono69/PepeBot/workflows/FailedChecker/badge.svg?branch=master)](https://github.com/prono69/PepeBot/actions "Build")
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/61152ca51cc6417bb9866562f3dfbf76)](https://app.codacy.com/manual/prono69/PepeBot?utm_source=github.com&utm_medium=referral&utm_content=prono69/PepeBot&utm_campaign=Badge_Grade_Settings)
[![Deploy](https://telegra.ph/file/4cb73b43c6a190638071a.jpg)](https://heroku.com/deploy?template=https://github.com/prono69/PepeBot/tree/master)


This deploy button

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

#### Code Quality

[![CodeFactor](https://www.codefactor.io/repository/github/prono69/pepebot/badge)](https://www.codefactor.io/repository/github/prono69/pepebot)

#### The Legacy Way
Simply clone the repository and run the main file:
```sh
git clone https://github.com/muhammedfurkan/uniborg.git
cd uniborg
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create config.py with variables as given below>
python3 -m stdborg YourSessionName
```
 
An example `config.py` file could be:
 
**Not All of the variables are mandatory**
 
__The UniBorg should work by setting only these variables__
 
```python3
from sample_config import Config
 
class Development(Config):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
  TG_BOT_TOKEN_BF_HER = ""
  TG_BOT_USER_NAME_BF_HER = ""
  UB_BLACK_LIST_CHAT = []
  # specify LOAD and NO_LOAD
  LOAD = []
  NO_LOAD = []
```
 
## internals
 
The core features offered by the custom `TelegramClient` live under the
[`uniborg/`](https://github.com/muhammedfurkan/uniborg/tree/master/uniborg)
directory, with some utilities, enhancements, the `_core` plugin, and the `_inline_bot` plugin.
 
 
- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will work without setting the non-mandatory environment variables.
