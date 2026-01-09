import discord
from discord.ext import commands
from embeds.info import info_embed
import Logs.logger as logger

class general(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print("Cog General cargado")

    @commands.command()
    async def pene(self, ctx):
        """Drohn se la queria comer"""
        await ctx.send(f"{ctx.author.mention} bitch")
        logger.Logger.log(f"| INFO | BOT | Comando pene usado | Usuario: {ctx.author.name}")

    @commands.command()
    async def info(self, ctx):
        print("INFO EJECUTADO")
        """Muestra informacion sobre el bot"""
        await ctx.send(embed = info_embed())
        logger.Logger.log(f"| INFO | BOT | Comando info usado | Usuario: {ctx.author.name}")

    # Listeners

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
                logger.Logger.log(f"| INFO | BOT | DM enviado | Se le envio un DM a {m.name} para jugar con {member.name}")
            except discord.Forbidden: # DM's cerrados :P
                logger.Logger.log(f"| INFO | BOT | DM fallido | No se le pudo enviar un DM a {m.name}")
                pass

async def setup(bot):
    await bot.add_cog(general(bot))