import discord
from discord.ext import commands
from discord import app_commands
import dotenv
import os
dotenv.load_dotenv()

intents = discord.Intents.all()
OWNER_ID = os.getenv('OWNER_ID')
client = commands.Bot(command_prefix='$', help_command=None, intents=intents, owner_id=OWNER_ID)

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

@client.event
async def on_command_error(ctx, error):
    await ctx.send('error')

# test command
@app_commands.command(name='test')
async def app_command_test(ctx):
    await ctx.response.send_message('test succesful')

# tree syncing command
@client.command(name='treesync', aliases=['sync'])
@commands.is_owner()
async def treesync(ctx):
    try: 
        client.tree.add_command(app_command_test, override=True)
        await client.tree.sync()
    except Exception as error:
        await ctx.send(f'Syncing error: {error}')
    else: await ctx.send('Syncing succesful')

# running the client
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)

#test