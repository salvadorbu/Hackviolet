import discord
from discord.ext import commands
from canvas_api import CanvasBot

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='..', intents=intents, description='A simple Discord bot')
token = 'MTA3MTQ4MTM1NjMwMDg2NTYxNg.Gj4CUK.3aErzRtaXKw9A7rAXR1-7u8AKdYZlgc2UzqENw'
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    print("message-->", message)
    if message.author == client.user:
        return
 
    if message.content.startswith('hi'):
        await message.channel.send('Hello!')
 
    if message.content.startswith('image'):
        await message.channel.send(file=discord.File('download.jpg'))

@bot.command()
async def hello(ctx):
    await ctx.send("Hello asdfsfad!")

@bot.command()
async def goodbye(ctx):
    idk()

def idk():
    url = "https://canvas.vt.edu"
    key = "4511~CSBkFbb31upwYZYNHWfENaVnF0xOdXbGPl9Kr55rDC5M4y3hr0QMx8wkvbLHQIxs"
    bot = CanvasBot(url, key)
    print(bot.get_courses())
    
@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")
    embed = discord.Embed(title='Reload', description=f'{extension} successfully reloaded', color=0xff00c8)
    await ctx.send(embed=embed)

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()
    
bot.run(token)