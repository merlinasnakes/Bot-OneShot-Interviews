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


#Events   
@bot.event 
async def on_ready():
    print('Bender is ready')

@bot.event
async def on_message(message):
    id = bot.get_guild(978319098834468864)
    if message.content.find("hello") != -1:
        await message.channel.send(pickPregunta())
    
    if message.content.find("miembros") != -1:
        guild = message.channel.guild
        print(guild)
        lista_miembros = []
        for member in guild.members:
            lista_miembros.append(member)                
        await message.channel.send(f"{lista_miembros[1].mention} - {pickPregunta()}")    
        
"""     channel_target = bot.get_channel(978319098834468864)
        members = bot.get_all_members() 
        #members = channel_target.members
        membersID = [] 
        for member in members:
            membersID.append(member.id)
        print(membersID)   """
            
    
bot.run(os.getenv('TOKEN_BOT'))

