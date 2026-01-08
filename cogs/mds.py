import discord
from discord.ext import commands
import Logs.logger as logger

class mds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):

        # ignorar mensajes de bots
        if message.author.bot:
            return

        if isinstance(message.channel, discord.DMChannel):
            # Log de mensajes directos
            logger.Logger.log(f"[DM] {message.author} -> {message.content}")
        else:
            # Log de cualquier mensaje en un servidor
            """
            logger.Logger.log(
                f"[{message.guild.name} | #{message.channel.name}] "
                f"{message.author}: {message.content}"
            )
            """

        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(mds(bot))