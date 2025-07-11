from discord.ext import commands
from discord import app_commands, Interaction

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Risponde con Pong!")
    async def ping(self, interaction: Interaction):
        await interaction.response.send_message("🏓 Pong!")

async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))
