import discord, json, random, os, datetime
from discord.ext import commands

intents = discord.Intents.all()

with open('C:\\Users\\USER\\Downloads\\dcbot\\bot\\set.json', 'r', encoding='UTF-8') as jfile:
    jdata = json.load(jfile)

with open('C:\\Users\\USER\\Downloads\\token\\token.json', 'r', encoding='UTF-8') as jt:
    jtoken = json.load(jt)

bot = commands.Bot(command_prefix = '%', intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'{member} leave!')

for filename in os.listdir('C:\\Users\\USER\\Downloads\\dcbot\\cmds'):
    if filename.endswith('.py'):
        bot.load_extension(F'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jtoken['TOKEN'])