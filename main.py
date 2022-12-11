import discord
from discord.ext import commands
from discord import app_commands
import dotenv
import os

intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', help_command=None, intents=intents)

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
    print(f'Bot dołączył do servera {guildV}')

@client.event
async def on_command_error(ctx, error):
    await ctx.send('Błąd')

# test command
@app_commands.command(name='test')
async def app_command_test(ctx):
    await ctx.response.send_message('test przebiegł pomyślnie')

# tree syncing command
@client.command(name='treesync', aliases=['sync'])
@commands.is_owner()
async def treesync(ctx):
    try: 
        client.tree.add_command(app_command_test, override=True)
        await client.tree.sync()
    except Exception as error:
        await ctx.send(f'Błąd synchronizacji drzewka poleceń. Błąd: {error}')
    else: await ctx.send('Udało się zsynchronizować drzewko poleceń')

# running the client
dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)