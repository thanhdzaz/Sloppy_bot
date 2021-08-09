import discord
import random
from discord.ext import commands

class text_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      

    @commands.command(name="chui", help="chui chet me.")
    async def chui(self,ctx, *, member):
        chuithe = [
          'Đm thằng danh con này',
          'Ngu thì chết khóc lóc cái lồn',
          'Mày biết bố mày là ai không',
          'Ngu hết chỗ nói',
          'Ăn gì mà ngu thế'
          ]
        await ctx.send(f'{random.choice(chuithe)} {member}',tts=True)
