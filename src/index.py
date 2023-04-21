import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from funcionesPreguntas import pickPregunta

#from paramiko import Channel

load_dotenv()
intents = discord.Intents.all()
bot = discord.Client(intents=intents)

#bot = commands.Bot(command_prefix='>', description="This is a survey bot")


@bot.event
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
        await message.channel.send(pickPregunta())    



@bot.event
async def ping(ctx):
    channel = bot.get_channel(978319098834468864)
    await channel.send('Pong!')
    
    
bot.run(os.getenv('TOKEN_BOT'))
