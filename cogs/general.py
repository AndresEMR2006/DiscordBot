import discord
from discord.ext import commands
from embeds.info import info_embed

class general(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pene(self, ctx):
        """Drohn se la queria comer"""
        await ctx.send(f"{ctx.author.mention} bitch")

    @commands.command()
    async def info(self, ctx):
        """Muestra informacion sobre el bot"""
        await ctx.send(embed = info_embed())

    # Listeners

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        print("Hubo una conexion a voz")
        
        canal_texto = self.bot.get_channel(812372867873243155)
        canal_voz = after.channel

        if canal_voz is None or before.channel is not None:
            print("No es una conexion nueva")
            return

        if canal_texto is None: # validacion de id en el canal
            print("Problema en el canal de texto")
            return

        if len(canal_voz.members) != 1:
            print("No es el primer usuario en el canal de voz")
            return

        print("Enviando mensajes DMs")
        for m in canal_texto.members:
            print(f"Revisando a {m.name}")

            if m.bot:
                print("Es un bot, no le envio mensaje")
                continue

            if m in canal_voz.members:
                print("Ya esta en el canal de voz, no le envio mensaje")
                continue

            try:
                print(f"Enviando mensaje a {m.name}")
                await m.send("Quieres jugar? :3")
            except discord.Forbidden: # DM's cerrados :P
                pass

async def setup(bot):
    await bot.add_cog(general(bot))