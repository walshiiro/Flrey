
import discord
from discord import Intents, Client

from discord.ext import commands
import Paginator

import requests
import json


intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)
prefix ='^'

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('Firefly to master: {:.2f} ms'.format(bot.latency *1000))
@bot.command()
async def user(ctx ,uid):
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


@bot.command()
async def invlink(ctx):
    await ctx.send('https://discord.com/oauth2/authorize?client_id=1239763299491381359')


@bot.command()
async def setuser(ctx, uid):
    userid = id(ctx.author)
    zip(str(userid), str(uid))
    embed = discord.Embed(url="https://example.com",
                          description=":white_check_mark:  Your UID has been edited to " + uid,
                          colour=0x00b0f4
                          )

    embed.set_author(name="Configure: Genshin UID",
                     icon_url="https://i.imgur.com/T8KX9tC.jpg")

    embed.set_footer(text="Fley Discord Bot",
                     icon_url="https://i.imgur.com/T8KX9tC.jpg")

    await ctx.send(embed=embed)


@bot.command()
async def char(ctx, uid):

    src = 'https://enka.network/api/uid/' + uid  # get data from EnkaNetwork
    solditems = requests.get(src)
    data = solditems.json()
    with open('jsonfile/userinfo.json', 'w') as f:
        json.dump(data, f)
    embeds=[]
    userdata = json.load(open('jsonfile/userinfo.json'))
    weapon = json.load(open('jsonfile/weaponname.json', encoding='utf-8'))

    if 'showAvatarInfoList' not in userdata['playerInfo']:
        await ctx.send('You have not shown any Character yet!')
    else:
        numberChar = len(userdata['playerInfo']['showAvatarInfoList'])  # Get the number of Char showcase
    if numberChar != 0:
        for current in range(0,numberChar):
        # Get char info
            charimgid = userdata['avatarInfoList'][current]['avatarId']
            charimgid1 = str(charimgid)
            character = json.load(open('jsonfile/charinfo.json'))
            charAVT = character[charimgid1]['SideIconName']
            charlvl = userdata['avatarInfoList'][current]['propMap']['4001']['val']

            if '2' not in userdata['avatarInfoList'][current]['fightPropMap'] and '3' not in \
                userdata['avatarInfoList'][current]['fightPropMap']:
                HP = userdata['avatarInfoList'][current]['fightPropMap']['1']
            elif '2' in userdata['avatarInfoList'][current]['fightPropMap'] and '3' not in \
                userdata['avatarInfoList'][current]['fightPropMap']:
                HP = userdata['avatarInfoList'][current]['fightPropMap']['1'] + \
                 userdata['avatarInfoList'][current]['fightPropMap']['2']
            elif '2' not in userdata['avatarInfoList'][current]['fightPropMap'] and '3' in \
                userdata['avatarInfoList'][current]['fightPropMap']:
                HP = userdata['avatarInfoList'][current]['fightPropMap']['1'] + \
                 userdata['avatarInfoList'][current]['fightPropMap']['1'] * \
                 userdata['avatarInfoList'][current]['fightPropMap']['3']
            else:
                HP = userdata['avatarInfoList'][current]['fightPropMap']['1'] + \
                 userdata['avatarInfoList'][current]['fightPropMap']['2'] + (
                             userdata['avatarInfoList'][current]['fightPropMap']['1'] +
                             userdata['avatarInfoList'][current]['fightPropMap']['2']) * \
                 userdata['avatarInfoList'][current]['fightPropMap']['3']

            if '5' not in userdata['avatarInfoList'][current]['fightPropMap'] and '6' not in \
                userdata['avatarInfoList'][current]['fightPropMap']:
                ATK = userdata['avatarInfoList'][current]['fightPropMap']['4']
            elif '5' in userdata['avatarInfoList'][current]['fightPropMap'] and '6' not in \
                userdata['avatarInfoList'][current]['fightPropMap']:
                ATK = userdata['avatarInfoList'][current]['fightPropMap']['4'] + \
                  userdata['avatarInfoList'][current]['fightPropMap']['5']
            elif '5' not in userdata['avatarInfoList'][current]['fightPropMap'] and '6' in \
                userdata["avatarInfoList"][current]['fightPropMap']:
                ATK = userdata['avatarInfoList'][current]['fightPropMap']['4'] + \
                  userdata['avatarInfoList'][current]['fightPropMap']['4'] * \
                  userdata['avatarInfoList'][current]['fightPropMap']['6']
            else:
                ATK = userdata['avatarInfoList'][current]['fightPropMap']['4'] + \
                  userdata['avatarInfoList'][current]['fightPropMap']['5'] + (
                              userdata['avatarInfoList'][current]['fightPropMap']['4'] +
                              userdata['avatarInfoList'][current]['fightPropMap']['5']) * \
                  userdata['avatarInfoList'][current]['fightPropMap']['6']

            if '8' not in userdata['avatarInfoList'][current]['fightPropMap'] and '9' not in \
                userdata['avatarInfoList'][current]['fightPropMap']:
                DEF = userdata['avatarInfoList'][current]['fightPropMap']['7']
            elif '8' in userdata['avatarInfoList'][current]['fightPropMap'] and '9' not in \
                userdata['avatarInfoList'][current]['fightPropMap']:
                DEF = userdata['avatarInfoList'][current]['fightPropMap']['7'] + \
                  userdata['avatarInfoList'][current]['fightPropMap']['8']
            elif '8' not in userdata['avatarInfoList'][current]['fightPropMap'] and '9' in \
                userdata["avatarInfoList"][current]['fightPropMap']:
                DEF = userdata['avatarInfoList'][current]['fightPropMap']['7'] + \
                  userdata['avatarInfoList'][current]['fightPropMap']['7'] * \
                  userdata['avatarInfoList'][current]['fightPropMap']['9']
            else:
                DEF = userdata['avatarInfoList'][current]['fightPropMap']['7'] + \
                  userdata['avatarInfoList'][current]['fightPropMap']['8'] + (
                              userdata['avatarInfoList'][current]['fightPropMap']['7'] +
                              userdata['avatarInfoList'][current]['fightPropMap']['8']) * \
                  userdata['avatarInfoList'][current]['fightPropMap']['9']

            CRITRate = userdata['avatarInfoList'][current]['fightPropMap']['20'] * 100
            CritDMG = userdata['avatarInfoList'][current]['fightPropMap']['22'] * 100
            ER = userdata['avatarInfoList'][current]['fightPropMap']['23']
            EM = userdata['avatarInfoList'][current]['fightPropMap']['28']
            WeaponID = userdata['avatarInfoList'][current]['equipList'][5]['flat']['nameTextMapHash']
            WeaponLevel = userdata['avatarInfoList'][current]['equipList'][5]['weapon']['level']
            WeaponName = weapon['en'][WeaponID]
            BaseATK = userdata['avatarInfoList'][current]['equipList'][5]['flat']['weaponStats'][0]['statValue']
            anotherfromweaponidfkwtfisthat = userdata['avatarInfoList'][0]['equipList'][5]['flat']['weaponStats'][1][
            'appendPropId']
            base2stats = userdata['avatarInfoList'][current]['equipList'][5]['flat']['weaponStats'][1]['statValue']
            if anotherfromweaponidfkwtfisthat == 'FIGHT_PROP_HP':
                Base2 = 'Flat HP'
            elif anotherfromweaponidfkwtfisthat == 'FIGHT_PROP_ATTACK':
                Base2 = 'Flat ATK'
            elif anotherfromweaponidfkwtfisthat == 'FIGHT_PROP_DEFENSE':
                Base2 = 'Flat DEF'
            elif anotherfromweaponidfkwtfisthat == 'FIGHT_PROP_HP_PERCENT':
                Base2 = 'HP%'
            elif anotherfromweaponidfkwtfisthat == 'FIGHT_PROP_ATTACK_PERCENT':
                Base2 = 'ATK%'
            elif anotherfromweaponidfkwtfisthat == 'FIGHT_PROP_DEFENSE_PERCENT':
                Base2 = 'DEF%'
            elif anotherfromweaponidfkwtfisthat == 'FIGHT_PROP_CRITICAL':
                Base2 = 'Crit RATE'
            elif anotherfromweaponidfkwtfisthat == 'FIGHT_PROP_CRITICAL_HURT':
                Base2 = 'Crit DMG'
            elif anotherfromweaponidfkwtfisthat == 'FIGHT_PROP_CHARGE_EFFICIENCY':
                Base2 = 'Energy Recharge'
            elif anotherfromweaponidfkwtfisthat == 'FIGHT_PROP_HEAL_ADD':
                Base2 = 'Healing Bonus'
            elif anotherfromweaponidfkwtfisthat == 'FIGHT_PROP_ELEMENT_MASTERY':
                Base2 = 'Elemental Mastery'
            nickname = userdata["playerInfo"]['nickname']
            UID = userdata['uid']
            descrip = "**Weapon**: " + WeaponName + " (LVL: " + str(WeaponLevel) + ")" + "\n**Base ATK**: " + str(
            BaseATK) + "\n**" + Base2 + "**: " + str(base2stats) + "\n**Character Level**: " + str(
            charlvl) + "\n**▸HP**: " + str(round(HP, 3)) + "\n**▸ATK**: " + str(
            int(round(ATK, 0))) + "\n**▸DEF**: " + str(int(round(DEF, 0))) + "\n**▸EM**: " + str(
            int(round(EM, 0))) + "\n**▸Crit Rate**: " + str(round(CRITRate, 1)) + "%" + "\n**▸Crit DMG**:" + str(
            round(CritDMG, 1)) + "%" + "\n**▸ER**: " + str(round(ER * 100, 1)) + "%"
        # Embed the infomation
            embed = discord.Embed(description=descrip, colour=0x00b0f4)

            embed.set_author(name="Character Showcase for " + nickname, url="https://enka.network/u/" + UID,
                         icon_url="https://i.pinimg.com/564x/16/5d/f0/165df0ced77df9aaf3903af3db5e93d1.jpg")

            embed.set_thumbnail(url="https://enka.network/ui/" + charAVT + ".png")

            embed.set_footer(text="Get the infomation from EnkaNetwork")
            embeds.append(embed)
            PreviousButton = discord.ui.Button(label="<",style=discord.ButtonStyle.gray)
            NextButton = discord.ui.Button(label=">",style=discord.ButtonStyle.gray)
        await Paginator.Simple(PreviousButton=PreviousButton,
    NextButton=NextButton,).start(ctx, pages=embeds)



        


TOKEN = 'your token'
bot.run(TOKEN)