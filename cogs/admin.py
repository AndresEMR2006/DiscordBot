import discord
from discord.ext import commands
import Logs.logger as logger
import os
import sys

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
    async def msg(self, ctx: commands.Context, username: str, *, message: str):
        """Envia un mensaje a la persona con el nombre de usuario dado (Solo para el admin)"""
        if(ctx.author.id != adminID):
            await ctx.send("No tienes permiso para usar este comando.")
            logger.Logger.log(f"| WARNING | BOT | Comando msg denegado | Usuario: {ctx.author.name} intento usar msg")
            return
        
        usuarios = logger.Logger.cargar_md_users()
        usuario_id_string = usuarios.get(username)

        if usuario_id_string == None:
            await ctx.send("No hay almacenado ningun usuario con ese nombre")
            logger.Logger.log(f"| WARNING | BOT | Comando msg denegado | El usuario al que se le queria escribir no esta almacenado")
            return

        usuario_id = int(usuario_id_string)
        usuario = await self.bot.fetch_user(usuario_id)
        
        try:
            await usuario.send(message)
            logger.Logger.log(f"| INFO | BOT | DM enviado | Se le envio el DM {message} a {usuario.name}")
        except discord.Forbidden: # DM's cerrados :P
            logger.Logger.log(f"| INFO | BOT | DM fallido | No se le pudo enviar un DM a {usuario.name}")
            pass

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

    @commands.command(hidden=True)
    async def mds(self, ctx):
        diccionario = logger.Logger.cargar_md_users()
        for usuario in diccionario:
            await ctx.send(usuario)

        logger.Logger.log(f"| INFO | BOT | Comando mds usado | Usuario: {ctx.author.name} quizo ver los usuarios registrados")

    @commands.command(hidden=True)
    async def redireccionamiento(self, ctx):

        if ctx.author.id != adminID:
            await ctx.send("No tienes permiso para usar este comando.")
            logger.Logger.log(f"| WARNING | BOT | Comando redireccionamiento denegado | Usuario: {ctx.author.name} intento activar o desactivar redireccionamiento")
            return

        self.bot.redireccionamiento = not self.bot.redireccionamiento
        await ctx.send(f"El redireccinamiento quedo en {self.bot.redireccionamiento}")
        logger.Logger.log(f"| INFO | BOT | GLOBAL-VARIABLE | se ha cambiado el redireccionamiento a {self.bot.redireccionamiento}")

async def setup(bot):
    await bot.add_cog(admin(bot))