# import discord
# import os
# import requests
# import json

# client = discord.Client()

# def get_quote():
#   res = requests.get("https://zenquotes.io/api/random")
#   data = json.loads(res.text)
#   quote = data[0]['q']+ ' - ' + data[0]['a']
#   print (quote)
#   return (quote)

# @client.event
# async def on_ready(self):
#   print('ahihi đây rồi!!!',  self.user)

# @client.event
# async def on_message(message):
#   if message.author == client.user:
#     return
#   if message.content.startswith('^quote'):
#     qoute = get_quote()
#     await message.channel.send(qoute)
# client.run(os.getenv('token'))
from discord import FFmpegPCMAudio
from discord.utils import get
import random
import discord 
from discord.ext import commands
import os
from alive import Alive
client = commands.Bot(command_prefix='>')
@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle,activity=discord.Game('Đợi >'))
  print('ahahhhh vào rồi!!!')

@client.command()
async def ping(ctx):
    await ctx.send('pong')
@client.command()
async def helpq(ctx):
    await ctx.send('help cái bầu đuồi')

@client.command(pass_context=True)
async def join(ctx):
    # channel = ctx.message.author.voice.channel
    # await client.join_voice_channel(channel)
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    # source = FFmpegPCMAudio('1.m4a')
    # player = voice.play(source)

@client.command(pass_context = True)
async def leave(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()

    return await client.say("I am not connected to any voice channel on this server!")



@client.command()
async def chui(ctx, *, member):
    chuithe = ['Đm thằng danh con này','Ngu thì chết khóc lóc cái lồn','Mày biết bố mày là ai không']
    await ctx.send(f'{random.choice(chuithe)} {member}')

Alive()
client.run(os.getenv('token'))
