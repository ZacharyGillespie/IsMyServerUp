# bot.py
import os
import random

import mcstatus
from mcstatus import JavaServer

import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
   
@client.event   
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '!server':
        try:
            server = JavaServer.lookup("69.14.37.251:25565")
            status = server.status()
            if status.latency < 300:
                response = 'Server is up!'
                await message.channel.send(response)
        except:
            response = 'Server is down!'
            await message.channel.send(response)

client.run(TOKEN)