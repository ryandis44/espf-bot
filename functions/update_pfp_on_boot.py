import aiohttp
import discord
import logging

from Database.tunables import tunables
from io import BytesIO
LOGGER = logging.getLogger()



async def update_pfp_on_boot(client: discord.Client):
    try:
        for guild in client.guilds:
            if guild.id == tunables('PFP_SERVER_ID'):
                
                pfp = None
                banner = None
                
                async with aiohttp.ClientSession() as ses:
                    if guild.icon:
                        async with ses.get(guild.icon.url) as r:
                            if r.status in range(200, 299):
                                img = BytesIO(await r.read())
                                pfp = img.getvalue()
                
                async with aiohttp.ClientSession() as ses:
                    if guild.banner:
                        async with ses.get(guild.banner.url) as r:
                            if r.status in range(200, 299):
                                img = BytesIO(await r.read())
                                banner = img.getvalue()
                
                await client.user.edit(
                    avatar=pfp,
                    banner=None,
                )
    except Exception as e: LOGGER.error(f"Error updating pfp on boot: {e}")