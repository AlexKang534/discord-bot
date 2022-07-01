from ctypes.wintypes import MSG
from socket import MsgFlag
import discord


client = discord.Client()

arkDictionary = ["lostark", "lost ark", "ark"]


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    msg = message.content

    if message.content.startswith('$hello'):
        await message.channel.send('Sup!')

    if any(word in msg for word in arkDictionary):
        await message.channel.send('Game is dead')

client.run("OTkyMzk0MzU5NTExMjA3OTg3.GFNqcX.8sUUM52iIhLwTJQBY_LC6h-GlYpmacFmkoaKUA")
