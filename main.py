import discord
from discord import Webhook, File
import asyncio
import aiohttp
import json
# ───────────────────────────────────────────────────────
#  WARNING: This is a self bot which violates discord TOS
# ───────────────────────────────────────────────────────
TOKEN = '' # put in your discord token

# Default config
config = {
    'webhook': '', # put in your discord webhook link

    'messagePing': True,
    'voicePing': True,
    'messageRole': 0,
    'voiceRole': 0,

    'server1': 1382494449934008433,
    'voiceRoleServer1': ["1382496063448940606","1382496298535751782"], # multi role support - e.g. ["1", "2"]
    'announceChannel': [1382502803058196612], # multi channel support - e.g. [1, 2]
}

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print(f"Ready at {discord.utils.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    # Forward announcement
    if (config.get('messagePing', False)
            and message.guild
            and message.guild.id == config['server1']
            and message.channel.id in config['announceChannel']
            and config.get('webhook')):

        content = (
            f"<@&{config['messageRole']}> channel name: __**{message.channel.name}**__ - <#{message.channel.id}>\n"
            f"{message.content}"
        )
        async with aiohttp.ClientSession() as session:
            try:
                webhook = Webhook.from_url(config['webhook'], session=session)
                await webhook.send(
                    content=content,
                    username=message.author.display_name,
                    avatar_url=message.author.avatar.url if message.author.avatar else None
                )
            except Exception as e:
                print(f"message ping failed: {e}")

@client.event
async def on_voice_state_update(member: discord.Member, before, after):
    if not config.get('voicePing'):
        return
    if member.guild.id != config['server1']:
        return
    if before.channel is not None or after.channel is None:
        return

    # Support multiple role IDs
    watched = [int(rid) for rid in config['voiceRoleServer1'] if str(rid).strip().isdigit()]

    if not any(role.id in watched for role in member.roles):
        return

    if not config.get('webhook'):
        return

    link = f"https://discord.com/channels/{member.guild.id}/{after.channel.id}"
    content = (
        f"<@&{config['voiceRole']}>\n"
        f"channel name: __**{after.channel.name}**__ - {link}"
    )

    async with aiohttp.ClientSession() as session:
        try:
            webhook = Webhook.from_url(config['webhook'], session=session)
            await webhook.send(
                content=content,
                username=member.display_name,
                avatar_url=member.avatar.url if member.avatar else None
            )
        except Exception as e:
            print(f"voice ping failed: {e}")

client.run(TOKEN)