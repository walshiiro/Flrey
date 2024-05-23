import discord
from discord import Intents, Client

from discord.ext import commands
from discord.ext.commands import bot
import Paginator

import requests
import json

async def checkusers(ctx,uid):
    src = 'https://enka.network/api/uid/' + uid # get data from EnkaNetwork
    solditems = requests.get(src)
    data = solditems.json()
    with open('jsonfile/userinfo.json', 'w') as f:
        json.dump(data, f)
    user =json.load(open('jsonfile/userinfo.json'))
    idcards =json.load(open('jsonfile/cardsname.json'))
    avatars =json.load(open('jsonfile/avatar.json'))
    user['test'] = True # user information
    idcards['test'] = True # User's Cards
    avatars['test'] = True # User's ingame avatar


    # Get data from json file
    nickname = user["playerInfo"]['nickname']
    ar = user["playerInfo"]['level']
    AR = str(ar)
    if 'signature' in user["playerInfo"]:
        signature = user["playerInfo"]['signature']
    else:
        signature ='None Bio Yet'
    worldlevel = user["playerInfo"]['worldLevel']
    finishAchievement = user["playerInfo"]['finishAchievementNum']
    SpiralAbyss = user["playerInfo"]['towerFloorIndex']
    SpiralAbyssLevel = user["playerInfo"]['towerLevelIndex']
    UID = user['uid']
    cards = user["playerInfo"]['showNameCardIdList'][0]
    avatar = user["playerInfo"]['profilePicture']['id']
    idcard = idcards[str(cards)]["icon"]
    idavatar = avatars[str(avatar)]["iconPath"]
    descrip = "> **Signature**: " + signature + "\n**▸AR**: " + str(ar) + "\n**▸World Level**: " + str(
        worldlevel) + "\n**▸Achievement**: " + str(finishAchievement) + "\n**▸SpiralAbyss**: " + str(
        SpiralAbyss) + "-" + str(SpiralAbyssLevel) + "\n**▸UID**: " + str(uid)
    akashaprof = 'https://enka.network/u/' + UID
    embed = discord.Embed(description=descrip, colour=0x00b0f4)
    embed.set_author(name="Genshin Impact Profile for " + nickname,
                     url="https://enka.network/u/" + UID,
                     icon_url="https://i.pinimg.com/564x/16/5d/f0/165df0ced77df9aaf3903af3db5e93d1.jpg")
    embed.set_thumbnail(url="https://enka.network/ui/" + idavatar + ".png")
    embed.set_footer(text="Get the data from EnkaNetwork",
                     icon_url="https://i.pinimg.com/736x/ff/b3/0f/ffb30fef8712c9503e23a4b851c2a85c.jpg")
    embed.set_image(url="https://enka.network/ui/" + idcard + ".png")
    await ctx.send(embed=embed)