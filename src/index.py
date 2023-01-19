from click import pass_context
import discord
from discord.ext import commands
from paramiko import Channel

bot = commands.Bot(command_prefix='>', description="This is a survey bot")

@bot.command()
async def ping(ctx):
    await ctx.sent('pong ')

#Events   
@bot.event 
async def on_ready():
    print('Bender is ready')

@bot.event
async def on_message(message):
    id = bot.get_guild(978319098834468864)
    if message.content.find("hello") != -1:
        await message.channel.send("Hi, stranger, What's your favorite food?")    

bot.run('OTc4MTgwOTg3NTgwMTkwNzIw.GxWpNh.wnEbMopPcQ5KoszK-82ZjOv5LRwDThm9sxOcjc')




@bot.command(pass_context=True)
async def ping(ctx):
    channel = bot.get_channel(978319098834468864)
    await channel.send('Pong!')