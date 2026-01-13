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

            if self.bot.redireccionamiento:
                admin = await self.bot.fetch_user(adminID)
                await admin.send(f"Autor: {message.author.name}\nMensaje: {message.content}")
                logger.Logger.log(f"[DM | REDIRECCIONADO | {message.author.name} -> {message.content}]")
            else:
                logger.Logger.log(f"[DM] | {message.author.name} -> {message.content}")

            usuario = [message.author.name, user_id]
            logger.Logger.guardar_md_users(usuario)

async def setup(bot):
    await bot.add_cog(mds(bot))
