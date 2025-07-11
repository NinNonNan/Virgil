import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} è online!")

@bot.slash_command(guild_ids=[GUILD_ID], description="Risponde con Pong!")
async def ping(ctx):
    await ctx.respond("Pong!")

bot.run(TOKEN)
