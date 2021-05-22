# bot.py
import os
import discord
from discord import guild
from dotenv import load_dotenv


# Download dotenv by pip install python-dotenv
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
my_guild = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    GUILD = discord.utils.get(client.guilds, name=my_guild)
    print(
        f'({client.user} is connected to the following guild:\n'
        f'{GUILD.name}(id: {GUILD.id})'
    )

# This line shoud be in every bot to protect from the bot responding to itself
@client.event
async def on_message(message):
    if message.author == client.user:
        return

client.run(token)