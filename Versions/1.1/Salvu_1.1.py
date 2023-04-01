import discord
from discord.ext import commands
import random
import json

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

async def getWinstreak(users, user):
    return users[f'{user.id}']['winstreak']

async def addWinstreak(users, user):
    users[f'{user.id}']['winstreak'] += 1

async def removeWinstreak(users, user):
    users[f'{user.id}']['winstreak'] = 0

async def updateData(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['winstreak'] = 0

@client.command()
async def salvurps(ctx):
    rpsGame = ['rock', 'paper', 'scissors']
    await ctx.send(f"<@{ctx.author.id}>, I see you have challenged me to a game of rock, paper scissors. Of course, I accept.\nChoose carefully, 'rock', 'paper' or 'scissors'?")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame
    
    with open('users.json','r') as f:
        users = json.load(f)

    if not ctx.author.id in users:
        await updateData(users, ctx.author)

    playerWon = False

    user_choice = (await client.wait_for('message', check=check)).content
    
    comp_choice = random.choice(rpsGame)
    if user_choice == 'rock':
        if comp_choice == 'rock':
            playerWon = None
        elif comp_choice == 'paper':
            playerWon = False
            await removeWinstreak(users, ctx.author)
        elif comp_choice == 'scissors':
            playerWon = True
            await addWinstreak(users, ctx.author)

    elif user_choice == 'paper':
        if comp_choice == 'rock':
            playerWon = True
            await addWinstreak(users, ctx.author)
        elif comp_choice == 'paper':
            playerWon = None
        elif comp_choice == 'scissors':
            playerWon = False
            await removeWinstreak(users, ctx.author)

    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            playerWon = False
            await removeWinstreak(users, ctx.author)
        elif comp_choice == 'paper':
            playerWon = True
            await addWinstreak(users, ctx.author)
        elif comp_choice == 'scissors':
            playerWon = None

    with open('users.json','w') as f:
        json.dump(users, f)

    winStreakString = f"\nWinstreak: {await getWinstreak(users, ctx.author)}"

    if playerWon == None:
        print("Player drawed.")
        await ctx.send(f'Ah, we drawed. Try again if you dare challenge my internet speed.\nYour choice: {user_choice}\nMy choice: {comp_choice}{winStreakString}')
    if playerWon == False:
        print("Player lost.")
        await ctx.send(f"I won! Fqajtek! I challenge you to another one. Or are you too scared?\nYour choice: {user_choice}\nMy choice: {comp_choice}{winStreakString}")
    if playerWon == True:
        print("Player won.")
        await ctx.send(f'Uff! I lost. Good game. Want to test me again?\nYour choice: {user_choice}\nMy choice: {comp_choice}{winStreakString}')

    print("Message sent.")

@client.command()
async def salvuroast(ctx):
    roasts = [
        "My internet is faster than yours!",
        "Ur mum so fat that they had to rebuild the entire titanic to bring her to Comino (it still sank).",
        "Error: Salvu cannot roast you because you are already burnt."
    ]
    await ctx.send(random.choice(roasts))
client.run("MTA2NzUyNjA2NDM1Nzc4MTU0NQ.G8Y-mP.7oeoHWVfS0g3SC4rbiqcDJ5lBQHJrHTEsFeFfo")
