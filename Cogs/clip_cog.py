import discord
from discord.ext import commands
import time

class clip_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.is_playing = False
        self.is_paused = False
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    @commands.command(name = 'bang', help = 'Plays the iconic bang bang bang clip')
    async def bang(self, ctx):
        voice_channel = ctx.author.voice.channel
        channel = None

        if voice_channel != None:
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio(executable = r'/app/vendor/ffmpeg.exe', source = r'/app/Clips/bang.mp3'))
            
            while vc.is_playing():
                time.sleep(.1)
            await vc.disconnect()
        
        else:
            await ctx.send('You are not in a channel baka.')

        await ctx.message.delete()