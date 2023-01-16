import disnake, config
from disnake.ext import commands

class readyEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'---------------------')
        print(f'БОТ: {self.bot.user}')

def setup(bot):
    bot.add_cog(readyEvent(bot))
