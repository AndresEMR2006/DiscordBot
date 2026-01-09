import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import Logs.logger as logger

# Intents (permisos del bot)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True

class MyBot(commands.Bot):
    async def setup_hook(self):
        bot.remove_command("help")
        await self.load_extension("cogs.general")
        await self.load_extension("cogs.ayuda")
        await self.load_extension("cogs.test")
        await self.load_extension("cogs.mds")
        await self.load_extension("cogs.admin")
        await self.load_extension("cogs.dnd")

bot = MyBot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    logger.Logger.log(f"| INFO | BOT | CONEXION |Bot conectado como {bot.user} ")
    for command in bot.commands:
        logger.Logger.log(f"| INFO | BOT | COMANDOS | Comando: {command.name}")
        
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    raise RuntimeError("No se encontró el DISCORD_TOKEN")

for c in bot.commands:
    print(c.name, c.callback.__module__)

bot.run(TOKEN)
