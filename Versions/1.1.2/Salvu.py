import discord
from discord.ext import commands
import random
import time





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

@client.command()
async def salvurps(ctx):
    rpsGame = ['rock', 'paper', 'scissors']
    await ctx.send(f"{ctx.author.name}, I see you have challenged me to a game of rock, paper scissors. Of course, I accept.\nChoose carefully, 'rock', 'paper' or 'scissors'?")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

    user_choice = (await client.wait_for('message', check=check)).content
    winStreak = 0

    comp_choice = random.choice(rpsGame)
    if user_choice == 'rock':
        if comp_choice == 'rock':
            winSteak = winStreak
            await ctx.send(f'Ah, we drawed. Try again if you dare challenge my internet speed.\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            
            await ctx.send(f'I won! Fqajtek! I challenge you to another one. Or are you too scared?\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            
            await ctx.send(f"Uff! I lost. Good game. Want to test me again?\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'paper':
        if comp_choice == 'rock':
            
            await ctx.send(f'Uff! I lost. Good game. Want to test me again?\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            
            await ctx.send(f'Ah, we drawed. Try again if you dare challenge my internet speed.\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            
            await ctx.send(f"I won! Fqajtek! I challenge you to another one. Or are you too scared?\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            
            await ctx.send(f'I won! Fqajtek! I challenge you to another one. Or are you too scared?\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            
            await ctx.send(f'Uff! I lost. Good game. Want to test me again?\nYour choice: {user_choice}\nMy choice: {comp_choice}\n')
        elif comp_choice == 'scissors':
            
            await ctx.send(f"Ah, we drawed. Try again if you dare challenge my internet speed.\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    print("Message sent.")

@client.command()
async def salvuroast(ctx):
    roasts = {"My internet is faster than yours!", "Ur mum so fat that they had to rebuild the entire titanic to bring her to comino (it still sank).", "Error: Salvu cannot roast you because you are alreadu burnt."}
    await ctx.send((random.choice(roasts)))

@client.command()
async def salvugwsvincent(ctx):
    await ctx.send("Ħa nibatlek naqra pastizzi minn Kemmuna. Get well soon Vincent :ocean: !")
client.run("")
