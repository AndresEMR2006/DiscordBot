import discord
from discord.ext import commands
import Logs.logger as logger

adminID = 517149490139103262

class mds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        # cargar usuarios MD guardados
        self.md_users = logger.Logger.cargar_md_users()

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        if isinstance(message.channel, discord.DMChannel):
            user_id = str(message.author.id)

            logger.Logger.log(f"[DM] {message.author} -> {message.content}")

            self.md_users[user_id] = {
                "name": message.author.name,
                "last_message": message.content
            }

            logger.Logger.guardar_md_users(self.md_users)

async def setup(bot):
    await bot.add_cog(mds(bot))
