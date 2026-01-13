import discord
from discord.ext import commands
import Logs.logger as logger
import os
import sys

adminID = 517149490139103262
MODULO = "ADMIN"

class admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        """Apaga el bot """
        await ctx.send("Apagando el bot...")
        logger.Logger.log(logger.NivelLog.INFO, MODULO, "Comando shutdown usado", ctx.author.name)
        await self.bot.close()

    @commands.command(hidden=True)
    @commands.is_owner()
    async def msg(self, ctx: commands.Context, username: str, *, message: str):
        """Envia un mensaje a la persona con el nombre de usuario dado """
        
        usuarios = logger.Logger.cargar_md_users()
        usuario_id_string = usuarios.get(username)

        if usuario_id_string == None:
            await ctx.send("No hay almacenado ningun usuario con ese nombre")
            logger.Logger.log(logger.NivelLog.WARNING, MODULO, "Comando msg denegado - USUARIO NO ALMACENADO", None)
            return

        usuario_id = int(usuario_id_string)
        usuario = await self.bot.fetch_user(usuario_id)
        
        try:
            await usuario.send(message)
            logger.Logger.log(logger.NivelLog.INFO, MODULO, f"DM enviado a {usuario.name}", None)

        except discord.Forbidden: # DM's cerrados :P
            logger.Logger.log(logger.NivelLog.ERROR, MODULO, f"Se le intento enviar un DM a {usuario.name} pero este tiene los DM cerrados", None)
            pass

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reiniciar(self, ctx):
        """Reinicia el bot"""

        await ctx.send("Reiniciando el bot...")
        logger.Logger.log(logger.NivelLog.INFO, MODULO, "Comando reiniciar usado", ctx.author.name)
        os.execv(sys.executable, ['python'] + sys.argv)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def mds(self, ctx):
        diccionario = logger.Logger.cargar_md_users()
        for usuario in diccionario:
            await ctx.send(usuario)

        logger.Logger.log(logger.NivelLog.INFO, MODULO, "Comando mds usado", ctx.author.name)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def redireccionamiento(self, ctx):
        self.bot.redireccionamiento = not self.bot.redireccionamiento
        await ctx.send(f"El redireccinamiento quedo en {self.bot.redireccionamiento}")
        logger.Logger.log(logger.NivelLog.INFO, MODULO, f"se ha cambiado el redireccionamiento a {self.bot.redireccionamiento}", None)

async def setup(bot):
    await bot.add_cog(admin(bot))