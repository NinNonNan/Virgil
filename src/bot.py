import discord
from discord.ext import commands
from discord import app_commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    # Sincronizza i comandi slash solo nel server specificato
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f"{bot.user} è online e pronto! Comandi sincronizzati.")

@tree.command(name="ping", description="Risponde con Pong!", guild=discord.Object(id=GUILD_ID))
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong!")

bot.run(TOKEN)
