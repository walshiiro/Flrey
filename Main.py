
import discord
from discord import Intents, Client,User

from discord.ext import commands
import Paginator
import random

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
async def build(ctx,charnum):
    await genshin.charbuild.build(ctx,charnum)

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
    userdata = json.load(open('jsonfile/uidfromuser.json'))
    def write_json(new_data, filename='jsonfile/uidfromuser.json'):
        with open(filename,'r+') as file:
          # First we load existing data into a dict.
            file_data = json.load(file)
        # Join new_data with file_data inside emp_details
            file_data["userdata"].append(new_data)
        # Sets file's current position at offset.
            file.seek(0)
        # convert back to json.
            json.dump(file_data, file, indent = 2)

    datafilelength = len(userdata["userdata"])
    check=int(1)
    dataplace=int()
    for i in range(0,datafilelength):
        if(userdata["userdata"][i]["userid"] == userid):
            check=check+1
            dataplace=i
    if(check==1):
        data={
            "userid":userid,
            "useruid":uid
        }
        write_json(data)
        embed = discord.Embed(
                          description=":white_check_mark:  Your UID has been added to " + uid,
                          colour=0x00b0f4
                          )

        embed.set_author(name="Configure: Genshin UID",
                     icon_url="https://i.imgur.com/T8KX9tC.jpg")

        embed.set_footer(text="Fley Discord Bot",
                     icon_url="https://i.imgur.com/T8KX9tC.jpg")

        await ctx.send(embed=embed)
    else:
        with open('jsonfile/uidfromuser.json','r') as file:
            data = json.load(file)
        del data["userdata"][dataplace]
        with open('jsonfile/uidfromuser.json', 'w') as file:
            json.dump(data, file, indent=2)
        data1={
            "userid":userid,
            "useruid":uid
            }   
        write_json(data1)
        embed = discord.Embed(
                          description=":white_check_mark:  Your UID has been edited to " + uid,
                          colour=0x00b0f4
                          )

        embed.set_author(name="Configure: Genshin UID",
                     icon_url="https://i.imgur.com/T8KX9tC.jpg")

        embed.set_footer(text="Fley Discord Bot",
                     icon_url="https://i.imgur.com/T8KX9tC.jpg")
        await ctx.send(embed=embed)
        
@bot.command()
async def char(ctx):
    await chardisplay.char(ctx)

TOKEN = ''
bot.run(TOKEN)