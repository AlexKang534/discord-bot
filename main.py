import discord
import os
from dotenv import load_dotenv
load_dotenv()


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

client.run(os.getenv('ARKTOKEN'))
