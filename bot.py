import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
    print ("Ready")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def memz(ctx):
    await bot.say("Memz is over rated")

@bot.command(pass_context=True)
async def matt(ctx):
    await bot.say("Sub to matt!")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: Pong!")

@bot.command(pass_context=True)
async def Donald(ctx):
    await bot.say("https://pbs.twimg.com/profile_images/874276197357596672/kUuht00m_400x400.jpg")

@bot.command(pass_context=True)
async def Kjinj(ctx):
    await bot.say("https://www.youtube.com/channel/UCArfR3cZ7y0x_MqaXxqyQvA/featured?view_as=subscriber")

bot.run("NDAyNzY4ODgyNTA4NzU5MDUx.DT9nng.Vo5xKblviL3nqIXmqdS9d1xTLUc")

