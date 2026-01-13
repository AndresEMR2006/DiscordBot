import discord
from discord.ext import commands
from discord import app_commands
import random
import re
import DnD.Tiradas as tiradas

tipos = {4, 6, 8, 10, 12, 20, 100}

def segmentar(dado: str):
        # funcion para segmentar el string del dado
        patron = r'(\d*)d(\d+)([+-]\d+)?'
        coincidencia = re.match(patron, dado)
        if coincidencia:
            num_dados = int(coincidencia.group(1)) if coincidencia.group(1) else 1
            tipo_dado = int(coincidencia.group(2))
            modificador = int(coincidencia.group(3)) if coincidencia.group(3) else 0
            return num_dados, tipo_dado, modificador
        else:
            return None

class DnDCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, dado: str):
        """Comando para lanzar un dado"""

        tirador = tiradas.tiradas()
        resultado = tirador.roll(dado)

        if not (resultado.get("estado")): 
            await ctx.send(resultado.get("error"))
            return
        
        for i, tirada in enumerate(resultado["tiradas"]):
            if i in resultado["posNat20"]:
                await ctx.send("¡Damm! salió un nat 20 🎉")
            else:
                await ctx.send(f"Resultado del tiro: {tirada}")
            


async def setup(bot: commands.Bot):
    await bot.add_cog(DnDCog(bot))
        
            

        