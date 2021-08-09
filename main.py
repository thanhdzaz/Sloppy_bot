
import discord
from discord.ext import commands
from alive import Alive
import os
import asyncio
#import all of the cogs
from main_cog import main_cog
from text_cog import text_cog
from music_cog import music_cog

async def status_task():
  while True:
      await asyncio.sleep(10)# 10 as in 10seconds
      await bot.change_presence(activity=discord.Game(name="Vợ Long"))
      await asyncio.sleep(10)# 10 as in 10seconds
      await bot.change_presence(activity=discord.Game(name="Vợ Khánh"))
      await asyncio.sleep(10)# 10 as in 10seconds
      await bot.change_presence(activity=discord.Game(name="Vợ An"))
      await asyncio.sleep(10)# 10 as in 10seconds
      await bot.change_presence(activity=discord.Game(name="Vợ Been"))
      await asyncio.sleep(10)# 10 as in 10seconds
      await bot.change_presence(activity=discord.Game(name="Vợ Cường"))
      # await asyncio.sleep(10)
      # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=f"competing status"))
      # await asyncio.sleep(10)
      # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f"streaming status"))
      # await asyncio.sleep(10)

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
  # await bot.change_presence(status=discord.Status.idle,activity=discord.Game('Đợi >'))
  bot.loop.create_task(status_task())
  print('ahahhhh vào rồi!!!')

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(main_cog(bot))
bot.add_cog(text_cog(bot))
bot.add_cog(music_cog(bot))

#start the bot with our token
Alive()
bot.run(os.getenv('token'))

