from discord.ext import commands
import discord

class test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def prueba(self, ctx):
        """Comando para realizar pruebas de aprendizaje y debugging"""
        embed = discord.Embed(
            title="Prueba :P",
            description="Prueba numero 2"
        )
        await ctx.send(embed=embed)     
        
async def setup(bot):
    await bot.add_cog(test(bot))