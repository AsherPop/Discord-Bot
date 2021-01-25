import discord
import asyncio
import random
from discord.ext.commands import Bot
from discord.ext import commands


pp = commands.Bot(command_prefix = '!')


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


@pp.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    await pp.send_message(member, newUserDMMessage)
    await pp.send_message(discord.Object(id='CHANNELID'), 'Welcome!')
    print("Sent message to " + member.name)
    print("Sent message about " + member.name + " to #CHANNEL")


@pp.event
async def on_member_remove(member):
    print("Recognised that a member called " + member.name + " left")
    await pp.send_message(discord.Object(id='CHANNELID'), member.name + ' left')
    print("Sent message to #CHANNEL")


@pp.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@pp.command()
async def ping(ctx):
    await ctx.send(f'{round(pp.latency * 1000)}ms')





pp.run('ODAxODM0MTA1ODA0ODE2Mzk0.YAmcNA.Af3aOaVlb2zz55ZZHtE9GU3IZ54')
