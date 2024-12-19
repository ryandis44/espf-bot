'''
Legacy Text Command

Testing only
'''

from discord.ext import commands
from discord.ext.commands import Context

class Tester(commands.Cog):
    def __init__(self, client: commands.Bot): self.client = client

    # Generates a random number between 0 and 100 [inclusive]
    @commands.command(name='test', aliases=['t'])
    async def roll(self, ctx: Context):
        
        await ctx.send(
            content=f"{ctx.guild.icon.url}"
        )

async def setup(client: commands.Bot):
    await client.add_cog(Tester(client))