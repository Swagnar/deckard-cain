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
        embed.add_field(
            name='!map @lokacja', 
            value='• Wyświetla mapę danego obszaru **(cmentarz, knieja, bagno, morze, biblioteka, góra, tundra)**',
            inline=False
        )
        embed.add_field(
            name='!vote @treść',
            value='• Tworzy ankietę do głosowania',
            inline=False
        )
        embed.add_field(
            name='!build @klasa @pod_co',
            value='• Zwraca proponowany build danej '
            '@klasy **(necro, monk, bar, crus, hun, wiz)** oraz '
            '@pod_jakie instancje ma być używany **(zlecenia, szczelina_pradawna, szczelina_wyzwań, lochy, levelowanie, pvp, relik, solo_farma)** ',
            inline=False
        )
        embed.add_field(
            name='!horadrim @nazwa',
            value='• Wyświetla informacje o danym naczyniu, gdzie go zdobyć oraz '
            'jakie warunki musisz spełniać by wypadł. Możliwe argumenty: \n'
            '> **all**  - wyświetla infografikę o wszystkich naczyniach z krótkim info \n'
            "> **cal**  - Miłosierdzie Caldesanna  | Caldensann's Compassion\n"
            "> **cat**  - Pobożność Cathana        | Cathan's Piety\n"
            "> **nam**  - Wina Bezimiennych        | Guilt if the Nameless\n"
            "> **ibe**  - Wytrwałość Iben Fahda    | Iben Fahds's Tenacity\n"
            "> **cain** - Wizja Jareda Caina       | Jered Cain's Vision\n"
            "> **nil**  - Precyzja Nilfura         | Nilfur's Precision \n"
            "> **nor**  - Wiedza Tiraja            | Nor Tiraj's Knowlage\n"
            "> **tal**  - Autorytet Tal Rashy      | Tal Rasha's Authority\n"
            "> **kul**  - Pomysłowość Zoltun Kuula | Zoltun Kuule's Ingenuity\n"
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))