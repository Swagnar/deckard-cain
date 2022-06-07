import discord


from discord.ext import commands
from classes.scrapper import Scrapper

# initialize helper class
myScrapper = Scrapper()

class Build(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Build cog is loaded')
        

    @commands.command()
    async def build(self, ctx, userClass, instance):

        # create dictionaries of values used in URL
        classes = {
            "necro": "necromancer",
            "monk" : "monk",
            "bar"  : "barbarian",
            "crus" : "crusader",
            "hun"  : "demon-hunter",
            "wiz"  : "wizard"
        }
        metas = {
            "zlecenia"              : "bounty",
            "szczelina_pradawna"    : "elder-rift",
            "szczelina_wyzwań"      : "challenge-rift",
            "lochy"                 : "dungeon",
            "levelowanie"           : "leveling",
            "pvp"                   : "pvp",
            "relik"                 : "raid",
            "solo"                  : "solo-farming"
        }

        # check if user inputs are in dictionaries
        if userClass not in classes:
            await ctx.send("\N{CROSS MARK}" + " Nie ma takiej klasy")
        elif instance not in metas:
            await ctx.send("\N{CROSS MARK}" + " Nie ma takiej aktywności")
        elif userClass not in classes and instance not in metas:
            await ctx.send("\N{CROSS MARK}" + " Obie składnie polecenia są nieprawidłowe")
        else:            
            
            url = f"https://immortal.maxroll.gg/category/build-guides#classes%3D%5Bdi-{classes[userClass]}%5D%26metas%3D%5Bdi-{metas[instance]}%5D"

            # embed = discord.Embed(
            #     color = discord.Color.green()
            # )
            # embed.set_author(name='Komenda w budowie')
            # embed.add_field(
            #     name='Brak implementacji',
            #     value='Tymczasem musisz sam wejść i przeglądać',
            #     inline = False
            # )
            # await ctx.send(embed=embed)
            await ctx.send(url)

            #await myScrapper.return_build_articles(classes[userClass], metas[instance])

def setup(bot):
    bot.add_cog(Build(bot))
            