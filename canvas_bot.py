import discord
from discord.ext import commands
from canvas_api import CanvasBot

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
TOKEN = "MTA3MTY2ODM4NzYxNDMxMDQ4MQ.GX6xkg.UV8CExFCNnLK_K_Au7kAbPWjXXU9IcOv3syRHQ"
if not TOKEN:
    raise ValueError("Please set the environment variable BOT_TOKEN.")

@bot.command()
async def hello(ctx):
    await ctx.send("hello")

asgn_list = None

@bot.command()
async def assignments(ctx):
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

    asgn_list = test.get_assignements()

    await user.send("Pending assignments: \n")
    assignment_index = 0
    #assignment name, due date, url, course id, assignment id
    for assignment in asgn_list:
        await user.send(f"[{assignment_index + 1}] {assignment[0]} due on {assignment[1]} | {assignment[2]}\n")
        assignment_index += 1
    


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
    await user.send("What was your assignment number? (check this by running ..assignments)")
    response = await bot.wait_for("message", check=lambda message: message.author == user)
    assignment_index = int(response.content)

    asgn_list = test.get_assignements()
    
    cid = asgn_list[assignment_index][3]
    aid = asgn_list[assignment_index][4]

    await user.send(f"{asgn_list[assignment_index][0]} chosen!")
    # PROMPT USER FOR CANVASID
    await user.send("Please upload a file:")
    response = await bot.wait_for("message", check=lambda message: message.author == user and message.attachments)
    attachment = response.attachments[0]
    file = await attachment.to_file(use_cached=False)
    print(file.filename)
    await user.send(f"Upload sent!")

    with open(file.filename, "wb") as f:
        f.write(file.fp.getbuffer())
    submission_file = open(file.filename, "rb")
    test.submit_assignment(int(cid), int(aid), submission_file)
    

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.close()
    
bot.run(TOKEN)
