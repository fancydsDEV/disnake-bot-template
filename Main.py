import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix = '.', intents = disnake.Intents.all(), help_command = None)

bot.run(config.TOKEN)
