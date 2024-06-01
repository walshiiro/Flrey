
import discord
from discord import Intents, Client,User

from discord.ext import commands
import Paginator
import random
import mysql.connector
import requests
import json
import genshin.charbuild
import genshin.checkbuild
import genshin.checkchars
import genshin.checkuser
import genshin.invlink1 as invlink1
import genshin.userpages as userpages
import genshin.chardisplay as chardisplay
import genshin


intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)
prefix ='^'

bot = commands.Bot(command_prefix=prefix, intents=intents)


mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)
mycursor = mydb.cursor()


@bot.command()
async def ping(ctx):
    await ctx.send('Firefly to master: {:.2f} ms'.format(bot.latency *1000))

@bot.command()
async def user(ctx):
    await userpages.user1(ctx)
    
@bot.command()
async def checkuser(ctx,uid):
    await genshin.checkuser.checkusers(ctx,uid)
@bot.command()
async def checkchar(ctx,uid):
    await genshin.checkchars.checkchars(ctx,uid)
@bot.command()
async def checkbuild(ctx,uid,charnum):
    await genshin.checkbuild.build(ctx,uid,charnum)


@bot.command()
async def build(ctx,charnum1):
    userid = ctx.message.author.id
    sql = "SELECT * FROM discorduserid WHERE userid =%s"
    val =(userid, )
    mycursor.execute(sql,val)
    index = mycursor.fetchall()
    check= len(index)
    if(check==1):
        for i in index:
            uid = i[1]
        src = 'https://enka.network/api/uid/' + uid  # get data from EnkaNetwork
        solditems = requests.get(src)
        data = solditems.json()
        charnum = ord(charnum1) - ord('0') -1
        with open('jsonfile/userinfo.json', 'w') as f:
            json.dump(data, f)
        userdata=json.load(open('jsonfile/userinfo.json'))
        embeds=[]
    #get how many artifact the char equiped
        getNumberArtifacts= len(userdata['avatarInfoList'][charnum]['equipList'])-1
        if getNumberArtifacts==0:
                    embed = discord.Embed(
                          description=":negative_squared_cross_mark:  You didn't equip any artifact",
                          colour=0x00b0f4
                          )

                    embed.set_author(name="Configure: Genshin UID",
                     icon_url="https://i.imgur.com/T8KX9tC.jpg")

                    embed.set_footer(text="Fley Discord Bot",
                     icon_url="https://i.imgur.com/T8KX9tC.jpg")
                    await ctx.send(embed=embed)
        else:
            for i in range(0,getNumberArtifacts):
                MainStats = userdata['avatarInfoList'][charnum]['equipList'][i]['flat']['reliquaryMainstat']['mainPropId']
                if MainStats == 'FIGHT_PROP_HP':
                    MainStats = 'Flat HP'
                elif MainStats == 'FIGHT_PROP_ATTACK':
                    MainStats = 'Flat ATK'
                elif MainStats == 'FIGHT_PROP_DEFENSE':
                    MainStats = 'Flat DEF'
                elif MainStats == 'FIGHT_PROP_HP_PERCENT':
                    MainStats = 'HP%'
                elif MainStats == 'FIGHT_PROP_ATTACK_PERCENT':
                    MainStats = 'ATK%'
                elif MainStats == 'FIGHT_PROP_DEFENSE_PERCENT':
                    MainStats = 'DEF%'
                elif MainStats == 'FIGHT_PROP_CRITICAL':
                    MainStats = 'Crit RATE'
                elif MainStats == 'FIGHT_PROP_CRITICAL_HURT':
                    MainStats = 'Crit DMG'
                elif MainStats == 'FIGHT_PROP_CHARGE_EFFICIENCY':
                    MainStats = 'Energy Recharge'
                elif MainStats == 'FIGHT_PROP_HEAL_ADD':
                    MainStats = 'Healing Bonus'
                elif MainStats == 'FIGHT_PROP_ELEMENT_MASTERY':
                    MainStats = 'Elemental Mastery'
                elif MainStats == 'FIGHT_PROP_PHYSICAL_ADD_HURT':
                    MainStats = 'Physical DMG Bonus'
                elif MainStats == 'FIGHT_PROP_FIRE_ADD_HURT':
                    MainStats = 'Pyro DMG Bonus'
                elif MainStats == 'FIGHT_PROP_ELEC_ADD_HURT':
                    MainStats = 'Electro DMG Bonus'
                elif MainStats == 'FIGHT_PROP_WATER_ADD_HURT':
                    MainStats = 'Hydro DMG Bonus'
                elif MainStats == 'FIGHT_PROP_WIND_ADD_HURT':
                    MainStats = 'Anemo DMG Bonus'
                elif MainStats == 'FIGHT_PROP_ICE_ADD_HURT':
                    MainStats = 'Cryo DMG Bonus'
                elif MainStats == 'FIGHT_PROP_ROCK_ADD_HURT':
                    MainStats = 'Geo DMG Bonus'
                elif MainStats == 'FIGHT_PROP_GRASS_ADD_HURT':
                    MainStats = 'Dendro DMG Bonus'
            
            
                MainStatsValue = userdata['avatarInfoList'][charnum]['equipList'][i]['flat']['reliquaryMainstat']['statValue']
                IconName ='https://enka.network/ui/'+userdata['avatarInfoList'][charnum]['equipList'][i]['flat']['icon']+'.png'
                ArtifactLvl=userdata['avatarInfoList'][charnum]['equipList'][i]['flat']['rankLevel']
            #equipType =userdata['avatarInfoList'][charnum]['equipList'][i]['flat']['rankLevel']['equipType']
                getNumberSubstats=len(userdata['avatarInfoList'][charnum]['equipList'][i]['flat']['reliquarySubstats'])
            
                appendPropId = []
                statValue = []

                for j in range(0,getNumberSubstats):
                    appendPropId.append(userdata['avatarInfoList'][charnum]['equipList'][i]['flat']['reliquarySubstats'][j]['appendPropId'])
                    statValue.append(userdata['avatarInfoList'][charnum]['equipList'][i]['flat']['reliquarySubstats'][j]['statValue'])

                embed = discord.Embed(description="**Main Stats** :"+str(MainStats)+"\n**Value**: "+str(MainStatsValue)+"\n",
                    colour=0x00b0f4)

                embed.set_author(name="Build of the character")
                for j in range(0,getNumberSubstats):
                    if appendPropId[j] == 'FIGHT_PROP_HP':
                        appendPropId[j] = 'Flat HP'
                    elif appendPropId[j] == 'FIGHT_PROP_ATTACK':
                        appendPropId[j] = 'Flat ATK'
                    elif appendPropId[j] == 'FIGHT_PROP_DEFENSE':
                        appendPropId[j] = 'Flat DEF'
                    elif appendPropId[j] == 'FIGHT_PROP_HP_PERCENT':
                        appendPropId[j] = 'HP%'
                    elif appendPropId[j] == 'FIGHT_PROP_ATTACK_PERCENT':
                        appendPropId[j] = 'ATK%'
                    elif appendPropId[j] == 'FIGHT_PROP_DEFENSE_PERCENT':
                        appendPropId[j] = 'DEF%'
                    elif appendPropId[j] == 'FIGHT_PROP_CRITICAL':
                        appendPropId[j] = 'Crit RATE'
                    elif appendPropId[j] == 'FIGHT_PROP_CRITICAL_HURT':
                        appendPropId[j] = 'Crit DMG'
                    elif appendPropId[j] == 'FIGHT_PROP_CHARGE_EFFICIENCY':
                        appendPropId[j] = 'Energy Recharge'
                    elif appendPropId[j] == 'FIGHT_PROP_HEAL_ADD':
                        appendPropId[j] = 'Healing Bonus'
                    elif appendPropId[j] == 'FIGHT_PROP_ELEMENT_MASTERY':
                        appendPropId[j] = 'Elemental Mastery'
                    statValuez = str(statValue[j])
                    if '.' in statValuez:
                        statValuez = statValuez +"%"
                    embed.add_field(name="**Sub Stats**: "+str(appendPropId[j]),
                value="Value: "+statValuez,
                inline=False)

                embed.set_thumbnail(url=IconName)
                embed.set_footer(text="Get the infomation from EnkaNetwork")
                embeds.append(embed)
        PreviousButton = discord.ui.Button(label="<",style=discord.ButtonStyle.gray)
        NextButton = discord.ui.Button(label=">",style=discord.ButtonStyle.gray)
        await Paginator.Simple(PreviousButton=PreviousButton,NextButton=NextButton,).start(ctx, pages=embeds)
    else:
        embed = discord.Embed(
                          description=":negative_squared_cross_mark:  Your UID hasn't been add to the database",
                          colour=0x00b0f4
                          )

        embed.set_author(name="Configure: Genshin UID",
                     icon_url="https://i.imgur.com/T8KX9tC.jpg")

        embed.set_footer(text="Fley Discord Bot",
                     icon_url="https://i.imgur.com/T8KX9tC.jpg")
        await ctx.send(embed=embed)

