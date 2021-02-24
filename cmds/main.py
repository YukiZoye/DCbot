import discord, random, json, datetime
from discord.ext import commands
from core.classes import Cog_Extension

with open('C:\\Users\\USER\\Downloads\\dcbot\\bot\\set.json', 'r', encoding='UTF-8') as jfile:
    jdata = json.load(jfile)

class Main(Cog_Extension):
    
    @commands.command()
    async def ping(self, ctx):
        ping = round(self.bot.latency*1000)
        await ctx.send(f'延遲為: {(ping)} (ms)')

    @commands.command()
    async def 圖片(self, ctx):
        random_picture = random.choice(jdata['url_picture'])
        await ctx.send(random_picture)
    
    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title=":turtle::four_leaf_clover: 今天的幸運指數:four_leaf_clover::turtle:", color=0x40c9f7, timestamp=datetime.datetime.now())
        embed.set_thumbnail(url="https://github.com/YukiZoye/DCbot/blob/main/picture/%E5%82%91%E5%B0%BC%E9%BE%9C%E8%AE%9A.gif?raw=true")
        embed.add_field(name="", value="", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Main(bot))