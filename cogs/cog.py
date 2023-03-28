import discord
from discord import app_commands
from discord.ext import commands

# Main cog class
class Cog(commands.Cog):
    def __init__(self, client):
        self.client = client

    # --cog stuff here--
    # For every command in a cog, there must be the 'self' parameter at the start. Otherwise the command will not work

    #simple ping command. Notice how the decorator is now @commands.command instead of @client.command
    @commands.command(name = "ping", aliases=["p"])
    async def  ping(self, ctx):
        #send the bot's curremt latency multiplied by 1000 and rounded. The resulting latency will be shown in miliseconds
        await ctx.send(f"Pong! bot's latency: {round(self.client.latency * 1000)}ms")

    #This decorator makes an application command (A slash command)
    @app_commands.command(name='app_ping', description='ping the bot!')
    async def app_ping(self, interaction):
        #Here we don't use refer to the context as ctx, we refer to it as interaction
        await interaction.response.send_message(f"Pong! bot's latency: {round(self.client.latency * 1000)}ms")
        #notice how we use different functions for interactions and for prefix commands, pay attention to this stuff: It gets mixed up easily
        

# setup function (cog won't load without this)
async def setup(client):
    await client.add_cog(Cog(client))
    print('Cog setup succesful')

    