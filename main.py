
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
      await asyncio.sleep(3)# 3 as in 3seconds
      await bot.change_presence(activity=discord.Game(name="Vợ Been"))
      await asyncio.sleep(3)# 3 as in 3seconds
      await bot.change_presence(activity=discord.Game(name="Vợ Cường"))
      await asyncio.sleep(3)# 3 as in 3seconds
      await bot.change_presence(activity=discord.Game(name="Vợ Quân"))
      await asyncio.sleep(3)# 3 as in 3seconds
      await bot.change_presence(activity=discord.Game(name="Vợ Hải"))
      await asyncio.sleep(3)# 3 as in 3seconds
      await bot.change_presence(activity=discord.Game(name="Vợ Tài"))
      await asyncio.sleep(3)# 3 as in 3seconds
      await bot.change_presence(activity=discord.Game(name="Vợ Bi"))
      await asyncio.sleep(3)# 3 as in 3seconds
      await bot.change_presence(activity=discord.Game(name="Vợ Thắng"))
      await asyncio.sleep(3)# 3 as in 3seconds
      await bot.change_presence(activity=discord.Game(name="Vợ Shi"))

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
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

