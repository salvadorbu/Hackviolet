import discord
from discord.ext import commands
from canvas_api import CanvasBot
from cache import Cache

# The intents variable in the code you provided is a discord. 
# Intents object that is set to include all possible Discord Intents. 
# Discord Intents are essentially permissions that allow your bot to 
# perform certain actions, such as viewing or sending messages, or reading reactions.
intents = discord.Intents.all() 

# This is a convenient class that simplifies the process of creating a bot and adding commands.
# The three parameters passed to the Bot class constructor are:
# command_prefix: The string that will be used as a prefix for commands. In this example, the prefix is set to '..'.
# intents: The discord.Intents object that was previously defined. This sets the intents that the bot will request when connecting to Discord.
# description: A string that describes the bot. This is used for documentation purposes.
# bot extends discord.client
bot = commands.Bot(command_prefix='..', intents=intents, description='A simple Discord bot')

# key to discord bot
token = 'MTA3MTQ4MTM1NjMwMDg2NTYxNg.Gj4CUK.3aErzRtaXKw9A7rAXR1-7u8AKdYZlgc2UzqENw'

async def on_ready(): pass

@bot.command()
async def hello(ctx):
    await ctx.send("hello")

@bot.command()
async def schedule(ctx):
    # get user
    user = ctx.message.author
    hello(ctx)
    # get/generate cache
    # web = cache.get("website")
    # key = cache.get("value")
    # if value is None:
    # PROMPT USER FOR WEBSITE
    # PROMPT USER FOR CANVASID
    #    cache.set("website", value)
    #    cache.set("value", value2)
    
    test = CanvasBot("https://canvas.vt.edu", "19~tqCIJW5unhHMKEzWuHPlEcLcRxeKN70c2LyVnw8bEXFRY9T8FwCDHI36Ih0JrZNH")
    l = test.get_courses()
    await user.send("curr courses: \n")
    for i in l:
        await user.send(f"{i}\n")

@bot.command()
async def prompt(ctx, *, prompt: str):
    response = await ctx.send(prompt)
    def check(m):
        return m.channel == response.channel and m.author == ctx.author
    response = await bot.wait_for("message", check=check)
    await ctx.send(f"You said your favorite color is {response.content}.")

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.close()
    
bot.run(token)