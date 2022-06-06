import discord
from discord.ext import commands

class Vote(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Vote cog is loaded")

    @commands.command()
    async def vote(self, ctx, text):

        # TODO: change to proper channel ID
        if(ctx.channel.id != 820700681375449092):
            await ctx.send("Głosować można tylko na kanale #głosowania")
        else:
            # get the command author
            author = ctx.author

            # create emoji table, 0 - ✅, 1 - ❌
            emojis = ["\N{WHITE HEAVY CHECK MARK}", "\N{CROSS MARK}"]

            # construct the message and send it
            content = '**'+str(author)+'**'+' głosuje o: '+text
            message = await ctx.send(content)

            # foreach emoji in emojis table, add it as a reaction to the sent message
            for emoji in emojis:
                await message.add_reaction(emoji)

def setup(bot):
    bot.add_cog(Vote(bot))