import discord
from discord.ext import commands
from config import TOKEN
import asyncio
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    try:
        await bot.tree.sync()
        print(f"{bot.user} è online e comandi sincronizzati globalmente.")
    except Exception as e:
        print(f"Errore nella sincronizzazione dei comandi: {e}")

async def load_extensions():
    for filename in os.listdir("./src/cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    await load_extensions()
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
