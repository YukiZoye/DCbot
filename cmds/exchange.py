import discord, random, json, datetime, lxml
from discord.ext import commands
from dcbot.core.classes import Cog_Extension
import requests # 模組建立各種 HTTP 請求，從網頁伺服器上取得想要的資料。
import pandas as pd # 進行資料處理和資料分析的工具

dollars = ['USD','HKD','GBP','AUD','CAD','SGD','CHF','JPY','ZAR','SEK','NZD','THD','PHP','IDR','EUR','KRW','VND','MYR','CNY'] # 新增可查詢幣別到List

class exchange(Cog_Extension):
    
    @commands.command()
    async def 匯率(self, ctx, msg):
        msg = msg.upper() # 轉換大寫
        if msg in dollars:
            url_address = 'http://rate.bot.com.tw/xrt/quote/day/' + msg # 欲查詢幣別網址
            res = requests.get(url_address) # 普通單純的網頁，只需要用最簡單的 GET 請求即可直接下載
            table = pd.read_html(res.text) # 將資料轉換為Dataframe

            df = table[0]  # 看一下第一個表格內容

            df.columns = df.columns.droplevel() # 從一個多層次的行索引下降一級
            
            df = df.drop('Unnamed: 6_level_1', axis = 1) # 刪除第六行空值內容
            df = df.drop('Unnamed: 7_level_1', axis = 1) # 刪除第七行空值內容

            df.columns = ['------掛牌日期時間------', '---幣別---', '現金:買', '現金:賣', '即期:買', '即期:賣'] # 重設列名稱
            
            df.index += 1   # 索引值改成從 1 開始

        await ctx.send(df) #印出結果

    @commands.command()
    async def test(self, ctx, msg):
        msg = msg.upper() # 轉換大寫
        await ctx.send(msg)


def setup(bot):
    bot.add_cog(exchange(bot))