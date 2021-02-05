import discord
import asyncio
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
pp = commands.Bot(command_prefix = '.', intents=intents)




#Events

@pp.event
async def on_ready():
    print(f'{pp.user} has connected to discord!')

@pp.event
async def on_member_join(member):
    if not member.bot:
        await message.send(f'Welcome to the server! Head over to the general channel and say hi!')

@pp.event
async def on_member_remove(member):
    if not member.bot:
        await message.send(f'{member.display_name} is no longer in the server!')




#Conmmands

@pp.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(pp.latency * 1000)}ms')

@pp.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit = amount)

@pp.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.display_name} has been booted from the server for making a bad decision!')

@pp.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped {}'.format(slapped, reason1))

@pp.command()
async def info(ctx, *, member: discord.Member):
    fmt = '{0} was welcomed to the server at {0.joined_at} and has {1} roles!'
    await ctx.send(fmt.format(member, len(member.roles)))

@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Im sorry I could not find any info about this member!')



pp.run('ODA3Mjg5ODkxMjYzNDc5ODI3.YB11TA.d-1o5IX4JlkQT6vZ6UfFwL-kR7w')
