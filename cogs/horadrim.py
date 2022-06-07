import discord, io, aiohttp
from discord.ext import commands

class Horadrims(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Hoardrim cog is loaded')
    
    @commands.command()
    async def horadrim(self, ctx, arg):
        urls = {
            "all" : "https://i.imgur.com/r59Xo5S.png",
            "cal" : "https://i.imgur.com/jLdq0jK.png",
            "cat" : "https://i.imgur.com/JfPodax.png",
            "nam" : "https://i.imgur.com/LZidIX6.png",
            "ibe" : "https://i.imgur.com/VnPZ9a0.png",
            "cain": "https://i.imgur.com/Tqo53R4.png",
            "nil" : "https://i.imgur.com/BflWeCo.png",
            "nor" : "https://i.imgur.com/TU38nJS.png",
            "tal" : "https://i.imgur.com/kJsTQEg.png",
            "kul" : "https://i.imgur.com/SvYWwTp.png"
        }

        if arg not in urls:
            return await ctx.send(
                "Nie ma takiego naczynia\n"
                "Możliwe opcje: all, cal, cat, nam, ibe, cain, nil, nor, tal, kul"
            )
        else:

            URL = urls[arg]

            async with aiohttp.ClientSession() as session:
                async with session.get(URL) as resp:
                    if resp.status != 200:
                        return await ctx.send('Błąd pobierania')
                    else:
                        data = io.BytesIO(await resp.read())
                        await ctx.send(file=discord.File(data, "vessel.png"))

def setup(bot):
    bot.add_cog(Horadrims(bot))                    