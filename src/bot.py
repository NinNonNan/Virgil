import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    try:
        await bot.tree.sync()  # Sync globale senza guild specifico
        print(f"{bot.user} è online e comandi sincronizzati globalmente.")
    except Exception as e:
        print(f"Errore nella sincronizzazione dei comandi: {e}")

@bot.tree.command(name="ping", description="Risponde con Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!")

bot.run(TOKEN)
