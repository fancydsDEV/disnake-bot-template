import disnake, os
from disnake.ext import commands

bot = commands.Bot(command_prefix = '.', intents = disnake.Intents.all(), help_command = None)

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):                        
        bot.load_extension(f'commands.{filename[:-3]}')
        print(f'Команда: {filename[:-3]} загружена.')

for filename in os.listdir('./events'):
    if filename.endswith('.py'):
        bot.load_extension(f'events.{filename[:-3]}')
        print(f'Ивент: {filename[:-3]} загружен.')

bot.run(config.TOKEN)
