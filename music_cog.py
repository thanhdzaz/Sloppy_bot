import discord
from gtts import gTTS
from discord.ext import commands
import time
import os

from youtube_dl import YoutubeDL

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
        #all the music related stuff
        self.is_playing = False

        # 2d array containing [song, channel]
        self.music_queue = []
        self.YDL_OPTIONS = {
          'format': 'bestaudio',
          'extractaudio': True,
          'audioformat': 'mp3',
          'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
          'restrictfilenames': True,
          'nocheckcertificate': True,
          'quiet': True,
          'no_warnings': True,
          'default_search': 'auto',
          'source_address': '0.0.0.0',}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        self.vc = ""

     #searching the item on youtube
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try: 
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception: 
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            #get the first url
            m_url = self.music_queue[0][0]['source']

            #remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    # infinite loop checking 
    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']
            
            #try to connect to voice channel if you are not already connected

            if self.vc == "" or not self.vc.is_connected() or self.vc == None:
                self.vc = await self.music_queue[0][1].connect()
            else:
                await self.vc.move_to(self.music_queue[0][1])
            
            print(self.music_queue)
            #remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    @commands.command(name="n", help="Gọi nhạc từ Youtube")
    async def n(self, ctx, *args):
        query = " ".join(args)
        
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            #you need to be connected so that the bot knows where to go
            await ctx.send(f"Vào kênh voice nào đó ngồi rồi hãy gọi tôi nhé {ctx.author}")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("Ơ méo tìm được bài này thử bài khác đi.")
            else:
                await ctx.send(f"```Thêm {query} vào hàng đợi thành công```")
                self.music_queue.append([song, voice_channel])
                
                if self.is_playing == False:
                    await self.play_music()

    @commands.command(name="ds", help="Hiển thị danh sách hiện tại")
    async def ds(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += self.music_queue[i][0]['title'] + "\n"

        print(retval)
        if retval != "":
            await ctx.send(f"```{retval}```")
        else:
            await ctx.send("```Không có gì trong hàng đợi.```")

    @commands.command(name="next", help="Next bài")
    async def next(self, ctx):
        if self.vc != "" and self.vc:
            self.vc.stop()
            #try to play next in the queue if it exists
            await self.play_music()
    @commands.command(name="dung", help="Next bài")
    async def pause(self, ctx):
        if self.vc != "" and self.vc:
            self.vc.pause()
            emoji = discord.utils.get(ctx.guild.emojis, name="ok_hand")
            await ctx.message.add_reaction(emoji)
            #try to play next in the queue if it exists
            # await self.play_music()
    @commands.command(name="tiep", help="Next bài")
    async def tiep(self, ctx):
        if self.vc != "" and self.vc:
            self.vc.resume()
            emoji = discord.utils.get(ctx.guild.emojis, name="ok_hand")
            await ctx.message.add_reaction(emoji)
            #try to play next in the queue if it exists
            # await self.play_music()
    @commands.command(name="ra", help="Next bài")
    async def leave(self,ctx):
        emoji = discord.utils.get(ctx.guild.emojis, name="EnpKypPWEAERxi8")
        await ctx.message.add_reaction(emoji)
        await ctx.voice_client.disconnect()
    @commands.command(name="vao", help="Next bài")
    async def join(self,ctx):
        channel = ctx.author.voice.channel
        emoji = discord.utils.get(ctx.guild.emojis, name="FischlDab")
        await ctx.message.add_reaction(emoji)
        self.vc = await channel.connect()

    @commands.command(name='noi',pass_context=True)
    async def devl(self,ctx, *, request):
        # channel = ctx.author.voice.channel
        channel = ctx.author.voice.channel
        if not channel:

            await ctx.send('Vào 1 kênh để gọi lệnh nha !!')
            return
        else:
            if os.path.exists(f"./music/{request}.mp3"):
              emoji = discord.utils.get(ctx.guild.emojis,name="Tom_and_Jerry_meme")
              await ctx.message.add_reaction(emoji)
              if self.vc == "" or not self.vc.is_connected() or self.vc == None:
                self.vc = await channel.connect()
                self.vc.play(discord.FFmpegPCMAudio(f"./music/{request}.mp3"), after=lambda e: print('done'))
              else:
                await self.vc.play(discord.FFmpegPCMAudio(f"./music/{request}.mp3"), after=lambda e: print('done'))
            elif request == '-all':
              await ctx.send('***Danh sách***```70tuoi, ban, bopdi, camgiac, cay, devl, locc, dcm, que, tobecontinue, cekt, thamlam, ngudot, concainit, zo, votay, deo, emoi, bmsq, haha, aotuong, diena, tinchu, vcl, yeuvoiduong, metrai, diachi, diachi2, doicc , immom, anhbana, oibanoi, khonglam, lay, nhatban, trandan, aothat, meomeo, ngu, xinloi, vinhbiet, bocphet, onichan, ehe, yamete, uwu, nghien, squid, hentai, contrai, o, ham, khoai, ragiday, 10d, mau, 26, conginuadau, kinh  ```')
            else:
              emoji = discord.utils.get(ctx.guild.emojis,name="Tom_and_Jerry_meme")
              await ctx.message.add_reaction(emoji)
              await ctx.send(f'Ơ kìa cái {request} này không tồn tại hãy sử dụng lệnh ```>noi -all``` để nhận danh sách')


    @commands.command(name='t',pass_context=True)
    async def t(self,ctx, *, request):
        user_channel = ctx.message.author.voice.channel
        print(user_channel)
        if(ctx.bot.voice_clients != []):
          bot_channel =   ctx.bot.voice_clients[0].channel
          print(bot_channel)
        emoji = discord.utils.get(ctx.guild.emojis, name="BarbaraLove")
        await ctx.message.add_reaction(emoji)
        global gTTS
        speech = gTTS(text = request, lang = 'vi', slow=False)
        speech.save('audio.mp3')
        channel = ctx.author.voice.channel
        
        if self.vc == "" or not self.vc.is_connected() or self.vc == None:
            self.vc = await channel.connect()
            self.vc.play(discord.FFmpegPCMAudio('audio.mp3'), after=lambda e: print('done'))
           
        else:
            if channel and user_channel == bot_channel:
              await self.vc.play(discord.FFmpegPCMAudio('audio.mp3'), after=lambda e: print('done'))
            else:
              await ctx.send(f'Bot đang chỗ khác kênh `{bot_channel}`')
        
