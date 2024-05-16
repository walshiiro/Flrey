import discord
from discord.ext import commands

from discord.app_commands import commands
from discord import Intents, Client, Message
from discord.ext import commands
import requests
import json

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('Firefly to master: {:.2f} ms'.format(bot.latency*1000))
@bot.command()
async def show(ctx,uid):
    src = 'https://enka.network/api/uid/' + uid + '?info'
    solditems = requests.get(src)
    data = solditems.json()
    with open('userinfo.json', 'w') as f:
        json.dump(data, f)
    user=json.load(open('userinfo.json'))
    user['test'] = True
    

    nickname = user["playerInfo"]['nickname']
    ar = user["playerInfo"]['level']
    if 'signature' in user["playerInfo"]:
        signature = user["playerInfo"]['signature']
    else:
        signature ='None Bio Yet'
    worldlevel = user["playerInfo"]['worldLevel']
    finishAchievement = user["playerInfo"]['finishAchievementNum']
    SpiralAbyss = user["playerInfo"]['towerFloorIndex']
    SpiralAbyssLevel = user["playerInfo"]['towerLevelIndex']

    UID = user['uid']

    akashaprof = 'https://enka.network/u/'+UID
    embed = discord.Embed(title="Genshin Impact Profile for "+nickname, url=akashaprof,description='Bio: '+signature, color=0x2dd293)
    embed.set_thumbnail(url="https://i.pinimg.com/564x/8a/22/65/8a226533a6f24520d3f26a34df3db77b.jpg")
    embed.add_field(name="AR", value=ar, inline=True)
    embed.add_field(name="World Level", value=worldlevel, inline=True)
    embed.add_field(name="Achievement", value=finishAchievement, inline=True)
    embed.add_field(name="SpiralAbyss", value=SpiralAbyss, inline=True)
    embed.add_field(name="SpiralAbyss Room", value=SpiralAbyssLevel, inline=True)
    embed.add_field(name="UID", value=UID, inline=True)
    embed.set_footer(text="Get the infomation from EnkaNetwork!")
    await ctx.send(embed=embed)













    

TOKEN ='your token'
bot.run(TOKEN)