@bot.command()
async def pick(ctx, first, second):
    await ctx.send('My choice is: {} '.format(random.choice([first, second])))
@bot.command()
async def whoisthebestdriver(ctx):
    await ctx.send('Max Verstappen for sure!!!')



@bot.command()
async def invlink(ctx):
    await invlink1.invlink(ctx)

#set user specific UID
@bot.command()
async def setuser(ctx,uid):
    userid = ctx.message.author.id

    #check if this userid in
    sql = "SELECT * FROM discorduserid WHERE userid =%s"
    val =(userid, )
    mycursor.execute(sql,val)
    index = mycursor.fetchall()
    check= len(index)
    

    
    if(check==0):
        sql = "INSERT INTO discorduserid (userid, useruid) VALUES (%s, %s)"
        val=(userid,uid)
        mycursor.execute(sql,val)
        mydb.commit()


        embed = discord.Embed(
                          description=":white_check_mark:  Your UID has been added to " + uid,
                          colour=0x00b0f4
                          )

        embed.set_author(name="Configure: Genshin UID",
                     icon_url="https://i.imgur.com/T8KX9tC.jpg")
        discordavt=ctx.message.author.avatar
        embed.set_thumbnail(url=discordavt)

        embed.set_footer(text="Fley Discord Bot",
                     icon_url="https://i.imgur.com/T8KX9tC.jpg")

        await ctx.send(embed=embed)
    else:
        sql = "UPDATE discorduserid SET useruid = %s WHERE userid = %s"
        val = (uid, userid)
        mycursor.execute(sql,val)
        mydb.commit()
        embed = discord.Embed(
                          description=":white_check_mark:  Your UID has been edited to " + uid,
                          colour=0x00b0f4
                          )
        discordavt=ctx.message.author.avatar
        embed.set_thumbnail(url=discordavt)
        embed.set_author(name="Configure: Genshin UID",
                     icon_url="https://i.imgur.com/T8KX9tC.jpg")

        embed.set_footer(text="Fley Discord Bot",
                     icon_url="https://i.imgur.com/T8KX9tC.jpg")
        await ctx.send(embed=embed)
bot.remove_command('help')

@bot.command()
async def help(ctx):
    await ctx.send('https://github.com/walshiiro/Flrey')
        
@bot.command()
async def char(ctx):
    await chardisplay.char(ctx)

TOKEN = ''
bot.run(TOKEN)