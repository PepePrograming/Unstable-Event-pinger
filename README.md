# Unstable-Event-pinger
Setup a python discord bot that pings on Unstable Universe voice and message events

## Download python and dependencies:

### Windows:
1. open cmd and run `winget install -e --id Python.Python.3.11`  | download [Python](https://www.python.org/downloads/)
2. also run `python -m pip install discord.py-self aiohttp`      | download dependencies

### Linux:
1. create a python-env and install the requirements in there. Then run the script via console. For help ask AI

## Bot setup
1. If not done download [main.py](main.py)
2. open any file editor and modify the <br />
   `TOKEN = 'and replace this with a discord user token'` - DON'T share with anyone <br />
   `'webhook': 'and replace this with a discord webhook link'` - DON'T share with anyone <br />
   `'messageRole': 0,` - replace 0 with a role ID - message pings <br />
   `'voiceRole': 0,` - replace 0 with a role ID - voicechat pings <br />
3. Make sure your account has joined the discord server
4. Just launch the bot after saving

## Important
Using this bot can get your discord account banned for breaking [Discords TOS](https://support.discord.com/hc/en-us/articles/115002192352-Automated-User-Accounts-Self-Bots). Unlikely but possible - recommended to use an alt. Sharing the discord token can lead to ur account being hacked and sharing your discord webhook can lead to your server getting nuked.

Use at your own risk

## License
   This project is licensed under the **GPL-3.0** license.  
   See the [LICENSE](LICENSE.md) file for full details.
   
## Public Use
   If you deploy this bot publicly, please keep a Discord invite link easily accessible to users so they can join the official server.

## Help
1. [Get discord token](https://www.youtube.com/watch?v=LnBnm_tZlyU)
2. [Create discord webhook](https://www.youtube.com/watch?v=xXPnUGrQpBY)

##
If you have further questions feel free to ask in the discord server:<br />
   https://discord.gg/FmWqWd78aK
