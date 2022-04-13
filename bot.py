import discord
from discord.ext import commands
import os

from Cogs.help_cog import help_cog
from Cogs.music_cog import music_cog
from Cogs.clip_cog import clip_cog
from Cogs.search_cog import search_cog

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix = '+', case_insensitive=True, intents=intents)

bot.remove_command('help')

bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))
bot.add_cog(clip_cog(bot))
bot.add_cog(search_cog(bot))

bot.run(os.getenv('TOKEN'))