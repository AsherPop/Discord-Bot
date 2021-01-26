import discord
import random
import asyncio
from discord.ext import commands


pp = commands.Bot(command_prefix = '-')


@pp.event
async def on_message(message):
    if message.content == ("hello"):
        await message.channel.send("Hello!")

	    
@pp.event
async def on_ready():
    print(f'{pp.user} has connected to discord!')


@pp.event
async def on_member_join(member):
    if not member.bot:
        await get.channel("welcome").send(f"Welcome to {member.guild.name} , {member.mention}! Head over to {get.channel('general').mention} and say hi!")

    
@pp.event
async def on_member_remove(member):
    if not member.bot:
        await get.channel("general").send(f'{member.display_name} is no longer in the server!')

        
@pp.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@pp.command()
async def ping(ctx):
    await ctx.send(f'{round(pp.latency * 1000)}ms')





pp.run('ODAxODM0MTA1ODA0ODE2Mzk0.YAmcNA.uyz1FI7FtRkeimD7_j3ApQQn_vY')
