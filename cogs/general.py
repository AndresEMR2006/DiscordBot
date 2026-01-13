import discord
from discord.ext import commands
from embeds.info import info_embed
import Logs.logger as logger

# variable para los logs
MODULO = "GENERAL"

class general(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        print("INFO EJECUTADO")
        """Muestra informacion sobre el bot"""
        await ctx.send(embed = info_embed())
        logger.Logger.log(logger.NivelLog.INFO, MODULO, "Comando info usado", ctx.author.name)

    # Listeners
    # Este comando funciona unicamente localmente, es un comando para un servidor en especifico
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        canal_texto = self.bot.get_channel(812372867873243155)
        canal_voz = after.channel

        if canal_voz is None or before.channel is not None:
            return

        if canal_texto is None: # validacion de id en el canal
            return

        if len(canal_voz.members) != 1:
            return

        for m in canal_texto.members:

            if m.bot:
                continue

            if m in canal_voz.members:
                continue

            try:
                await m.send("Quieres jugar? :3")
                logger.Logger.log(logger.NivelLog.INFO, MODULO, f"Se le envio un DM a {m.name} para jugar con {member.name}", None)
            except discord.Forbidden: # DM's cerrados :P
                logger.Logger.log(logger.NivelLog.ERROR, MODULO, f"Se le intento enviar un DM a {m.name} pero este tiene los DM cerrados", None)
                pass

async def setup(bot):
    await bot.add_cog(general(bot))