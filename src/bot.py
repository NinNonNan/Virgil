import discord
from discord.ext import commands
import os
import sys

sys.path.append(os.path.dirname(__file__))

from config import TOKEN

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Sincronizza i comandi al ready
@bot.event
async def on_ready():
    try:
        await bot.tree.sync()  # sync globale o per guild specifica se vuoi
        print(f"{bot.user} è online e comandi sincronizzati globalmente.")
    except Exception as e:
        print(f"Errore nella sincronizzazione dei comandi: {e}")

# Caricamento cog prima di bot.run()
async def load_extensions():
    await bot.load_extension("cogs.ping")
    print("Cog 'ping' caricato.")

import asyncio
asyncio.run(load_extensions())

bot.run(TOKEN)
