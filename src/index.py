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
    channel_target = bot.get_guild(978319098834468864)
    await channel_target.send('Pong!')
    
@bot.event    
async def get_membersChannel():
    channel_target = bot.get_guild(978319098834468864)
    #members = channel_target.get_all_members() 
    members = channel_target.members
    membersID = [] 
    for member in members:
        membersID.append(member.id)
    print(membersID)  
            
get_membersChannel()
    
bot.run(os.getenv('TOKEN_BOT'))

