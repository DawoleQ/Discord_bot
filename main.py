import discord #main discord module
from discord.ext import commands #command module
from discord import app_commands #app commands module
import dotenv #module for .env file
import datetime #module for getting the time
import os 
dotenv.load_dotenv() #load the .env file

# Initialize bot
intents = discord.Intents.all() #intent are essential to run the bot since discord.py rewrite
OWNER_ID = os.getenv('OWNER_ID') #setting the owner ID
client = commands.Bot(command_prefix='$', owner_id=OWNER_ID, intents=intents) #creating the bot user

#The on_ready() event is executed when bot initialization (the thing above this) is done
@client.event
async def on_ready():
    # Load extensions
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await client.load_extension(f'cogs.{filename[:-3]}')
            except Exception as error:
                print(error)
            else:
                print(f'loaded {filename}')
    print('Bot online')

@client.event
async def on_guild_join(guild):
    guildId = guild.id
    guildV = client.get_guild(guildId)
    print(f'Bot joined a server named {guildV}')

# Error handler (will just display the error for naw)
@client.event
async def on_command_error(ctx, error):
    await ctx.send(error)

# test command
@app_commands.command(name='test')
async def app_command_test(ctx):
    await ctx.response.send_message('test succesful')

# tree syncing command (this is used to sync changes or add new app commands as they are stored and processed by discord itself, not by the bot)
@client.command(name='treesync', aliases=['sync'])
@commands.is_owner()
async def treesync(ctx):
    try: 
        await client.tree.sync()
    except Exception as error:
        await ctx.send(f'Syncing error: {error}')
    else: await ctx.send('Syncing succesful')

#This commands will run every time a command is run
@client.event
async def on_command(ctx):
    #ctx is the context of the current command
    user = ctx.author
    command = ctx.command
    date = datetime.now()
    # this gets the current date in a specified format
    time = date.strftime(r"%I:%M %p")
    print(f'{user} used {command} at: {time}')

# running the client
TOKEN = os.getenv('TOKEN') #this function gets the TOKEN from the .env file we opened at the very top of this code (line 6)
client.run(TOKEN) #this initializes the bot and must ALWAYS be at the very end of our main bot file