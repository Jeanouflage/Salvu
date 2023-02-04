import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Success: Bot is connected to Discord! :D")

@client.command()
async def aboutsalvu(ctx):
    await ctx.send("My name is Salvu and I own an island.")
    print("Message sent.")

@client.command()
async def salvucommands(ctx):
    await ctx.send("/aboutsalvu , /aboutsalvuNasDaily . Do you want to know what they do? Try them out and get to know Salvu.")
    print("Message sent.")

@client.command()
async def aboutsalvuNasDaily(ctx):
    await ctx.send("This is Salvu. His home is an island, where he and his two cousins live! His family moved here for a job that no longer exists, and have lived there for more than 66 years! There are many tourists that he can hang out with, but can also spend time alone, as they are all gone by 5pm! In his tiny house, he has mail, electricity, TVs and internet. His internet is faster than yours! He has recieved the highest honour in Malta because he takes care of his island. Salvu's house has everything it needs, except noise... Check out this video to learn about Salvu:  https://www.facebook.com/watch/?v=1018363788315773")
    print("Message sent.")
client.run("")

//This is the part where I put the bot token.
