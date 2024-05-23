import discord
from discord import Intents, Client

from discord.ext import commands
from discord.ext.commands import bot
import Paginator

import requests
import json

async def invlink(ctx):
    await ctx.send('https://discord.com/oauth2/authorize?client_id=1239763299491381359')