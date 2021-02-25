import discord
import aiohttp
import asyncio
from discord.ext import commands
#import BotCommands

# Logger Setup
import logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# End Logger Setup

from BotToken import botToken, steamIDkey


intents = discord.Intents.default()
intents.members = True


client = commands.Bot(command_prefix='!', intents = intents)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_member_remove(member):
    # Ban member when they leave the discord
    print('Banning'+member)

@client.command()
async def lookup(ctx, arg):
    #Looks up the passed steam64 ID on steamID.uk
    await ctx.send('Looking up: ' + arg)
    async with aiohttp.ClientSession() as session:
        async with session.get('https://steamidapi.uk/request.php?api=' + steamIDkey + '&player=' + arg + '&request_type=1&format=json') as response:
            await ctx.send("Status:" + str(response.status))
            await ctx.send("Content-type:" + str(response.headers['content-type']))
            html = await response.text()
            await ctx.send(html)

@client.command()
async def connected(ctx, arg: discord.member):
    #Show account connections
    await ctx.send(arg)
    await ctx.send(arg.connected_accounts)

@client.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.display_name} joined in {0.joined_at}'.format(member))



client.run(botToken)