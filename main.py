from dotenv import load_dotenv
load_dotenv()
import os

import discord
# from discord.ext import commands
from discord.ext.commands import Bot

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print("The bot is ready")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        print(message.author, message.content)
        #await message.channel.send("hello")
        await message.reply("hello")

client.run(os.getenv("TOKEN"))