import discord, random, json, datetime
from discord.ext import commands
from dcbot.core.classes import Cog_Extension

with open('D:\\dc_bot\\dcbot\\bot\\set.json', 'r', encoding='UTF-8') as jfile:
    jdata = json.load(jfile)

percent = str('%')
time_range = datetime.timedelta(hours = -8) # 減八小時

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
    async def 幸運指數(self, ctx):
        number = random.randrange(1,101)
        number = str(number)
        time = datetime.datetime.now()
        nowtime = time + time_range
        username = ctx.message.author.display_name
        avatar = ctx.message.author.avatar_url
        embed=discord.Embed(title=":four_leaf_clover::turtle: 今天的幸運指數:turtle::four_leaf_clover:",
                            description=("%s，你今天的幸運指數是%s%s！"%(username, number, percent)), color=0x3daae1,
                            timestamp=nowtime)
        embed.set_thumbnail(url="https://github.com/YukiZoye/DCbot/blob/main/picture/%E5%82%91%E5%B0%BC%E9%BE%9C%E8%AE%9A.gif?raw=true")
        embed.set_author(name = username+"輸入指令" ,icon_url = avatar)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Main(bot))