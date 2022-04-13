import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.help_message = '''
        ```
        General Commands:
        +help - Showcases this message
        +search <query> - Searches the query on google

        Music Commands:
        +play <query> - Searches the query on youtube and plays it in your current channel
        +pause - Pauses the song being play and resumes if already paused
        +resume - Resumes playing the current song
        +skip - Skips the current song being played
        +queue - Displays the current music queue
        +clear - Clears the queue and stops playback
        +leave - Disconnects bot from the voice channel
        ```
        '''
        self.text_channel_text = []
    
    @commands.command(name = 'help', aliases = ['h'], help = 'Displays help message')
    async def help(self, ctx):
        await ctx.send(self.help_message)
    
    @commands.Cog.listener()
    async def on_ready(self):
        game = discord.Game('Waiting for + in life')
        await self.bot.change_presence(status=discord.Status.online, activity=game)
        print('Setsuna has been corrupted!')