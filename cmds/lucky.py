import discord, random, json, datetime, requests, bs4
from discord.ext import commands
from dcbot.core.classes import Cog_Extension

with open('D:\\dc_bot\\dcbot\\bot\\set.json', 'r', encoding='UTF-8') as jfile:
    jdata = json.load(jfile)

time_range = datetime.timedelta(hours = -8) # 減八小時

class lucky(Cog_Extension):

    @commands.command()
    async def 今日運勢(self, ctx, msg):
        if msg in jdata:
            username = ctx.message.author.display_name
            avatar = ctx.message.author.avatar_url
            url = jdata[msg]
            req = requests.get(url)
            req.encoding="utf-8"
            data = req.text
            
            #標題
            root = bs4.BeautifulSoup(data, "html.parser")
            minarea = root.find("div", class_="TODAY_CONTENT")
            minarea = str(minarea)
            title = bs4.BeautifulSoup(minarea, "html.parser")
            title = title.find("h3").string

            #運勢
            allword = bs4.BeautifulSoup(minarea, "html.parser")
            allword = allword.find_all("p")
            word = []
            for x in allword:
                strx = x.string
                strx = str(strx)
                word.append(strx)

            txt_green = word[0]
            txt_green_word = word[1]
            txt_pink = word[2]
            txt_pink_word = word[3]
            txt_blue = word[4]
            txt_blue_word = word[5]
            txt_orange = word[6]
            txt_orange_word = word[7]

            time = datetime.datetime.now()
            nowtime = time + time_range

            embed=discord.Embed(title=title, url=url, color=0x3daae1, timestamp=nowtime)
            embed.set_author(name = username+"輸入指令" ,icon_url = avatar)
            embed.add_field(name=txt_green, value=txt_green_word, inline=True)
            embed.add_field(name=txt_pink, value=txt_pink_word, inline=False)
            embed.add_field(name=txt_blue, value=txt_blue_word, inline=False)
            embed.add_field(name=txt_orange, value=txt_orange_word, inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(lucky(bot))