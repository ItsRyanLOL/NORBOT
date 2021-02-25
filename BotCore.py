import discord
from discord.ext import commands
import requests

# Logger Setup
import logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# End Logger Setup

from BotToken import botToken, steamIDkey


bot = commands.Bot(command_prefix='!')


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    elif message.content.startswith('!lookup'):
        #Look up steam profile on steamid.uk
        response = requests.get("https://steamidapi.uk/request.php?api=" + steamIDkey + "&player=76561197973745007&request_type=1&format=json")

        if (response.status_code == 200):
            await message.channel.send('```json\n' + response.text + '```')

@client.event
async def on_member_remove(member):
    # Ban member when they leave the discord
    print('Banning'+member)

client.run(botToken)