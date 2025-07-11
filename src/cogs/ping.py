from discord import app_commands, Interaction
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Risponde con Pong!")
    async def ping(self, interaction: Interaction):
        await interaction.response.send_message("🏓 Pong!")

async def setup(bot):
    bot.add_cog(Ping(bot))
