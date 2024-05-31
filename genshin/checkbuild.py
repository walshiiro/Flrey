import discord
from discord import Intents, Client

from discord.ext import commands
from discord.ext.commands import bot
import Paginator

import requests
import json

async def build(ctx,uid,charnum1):
    check=1
    if(check==1):
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
                elif MainStats == 'FIGHT_PROP_WIND_ADD_HURT	':
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



                   
                
            

                     
                        


                