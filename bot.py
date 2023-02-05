import discord
from discord.ext import commands
from canvas_api import CanvasBot
from cache import Cache
import os

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
# TOKEN = os.environ.get("BOT_TOKEN")
TOKEN = "MTA3MTQ4MTM1NjMwMDg2NTYxNg.GZO_qJ.axEsTL3AVx4btGXBa0TwWJa2Ip-ElEwY34E198"
if not TOKEN:
    raise ValueError("Please set the environment variable BOT_TOKEN.")

@bot.command()
async def hello(ctx):
    await ctx.send("hello")

@bot.command()
async def schedule(ctx):
    # get user
    user = ctx.message.author
    
    # PROMPT USER FOR WEBSITE
    await user.send("What is your school's canvas website?")
    response = await bot.wait_for("message", check=lambda message: message.author == user)
    web = response.content
    # PROMPT USER FOR CANVASID
    await user.send("What is your canvas api key?")
    response = await bot.wait_for("message", check=lambda message: message.author == user)
    key = response.content
    test = CanvasBot(web, key)
    # test = CanvasBot("https://canvas.vt.edu", "4511~CSBkFbb31upwYZYNHWfENaVnF0xOdXbGPl9Kr55rDC5M4y3hr0QMx8wkvbLHQIxs")
    l = test.get_courses()
    await user.send("curr courses: \n")
    for i in l:
        string = ""
        for j in range(len(i)):
            string += i[j] + " "
        await user.send(f"{string}\n")

@bot.command()
async def submit(ctx):
    # get user
    user = ctx.message.author
    
    # PROMPT USER FOR WEBSITE
    await user.send("What is your school's canvas website?")
    response = await bot.wait_for("message", check=lambda message: message.author == user)
    web = response.content
    # PROMPT USER FOR API KEY
    await user.send("What is your canvas api key?")
    response = await bot.wait_for("message", check=lambda message: message.author == user)
    key = response.content
    test = CanvasBot(web, key)
    
    # PROMPT USER FOR COURSEID
    await user.send("What is your course id")
    response = await bot.wait_for("message", check=lambda message: message.author == user)
    cid = response.content
    
    # PROMPT USER FOR CANVASID
    await user.send("What is your assignment id?")
    aid = await bot.wait_for("message", check=lambda message: message.author == user)
    
    # PROMPT USER FOR CANVASID
    await user.send("Please upload a file:")
    response = await bot.wait_for("message", check=lambda message: message.author == user and message.attachments)
    attachment = response.attachments[0]
    await user.send(f"Thank you for uploading {attachment}!")
    
    test.submit_assignment(int(cid), int(aid), str(attachment))
    

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.close()
    
bot.run(TOKEN)