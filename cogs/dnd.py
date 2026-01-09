import discord
from discord.ext import commands
from discord import app_commands
import random
import re

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

        if not ("d" in dado):
            await ctx.send("Formato inválido. Usa NdM, donde N es el número de dados y M el número de caras.")
            return

        partes = segmentar(dado)

        if partes is None:
            await ctx.send("Formato inválido. Usa NdM, donde N es el número de dados y M el número de caras.")
            return

        if not (partes[1] in tipos):
            await ctx.send(f"Tipo de dado inválido. Los tipos permitidos son: {', '.join(map(str, tipos))}.")
            return

        for dados in range(int(partes[0])):
            rng = random.randint(1, int(partes[1]))
            if partes[1] == 20 and rng == 20:
                await ctx.send(f"¡Damm! salio un {partes[1]} natural :o")
            else:
                if partes[2] != 0:
                    await ctx.send(f"Ha caido un {rng} + {partes[2]}:P")
                else:
                    await ctx.send(f"Ha caido un {rng} :P")


async def setup(bot: commands.Bot):
    await bot.add_cog(DnDCog(bot))
        
            

        