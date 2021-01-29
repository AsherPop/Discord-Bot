import discord
from discord.ext import commands


pp = discord.Client()
pp = commands.Bot(command_prefix = '.')


@pp.event
async def on_message(message):
    if message.content == ("hello"):
        await message.channel.send("Hello!")


@pp.event
async def on_message(message):
    if str(message.channel) == "memes" and message.conenet !="":
        await message.channel.purge(limit=1)


@pp.event
async def on_ready():
    print(f'{pp.user} has connected to discord!')


@pp.event
async def on_member_join(member):
    if not member.bot:
        await get.channel("welcome").send(f'Welcome to the server! Head over to the general channel and say hi! Make sure to follow all of our rules and do not be mean, or you might get kicked.')

   
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


@pp.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    await bot.kick(userName)
    await ctx.send(f'{member.display_name} has been booted from the server for making a bad decision!')


pp.run('ODAxODM0MTA1ODA0ODE2Mzk0.YAmcNA.p1MqjM2hFu7si7V33EDpC4T3mbc')
