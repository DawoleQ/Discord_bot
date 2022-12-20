import discord
from discord import app_commands
from discord.ext import commands

# Main cog class
class Cog(commands.Cog):
    def __init__(self, client):
        self.client = client

    # --cog stuff here--

# setup function (cog won't load without this)
async def setup(client):
    await client.add_cog(Cog(client))
    print('Cog setup succesful')

    