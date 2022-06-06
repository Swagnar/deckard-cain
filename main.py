import os

from dotenv import load_dotenv
from discord.ext import commands

# in the main directory create .env file with const variable DISCORD_TOKEN="your_token"

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='!')
bot.remove_command("help")

# for each file in /cogs directory, if it ends with .py, strip the last 3 chars
# example.py -> example
# and load that file using load_extension

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(DISCORD_TOKEN)

# MISC FUNCTIONS

# function for loading extensions
# @bot.command()
# @commands.is_owner()
# async def load(ctx, extension):
#     bot.load_extension(f'cogs.{extension}')


# function for unloading extensions
# @bot.command()
# @commands.is_owner()
# async def unload(ctx, extension):
#     bot.unload_extension(f'cogs.{extension}')