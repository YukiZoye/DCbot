import discord
from discord.ext import commands
import json
import random
import os

with open('dcbot\\bot\\set.json', 'r', encoding='UTF-8') as jfile:
    jdata = json.load(jfile)

with open('D:\dc_bot\\token\\token.json', 'r', encoding='UTF-8') as jt:
    jtoken = json.load(jt)

bot = commands.Bot(command_prefix = '%')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def joined_at(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    ping = round(bot.latency*1000)
    await ctx.send(f'延遲為: {(ping)} (ms)')

@bot.command()
async def 圖片(ctx):
    random_picture = random.choice(jdata['url_picture'])
    await ctx.send(random_picture)

bot.run(jtoken['TOKEN'])