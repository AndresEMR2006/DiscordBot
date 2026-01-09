import discord
from discord.ext import commands
import Logs.logger as logger

adminID = 517149490139103262

class admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def shutdown(self, ctx):
        """Apaga el bot (Solo para el admin)"""
        if ctx.author.id != adminID:
            await ctx.send("No tienes permiso para usar este comando.")
            logger.Logger.log(f"| WARNING | BOT | Comando shutdown denegado | Usuario: {ctx.author.name} intento usar shutdown")
            return

        await ctx.send("Apagando el bot...")
        logger.Logger.log(f"| INFO | BOT | Comando shutdown usado | Usuario: {ctx.author.name} apago el bot")
        await self.bot.close()

    @commands.command(hidden=True)
    async def msg(self, ctx, username: str, *, message: str):
        """Envia un mensaje a la persona con el nombre de usuario dado (Solo para el admin)"""
        if ctx.author.id != adminID:
            await ctx.send("No tienes permiso para usar este comando.")
            logger.Logger.log(f"| WARNING | BOT | Comando msg denegado | Usuario: {ctx.author.name} intento usar msg")
            return

        for member in self.bot.users:
            if member.name == username:
                try:
                    await member.send(message)
                    await ctx.send(f"Mensaje enviado a {username}.")
                    logger.Logger.log(f"| INFO | BOT | Comando msg usado | Usuario: {ctx.author.name} envio un mensaje a {username}")
                except discord.Forbidden:
                    await ctx.send(f"No se pudo enviar el mensaje a {username}.")
                    logger.Logger.log(f"| WARNING | BOT | Comando msg fallo | No se pudo enviar el mensaje a {username}")
                return

        await ctx.send(f"No se encontró al usuario {username}.")
        logger.Logger.log(f"| WARNING | BOT | Comando msg fallo | No se encontró al usuario {username}")

    @commands.command(hidden=True)
    async def reiniciar(self, ctx):
        """Reinicia el bot (Solo para el admin)"""
        if ctx.author.id != adminID:
            await ctx.send("No tienes permiso para usar este comando.")
            logger.Logger.log(f"| WARNING | BOT | Comando reiniciar denegado | Usuario: {ctx.author.name} intento usar reiniciar")
            return

        await ctx.send("Reiniciando el bot...")
        logger.Logger.log(f"| INFO | BOT | Comando reiniciar usado | Usuario: {ctx.author.name} reinicio el bot")
        os.execv(sys.executable, ['python'] + sys.argv)


async def setup(bot):
    await bot.add_cog(admin(bot))