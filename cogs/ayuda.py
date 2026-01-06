import discord
from discord.ext import commands

class ayuda(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["a" , "help", "h"])
    async def ayuda(self, ctx, comando=None):
        """Muestra informacino importante de todos los comandos"""
        embed = discord.Embed(
            title="",
            description=""
        )
        if comando is None:
            embed.title = "Comandos"
            for comando_ in self.bot.commands:
                embed.description+= (comando_.name + "\n")
        else:

            cmd = self.bot.all_commands.get(comando)
            if cmd is not None:
                embed.title = "¿Como usarlo?"
                embed.description = ("Uso: !" + cmd.name)
                embed.description += (" " + cmd.signature)
                embed.description += ("\n Info adicional: " + cmd.help)
                if cmd.aliases:
                    embed.description += ("\n Alias del comando:  ")
                    for alias in cmd.aliases:
                        embed.description += ( alias + "  ")
                        
            else:
                embed.title = "Typo? o estupidez? ¬¬"
                embed.description = "El comando no existe bro"

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ayuda(bot))