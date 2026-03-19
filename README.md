# Unstable-Event-pinger
Setup a python discord bot that pings on Unstable Universe voice and message events

Download python and dependencies:

### Windows:
1. open cmd and run `winget install -e --id Python.Python.3.11`  | download Python
2. run `pip install discord.py aiohttp`                          | download dependencies

## bot setup
1. open any file editor and modify the
   1. TOKEN = 'and replace this with a discord user token'          | don't show this setting to anyone - you can get hacked
   2. 'webhook': 'and replace this with a discord webhook link'     | don't show this setting to anyone - your server can be spammed
   3. 'messageRole': 0,                                             | replace 0 with a role you want to be pinged on a message
   4. 'voiceRole': 0,                                               | replace 0 with a role you want to be pinged when someone joins a VC
