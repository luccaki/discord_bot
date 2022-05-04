#kill 1 - para resetar o replit
#pip install pynacl
import os
from discord.ext import commands
import discord
import random
import pafy

client = discord.Client()
        
#@client.command()
#async def yt(ctx, url = "lxl388vKUmE"):
#  #If you want to use a youtube URL
#  if "/watch?v=" in url:
#    url = url[(url.index('/watch?v=')+9):(url.index('/watch?v=')+20)]
#  elif "youtu.be/" in url:
#    url = url[(url.index('youtu.be/')+9):(url.index('youtu.be/')+20)]
#  else:
#    url = "lxl388vKUmE"
#
#  #If you want to use a file
#  #url = "audio.mp3"
#  
#  guild = ctx.guild
#  song = pafy.new(url)
#  audio = song.getbestaudio()
#  audio_source = discord.FFmpegPCMAudio(audio.url)
#  #audio_source = discord.FFmpegPCMAudio('vuvuzela.mp3')
#  vc = ctx.message.author.voice.channel
#  voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
#  if voice_client == None:
#    await vc.connect()
#    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
#  elif vc != voice_client.channel:
#    await voice_client.move_to(vc)
#    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
#  if not voice_client.is_playing():
#    voice_client.play(audio_source, after=None)
#  else:
#    voice_client.stop()

#@client.command(name='$p')
#async def pokemonMiranha(ctx):
#  if(ctx.author.id == 312555845286363136):
#    await ctx.send("**SAI DO VÍCIO MIRANHA!**")
#    await ctx.send(file=discord.File('charas.png'))

#@client.command(name='')
#async def t(ctx):
#  await ctx.message.delete()
#  await ctx.send("**TESTE!**")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.mention_everyone:
    await message.delete()
    await message.channel.send("**PRIMATA!**")

  elif 840953718312009739 in message.raw_mentions:
    if "?" in message.content:
      await message.channel.send("**CALA BOCA PRIMATA!**")
    else:
      await message.channel.send("**PRIMATA!**")

  #elif message.author.id == 689976497364271205:
  #  await message.delete()

  elif "F" == message.content.upper():
    await message.channel.send(file=discord.File('F.jpg'))

  elif "HAMERTI" == message.content.upper():
    await message.channel.send(file=discord.File('hamerti.jpg'))
    #voice = await message.author.voice.channel.connect()
    #voice.play("https://www.youtube.com/watch?v=RrZt1FGV8vQ")

  #elif message.author.id == 312555845286363136:
  #  if "$P" in message.content.upper():
  #    await message.channel.send("**SAI DO VÍCIO MIRANHA!**")
  #    if (random.randrange(2) == 1):
  #      await message.channel.send(file=discord.File('charas.png'))
  #    else:
  #      await message.channel.send(file=discord.File('charas_do_miranha.gif'))
      
  elif message.author.id == 663487700728283176:
    if message.content.startswith("teste"):
      await message.author.send("I'm alive")
      print("funcionando")
  
  elif message.author.id == 594304718382170112:
    if "amouranth" in message.content:
      await message.author.send("Sai do Vicio Rapha")

  #elif message.author.id == 689976497364271205:
  #  await message.author.edit(nick = message.content)

  #if message.author.id == 332525747749257216:
  #  await message.channel.send("**PRIMATA!**")
     
client.run(os.environ.get('TOKEN'))