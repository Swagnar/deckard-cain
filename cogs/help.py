import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help cog is loaded')

    # overwritten default help command for better text formatting
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            color = discord.Color.red()
        )
        embed.set_author(name='Możliwe komendy')
        embed.add_field(name='!map @lokacja', value='• Wyświetla mapę danego obszaru (cmentarz, knieja, bagno, morze, biblioteka, góra, tundra)', inline=False)
        embed.add_field(name='!vote @treść @czas_trwania', value='• Tworzy ankietę do głosowania z licznikiem ile ma trwać (podawane w minutach, max 15)', inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))