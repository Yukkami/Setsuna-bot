import discord
from discord.ext import commands

from googlesearch import search
    
class search_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.query = ''
        self.results = []
        self.result_number = 0
        self.emojis = ['⬅️', '➡️', '⏹️']
        self.message = ''
    
    @commands.command(name= 'search', help = 'Searches google for your query')
    async def search(self, ctx, *args):
        self.query = ' '.join(args)
        self.result_number = 1

        for i in search(self.query, num=10, stop=10, pause=2):
            self.results.append(i)
    
        embed = discord.Embed(title = 'Search', description = self.results[self.result_number])
        embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=f'{ctx.author.avatar_url}')

        self.message = await ctx.send(embed = embed)

        for i in self.emojis:
            await self.message.add_reaction(i)
    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        emoji = reaction.emoji
        message_id = await self.bot.get_channel(self.message.channel.id).fetch_message(self.message.id)

        if user.bot:
            return

        if emoji == '⬅️':

            if self.result_number == 1:
                return
            
            else:
                self.result_number = self.result_number - 1

                edited_embed = discord.Embed(title = 'Search-1', description = self.results[self.result_number])
                edited_embed.set_footer(text=f'Requested by {user.name}#{user.discriminator}', icon_url=f'{user.avatar_url}')
                await message_id.edit(embed = edited_embed)

        elif emoji == '➡️':

            if self.result_number == 10:
                return
            
            else:
                self.result_number = self.result_number + 1

                edited_embed = discord.Embed(title = 'Search+1', description = self.results[self.result_number])
                edited_embed.set_footer(text=f'Requested by {user.name}#{user.discriminator}', icon_url=f'{user.avatar_url}')
                await message_id.edit(embed = edited_embed)

        elif emoji == '⏹️':
            self.result_number = 0

            for i in self.emojis:
                await self.message.clear_reaction(i)

        else:
            return


    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        emoji = reaction.emoji
        message_id = await self.bot.get_channel(self.message.channel.id).fetch_message(self.message.id)

        if user.bot:
            return

        if emoji == '⬅️':

            if self.result_number == 1:
                return
            
            else:
                self.result_number = self.result_number - 1

                edited_embed = discord.Embed(title = 'Search-1', description = self.results[self.result_number])
                edited_embed.set_footer(text=f'Requested by {user.name}#{user.discriminator}', icon_url=f'{user.avatar_url}')
                await message_id.edit(embed = edited_embed)

        elif emoji == '➡️':

            if self.result_number == 10:
                return
            
            else:
                self.result_number = self.result_number + 1

                edited_embed = discord.Embed(title = 'Search+1', description = self.results[self.result_number])
                edited_embed.set_footer(text=f'Requested by {user.name}#{user.discriminator}', icon_url=f'{user.avatar_url}')
                await message_id.edit(embed = edited_embed)

        elif emoji == '⏹️':
            self.result_number = 0

            for i in self.emojis:
                await self.message.clear_reaction(i)

        else:
            return