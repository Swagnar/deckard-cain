import discord, io, aiohttp
from discord.ext import commands

class Maps(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Maps cog is loaded')

    # !map command
    @commands.command()
    async def map(self, ctx, arg):

        # dictionary with keys of @arg and values or URL with JPG of given location  
        
        urls = {
            "cmentarz": "http://diablo.blizzplanet.com/wp-content/uploads/2021/05/ashwold-cemetery-purple-rare-elites-no-skull.jpg",
            "knieja": "http://diablo.blizzplanet.com/wp-content/uploads/2021/05/darkwood-purple-rare-elites-no-skull.jpg",
            "bagno": "http://diablo.blizzplanet.com/wp-content/uploads/2021/05/bilefen-purple-rare-elites-no-skull.jpg",
            "morze": "http://diablo.blizzplanet.com/wp-content/uploads/2021/05/shassar-sea-purple-rare-elites-no-skull.jpg",
            "biblioteka": "http://diablo.blizzplanet.com/wp-content/uploads/2021/05/library-of-zoltun-kulle-purple-rare-elites-no-skull.jpg",
            "góra": "http://diablo.blizzplanet.com/wp-content/uploads/2021/05/mount-zavain-purple-rare-elites-no-skull.jpg",
            "tundra" : "http://diablo.blizzplanet.com/wp-content/uploads/2021/05/frozen-tundra-purple-rare-elites-no-skull.jpg"
        }

        # if user inputs @arg thats not in the dictionary

        if arg not in urls:
            return await ctx.send(
                "Nie ma takiego miejsca w Sanktuarium\n"
                "Możliwe opcje: **cmentarz**, **knieja**, **bagno**, **morze**, **biblioteka**, **góra**, **tundra**"
            )
        else:

            # URL = value of given key from dictionary
            URL = urls[arg]
        
            # stolen code <3

            async with aiohttp.ClientSession() as session:
                async with session.get(URL) as resp:
                    if resp.status != 200:
                        return await ctx.send('Błąd pobierania')
                    else:
                        data = io.BytesIO(await resp.read())
                        await ctx.send(file=discord.File(data, "map.png"))

def setup(bot):
    bot.add_cog(Maps(bot))