import discord
import os
from discord.ext import commands
from discord import app_commands
from discord import tree
from dotenv import load_dotenv
from funcionesPreguntas import pickPregunta

#from paramiko import Channel

load_dotenv()
intents = discord.Intents.all()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

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

@tree.command(name = "commandname", description = "My first application Command") #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message("Hello!")
    
         
        
"""     channel_target = bot.get_channel(978319098834468864)
        members = bot.get_all_members() 
        #members = channel_target.members
        membersID = [] 
        for member in members:
            membersID.append(member.id)
        print(membersID)   """
            
    
bot.run(os.getenv('TOKEN_BOT'))

