import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
pp = commands.Bot(command_prefix = '.', intents=intents)



#Events

@pp.event
async def on_ready():
    print(f'{pp.user} has connected to discord!')


@pp.event
async def on_message(message):
    if str(message.channel) == "memes" and message.content !="":
        await message.channel.purge(limit=1)



#Commands

@pp.command()
async def ping(ctx):
    await ctx.send(f'{round(pp.latency * 1000)}ms')


@pp.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit = amount)



pp.run('ODA2OTk0MTYwMjkxNjc2MTYw.YBxh4Q.i-GZ_2OrFk7aGTioPzJZJ6evyPM')
