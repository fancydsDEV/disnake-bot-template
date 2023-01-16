import disnake, config
from disnake.ext import commands
from pymongo import MongoClient

class readyEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cluster = MongoClient(config.mongo_uri)
        self.db = self.cluster["botdb"]
        self.collection = self.db["economy"]
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'---------------------')
        print(f'БОТ: {self.bot.user}')


def setup(bot):
    bot.add_cog(readyEvent(bot))