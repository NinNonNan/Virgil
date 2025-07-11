import discord
from discord.ext import commands
import os
import sys

# Aggiunge il path della directory corrente per trovare config.py
sys.path.append(os.path.dirname(__file__))

from config import TOKEN

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Carica i cogs all'avvio
@bot.event
async def on_ready():
    try:
        await bot.tree.sync()  # sync globale
        print(f"{bot.user} è online e comandi sincronizzati globalmente.")
    except Exception as e:
        print(f"Errore nella sincronizzazione dei comandi: {e}")

    print("Caricamento cogs...")
    await bot.load_extension("cogs.ping")
    print("Cogs caricati.")

bot.run(TOKEN)
