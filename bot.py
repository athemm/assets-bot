import discord
from discord.ext.commands import Bot
import io
import aiohttp
import asyncio
import shutil
from discord.ext import commands
import os
import time
import requests
from PIL import Image  
import PIL  
import sys
import lzma
import struct
import random
import binascii
import platform
import sce
import csv
from zipfile import ZipFile
from sce import enco
from DataBase import Version
from BytesWorker import *
from PIL import Image
import scd
from os import path
from scd import wholex
bot = commands.Bot(command_prefix='!')
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Working on {0.user}'.format(client))

prefixn = "!sc "
helpg = "!"
prefix = "!texture "
bann = "assets bot please ban him"


def writedb(sentu):
    data = open("DB//database.csv", "r+")
    reader = csv.reader(data)
    writer = csv.writer(data)
    for row in reader:
        if sentu in row[0]:
            pass
        else:
            writer.writerow([sentu])

@client.event





async def on_message(message): 




    if message.author == client.user:
        return
    if message.author.bot == True:
        return

    if message.content.startswith("good talk"):
        await message.channel.send("good talk indeed")


    if message.content.startswith(helpg + "info"):
        await message.channel.send("The <@704088993569964103> is a bot that can give you textures of brawlers, decompress _tex.sc files or convert your obj to scw files")

    if message.content.startswith(helpg + "help"):
        await message.channel.send("available commands: **!info"" for info  \n**!texture help**\n-!texture [brawler]\n**!sc decode(attach _tex.sc file)\n **!obj2scw [obj attachment]** converts your obj to scw file \n**FUN** \n---------\n**!inspirobot** returns a random inspirobot generated image!")

    if message.content.startswith(prefix + "list"):
        await message.channel.send('Supported Brawlers: bea, 8bit, bibi, \nbarley, bo, brock, \nbull, carl, colt, \ncrow, darryl, dynamike, dynamikered, \nfrank, gene, jacky, \nleon, penny, max, \nmortis, mortos, nita, pam, piper, poco,\nshelly,tara,sprout')

    if message.content.startswith(prefix + "help"):
        await message.channel.send("use !texture [brawler] and !texture list to get a list of supported brawlers")

    if message.content.startswith(helpg + "invite"):
        await message.channel.send("You can invite me to your server with: https://bit.ly/3eYGz6g ")


    if message.content.startswith(prefix + "bea"):
        await message.channel.send(file=discord.File('tex//bea_tex.png'))

    if message.content.startswith("!inspirobot"):
        site = requests.get('https://inspirobot.me/api?generate=true', stream=True)
        cont = site.content
        contd = cont.decode("utf-8")
        await message.channel.send(requests.get('https://inspirobot.me/api?generate=true', stream=True).content.decode("utf-8")) 



    if message.content.startswith(prefix + "8bit"):
        await message.channel.send(file=discord.File('tex//8bit_tex.png'))
        await message.channel.send('and turret:')
        await message.channel.send(file=discord.File('tex//8bitulti_tex.png'))

    if message.content.startswith(prefix + "bibi"):
        await message.channel.send(file=discord.File('tex//bibi_tex.png'))
        
    if message.content.startswith(prefix + "barley"):
        await message.channel.send(file=discord.File('tex//barley_tex.png'))

    if message.content.startswith(prefix + "bo"):
        await message.channel.send(file=discord.File('tex//bo_tex.png'))
       
    if message.content.startswith(prefix + "brock"):
        await message.channel.send(file=discord.File('tex//brock_tex.png'))               

    if message.content.startswith(prefix + "bull"):
        await message.channel.send(file=discord.File('tex//bull_tex_01.png'))

    if message.content.startswith(prefix + "carl"):
        await message.channel.send(file=discord.File('tex//carl_tex.png'))        

    if message.content.startswith(prefix + "colt"):
        await message.channel.send(file=discord.File('tex//colt_tex.png'))

    if message.content.startswith(prefix + "crow"):
        await message.channel.send(file=discord.File('tex//crow_d_01.png'))

    if message.content.startswith(prefix + "darryl"):
        await message.channel.send(file=discord.File('tex//darryl_tex.png'))   

    if message.content.startswith(prefix + "dynamike"):
        await message.channel.send(file=discord.File('tex//dynamike_blue_tex.png'))  

    if message.content.startswith(prefix + "dynamikered"):
        await message.channel.send(file=discord.File('tex//dynamike_tex.png'))  

    if message.content.startswith(prefix + "emz"):
        await message.channel.send(file=discord.File('tex//emz_tex.png')) 

    if message.content.startswith(prefix + "frank"):
        await message.channel.send(file=discord.File('tex//frank_tex.png'))  

    if message.content.startswith(prefix + "gene"):
        await message.channel.send(file=discord.File('tex//gene_tex.png'))  

    if message.content.startswith(prefix + "jacky"):
        await message.channel.send(file=discord.File('tex//jacky_tex.png'))  

    if message.content.startswith(prefix + "leon"):
        await message.channel.send(file=discord.File('tex//leon_tex.png'))  

    if message.content.startswith(prefix + "penny"):
        await message.channel.send("Turret is included in this texture") 
        await message.channel.send(file=discord.File('tex//mari_tex.png'))  

    if message.content.startswith(prefix + "max"):
        await message.channel.send(file=discord.File('tex//max_tex.png'))  

    if message.content.startswith(prefix + "mortis"):
        await message.channel.send(file=discord.File('tex//mortis_v2_tex.png'))  
    if message.content.startswith(prefix + "mrp"):
        await message.channel.send(file=discord.File('tex//mrp_tex.png')) 
    if message.content.startswith(prefix + "mortos"):
        await message.channel.send(file=discord.File('tex//f10ed60.jpg'))  

    if message.content.startswith(prefix + "nita"):
        await message.channel.send(file=discord.File('tex//nita_tex.png'))  
        await message.channel.send("and bear:")  
        await message.channel.send(file=discord.File('tex//nita_bear_tex.png')) 

    if message.content.startswith(prefix + "pam"):
        await message.channel.send(file=discord.File('tex//pam_tex.png'))
        await message.channel.send("and station:")
        await message.channel.send(file=discord.File('tex//pamulti_tex.png'))
 
    if message.content.startswith(prefix + "piper"):
        await message.channel.send(file=discord.File('tex//piper_tex.png'))  

    if message.content.startswith(prefix + "poco"):
        await message.channel.send(file=discord.File('tex//poco_tex.png'))  

    if message.content.startswith(prefix + "primo"):
        await message.channel.send(file=discord.File('tex//primo_tex.png'))  

    if message.content.startswith(prefix + "ricochetnew"):
        await message.channel.send(file=discord.File('tex//rico_og_tex.png'))  

    if message.content.startswith(prefix + "rico"):
        await message.channel.send(file=discord.File('tex//rico_tex.png'))  

    if message.content.startswith(prefix + "rosa"):
        await message.channel.send(file=discord.File('tex//rosa_tex.png'))  

    if message.content.startswith(prefix + "sandy"):
        await message.channel.send(file=discord.File('tex//sandy_tex.png'))
    if message.content.startswith(prefix + "me"):
        user = message.guild.get_member(message.author.id)
        pfp = user.avatar_url
        await message.channel.send(pfp)

    if message.content.startswith(prefix + "scrappy"):
        await message.channel.send(file=discord.File('tex//scrappy.png'))  

    if message.content.startswith(prefix + "shelly"):
        await message.channel.send(file=discord.File('tex//shelly_v2_01.png'))  

    if message.content.startswith(prefix + "spike"):
        await message.channel.send(file=discord.File('tex//spike_tex.png'))  

    if message.content.startswith(prefix + "qwertyuıopğüasdfghjklşizxcvbnmöç"):
        await message.channel.send("fuck you retart")  

    if message.content.startswith(prefix + "sprout"):
        await message.channel.send(file=discord.File('tex//sprout_tex.png'))  

    if message.content.startswith(prefix + "tara"):
        await message.channel.send(file=discord.File('tex//tara_tex.png'))  

    if message.content.startswith(prefix + "tick"):
        await message.channel.send(file=discord.File('tex//tick_tex.png'))  

    if message.content.startswith(prefix + "gale"):
        await message.channel.send(file=discord.File('tex//gale_tex.png'))

    if message.content.startswith(prefix + "nani"):
        await message.channel.send(file=discord.File('tex//nani_tex.png'))

    if message.content.startswith(prefixn + "decode"):
        filee = "tmp_tex.sc"
        if len(message.attachments) == 0:
            await message.channel.send("attach a _tex.sc file please")    
        await message.attachments[0].save(filee, seek_begin=True, use_cached=False)
        sentu = message.author.id

        shutil.move("/Users/Asus/Desktop/jm/2/" + filee, "/Users/Asus/Desktop/jm/2/In-Compressed-SC/" + filee)
        await message.channel.send("processing... this may take some time")
        scd.wholex()
        #os.system("python SC-Decode.py")
        dier = "C:/Users/Asus/Desktop/jm/2/Out-Decompressed-SC/tmp_tex"
        writedb(sentu = str(message.author.id))
        for filename in os.listdir(dier):
            await message.channel.send(file=discord.File(os.path.join(dier, filename)))

    if message.content.startswith(bann):
        await message.channel.send("no lol")


    if message.content.startswith(helpg + "obj2scw"):
     if len(message.attachments) == 0:
      await message.channel.send("attach an obj file please")    

     await message.channel.send("*This tool was made by Garlfin. Link to the tool: github.com/garlfin/obj2scw\nCopyright notice: Copyright 2020 Garlfin, Some Rights Reserved. Licenced under CC BY-SA 4.0 licence*")
     await message.attachments[0].save("output.obj", seek_begin=True, use_cached=False)
     shutil.move("/Users/Asus/Desktop/jm/2/output.obj", "/Users/Asus/Desktop/jm/2/obj/output.obj")
     await message.channel.send("**processing... this may take some time**")
     try:
         os.system("python convert.py")
         await message.channel.send(file=discord.File('scw//output.scw'))
         await message.channel.send("you must remove the animations in animations.csv before putting this in-game")
         os.remove("C://Users//Asus//Desktop//jm//2//scw//output.scw")
     except:
         await message.channel.send("done")

    if message.content.startswith(prefixn + "encode"):
        if len(message.attachments) == 0:
            await message.channel.send("attach a zip file that contains directly accesible png files with their original sc names")          
        filenae = message.attachments[0].filename
        filenam = filenae.replace('.zip', '')
        andd = ".zip"
        if andd in filenam:
            filenam.replace(andd,' ')         
        await message.attachments[0].save(filenam, seek_begin=True, use_cached=False)
        await message.channel.send("**processing... this may take some time**")
        async def encodethis():
         path = os.getcwd() + "\\" + "In-Decompressed-SC" + "\\" + filenam
         with ZipFile(filenam, 'r') as zipObj:
          zipObj.extractall('In-Decompressed-SC/' + filenam)
          sce.enco()
         for filename in os.listdir("C:/Users/Asus/Desktop/jm/2/Out-Compressed-SC"):
          await message.channel.send(file=discord.File(os.path.join("C:/Users/Asus/Desktop/jm/2/Out-Compressed-SC", filename)))        
          await message.channel.send("done")
          time.sleep(4)
          os.remove(os.path.join("C:/Users/Asus/Desktop/jm/2/Out-Compressed-SC", filenam))
        await encodethis()
        
        
      #  if path.exists("C:/Users/Asus/Desktop/jm/2/In-Decompressed-SC/" + filenam + ".zip"):
     #    encodethis()
    #    else:
   #      os.mkdir("C:/Users/Asus/Desktop/jm/2/In-Decompressed-SC/" + filenam + ".zip")
    
       #encodethis()       
async def test(ctx, *, arg):
    await ctx.send(arg)

         
client.run('NzA0MDg4OTkzNTY5OTY0MTAz.XqYELQ.nxRJvpDqDE9Ota0iPINsfrs_tG8')
