import disnake, config, random
from disnake.ext import commands

class helloCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(
        name = 'hello'
    )
    async def hello_command(self, interaction):
        hello_words = ['Привет', 'Здравствуйте', 'Добро пожаловать']
        await interaction.response.send_message(f'{random.choice(hello_words)}, {interaction.author.mention}')

def setup(bot):
    bot.add_cog(helloCommand(bot))