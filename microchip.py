import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
  
Client = discord.Client()
bot_prefix= "m>"
client = commands.Bot(command_prefix=bot_prefix)
  
@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    #Extra 1
    await client.change_presence(game=discord.Game(name='as a bot!'))
  


  

  

  

  


#command7
@client.command(pass_context = True)
async def pwn(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return
 
    if not member:
        return await client.say(ctx.message.author.mention + "tell me who to kick")
    try:
        await client.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: privilege too low!")
 
    embed = discord.Embed(description = "i pwned **%s** !"%member.name, color = 0xFF0000)
    return await client.say(embed = embed)
 

#command9
@client.command(pass_context = True)
async def info(ctx):
    await client.say("""hi, my name is microchip and i'm a discord bot coded by swoo32! type m>help for a list of commands!""")
 
       
client.run("MzU3Mjc1MzU0ODE1MjY2ODI2.DsuIkA.LsV76Xy3MYvA26zcFrUcKHcWbJA")
