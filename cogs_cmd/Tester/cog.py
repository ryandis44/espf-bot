'''
Legacy text command migrated to application command

Testing only
'''



import discord
import logging
import os

from discord.ext import commands
from discord import app_commands
LOGGER = logging.getLogger()



class TesterCog(commands.Cog):
    def __init__(self, client):
        self.client: discord.Client = client
        
        
        
    group = app_commands.Group(name="test", description="Poll Commands")



    @group.command(name="command", description=f"{os.getenv('APP_CMD_PREFIX')}Test command")
    @app_commands.guild_only
    async def test(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            content=f"{interaction.guild.icon.url}"
        )



async def setup(client: commands.Bot):
    await client.add_cog(TesterCog(client))