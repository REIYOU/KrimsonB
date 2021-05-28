from datetime import date, datetime
from typing import Counter
import discord
from discord import activity
from discord import client
from discord import user
from discord.colour import Color
from discord.ext.commands import bot
from discord.ext.commands.errors import MissingPermissions
from discord.member import Member
from discord import Client
import requests
from discord import Webhook
from discord import AsyncWebhookAdapter
import asyncio
from io import BytesIO
import aiohttp
import random
from asyncio import sleep
import os
import datetime
from discord.ext import commands, tasks
from discord.utils import get 
import DiscordUtils
from AntiSpam import AntiSpamHandler
import aiofiles
import aiohttp
# invie logging
invites = {}
last = ""
#  initializing the bot 
intents = discord.Intents.default()
intents.presences = True
intents.members = True
client = commands.Bot(command_prefix=">>",intents=intents)
client.remove_command("help")
client.load_extension('cogs.fun')

client.warnings = {} # guild_id : {member_id: [count, [(admin_id, reason)]]}
    
# help command 
@client.group(invoke_without_command=True)
async def help(ctx):
    m = discord.Embed(title="**HELP**",description="*Use >>help <command> for extended info*")
    m.add_field(name="**MODERATION**", value="`ban ,  unban , mute , unmute , idunban , kick , purge , warns , warnings`",inline=False)
    m.add_field(name="**SERVER MANAGEMENT**", value="`ccr , creemo , delemo , delccr , lockdown , unlock`", inline=False)
    m.add_field(name="**MISC**",value="`snipe , avatar , ping , remind , userinfo , serverinfo , clone , chnick , announce`", inline=False)
    m.add_field(name="FUN", value="`meme , help (this command)`")
    m.set_footer(text=f"Requested by {ctx.author.display_name}")
    await ctx.send(embed=m)
'''MISC'''
@help.command()
async def snipe(ctx):
    em = discord.Embed(title= "**snipe**", description="`snipes the deleted message`")
    em.add_field(name="`SYNTAX`",value="*>>snipe*",inline=False)
    await ctx.send(embed=em)

@help.command()
async def avatar(ctx):
    em = discord.Embed(title= "**avatar**", description="`Shows user avatar`")
    em.add_field(name="`SYNTAX`",value="*>>avatar (user)*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def ping(ctx):
    em = discord.Embed(title= "**ping**", description="`Shows bot latency`")
    em.add_field(name="`SYNTAX`",value="*>>ping*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def remind(ctx):
    em = discord.Embed(title= "**remind**", description="`set a reminder`")
    em.add_field(name="`SYNTAX`",value="*>>remind <time '1s' '2m' '3h' <message>>*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def userinfo(ctx):
    em = discord.Embed(title= "**userinfo**", description="`shows userinfo`")
    em.add_field(name="`SYNTAX`",value="*>>userinfo <user>*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def serverinfo(ctx):
    em = discord.Embed(title= "**serverinfo**", description="`show's server info`")
    em.add_field(name="`SYNTAX`",value="*>>serverinfo*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def clone(ctx):
    em = discord.Embed(title= "**clone**", description="`clone's a user message`")
    em.add_field(name="`SYNTAX`",value="*>>clone@<usermention><message>*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def chnick(ctx):
    em = discord.Embed(title= "**chnick**", description="`changes the nickname`")
    em.add_field(name="`SYNTAX`",value="*>>chnick <nickname> <user>*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def announce(ctx):
    em = discord.Embed(title= "**announce**", description="`to make an announcement`")
    em.add_field(name="`SYNTAX`",value="*>>announce <@role> message*",inline=False)
    await ctx.send(embed=em)
''' Management '''
@help.command()
async def ccr(ctx):
    em = discord.Embed(title= "**CCR**", description="`Creates a channel`")
    em.add_field(name="`SYNTAX`",value="*>>ccr <amount of channel> name*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def creemo(ctx):
    em = discord.Embed(title= "**creemo**", description="`Creates an emoji`")
    em.add_field(name="`SYNTAX`",value="*>>creemo <emoji link> name*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def delemo(ctx):
    em = discord.Embed(title= "**delemo**", description="`Deletes an emoji`")
    em.add_field(name="`SYNTAX`",value="*>>delemo <emoji>*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def delccr(ctx):
    em = discord.Embed(title= "**delccr**", description="`Deletes a channel`")
    em.add_field(name="`SYNTAX`",value="*>>delccr <channel name/ID>*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def lockdown(ctx):
    em = discord.Embed(title= "**lockdown**", description="`Locks the current channel`")
    em.add_field(name="`SYNTAX`",value="*>>lockdown*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def unlock(ctx):
    em = discord.Embed(title= "**unlock**", description="`unlocks the channel`")
    em.add_field(name="`SYNTAX`",value="*>>unlock*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def meme(ctx):
    em = discord.Embed(title= "**meme**", description="`shows a meme`")
    em.add_field(name="`SYNTAX`",value="*>>meme*",inline=False)
    await ctx.send(embed=em)
''' Moderation'''
@help.command()
async def ban(ctx):
    em = discord.Embed(title= "**BAN**", description="`Permanently bans a member from the guild`")
    em.add_field(name="`SYNTAX`",value="*>>kick <member> Reason*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def unban(ctx):
    em = discord.Embed(title= "**UNBAN**", description="`Revokes the ban`")
    em.add_field(name="`SYNTAX`",value="*>>unban <member#tag>*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def mute(ctx):
    em = discord.Embed(title= "**Mute**", description="`Mutes a user`")
    em.add_field(name="`SYNTAX`",value="*>>mute <member> reason*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def unmute(ctx):
    em = discord.Embed(title= "**Mute**", description="`removes the mute from the  user`")
    em.add_field(name="`SYNTAX`",value="*>>unmute <member>*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def idunban(ctx):
    em = discord.Embed(title= "**idunban**", description="`Uses User ID to unban`")
    em.add_field(name="`SYNTAX`",value="*>>unban <member id>*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def kick(ctx):
    em = discord.Embed(title= "**Kick**", description="`Kicks a user`")
    em.add_field(name="`SYNTAX`",value="*>>kick <member> reason*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def purge(ctx):
    em = discord.Embed(title= "**Purge**", description="`Deletes the number of messages given`")
    em.add_field(name="`SYNTAX`",value="*>>purge <amount of msg>*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def warn(ctx):
    em = discord.Embed(title= "**warn**", description="`Warns a user`")
    em.add_field(name="`SYNTAX`",value="*>>warn <member> reason*",inline=False)
    await ctx.send(embed=em)
@help.command()
async def warnings(ctx):
    em = discord.Embed(title= "**warnings**", description="`gives the number of warnings`")
    em.add_field(name="`SYNTAX`",value="*>>warnings <member>*",inline=False)
    await ctx.send(embed=em)

#  fetch 
guild_id = 801577364471545896
logs_channel =847360793020596234
async def fetch():
    global last
    global invites
    await client.wait_until_ready()
    gld = client.get_guild(int(guild_id))
    logs = client.get_channel(int(logs_channel))
    while True:
        invs = await gld.invites()
        tmp = []
        for i in invs:
            for s in invites:
                if s[0] == i.code:
                    if int(i.uses) > s[1]:
                        usr = gld.get_member(int(last))
                        eme = discord.Embed(description="Just joined the server", color=0x03d692, title=" ")
                        eme.set_author(name=usr.name + "#" + usr.discriminator, icon_url=usr.avatar_url)
                        eme.set_footer(text="ID: " + str(usr.id))
                        eme.timestamp = usr.joined_at
                        eme.add_field(name="Used invite",
                                      value="Inviter: " + i.inviter.mention + " (`" + i.inviter.name + "#" + i.inviter.discriminator + "` | `" + str(i.inviter.id) + "`)\nCode: `" + i.code + "`\nUses: `" + str(
                                          i.uses) + "`", inline=False)
                        await logs.send(embed=eme)
            tmp.append(tuple((i.code, i.uses)))
        invites = tmp
        await asyncio.sleep(4)
@client.event
async def on_member_join(meme):
    global last
    last = str(meme.id)




# client event
@client.event
async def on_ready():
    for guild in client.guilds:
        client.warnings[guild.id] = {}
        
        async with aiofiles.open(f"{guild.id}.txt", mode="a") as temp:
            pass

        async with aiofiles.open(f"{guild.id}.txt", mode="r") as file:
            lines = await file.readlines()

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                reason = " ".join(data[2:]).strip("\n")

                try:
                    client.warnings[guild.id][member_id][0] += 1
                    client.warnings[guild.id][member_id][1].append((admin_id, reason))

                except KeyError:
                    client.warnings[guild.id][member_id] = [1, [(admin_id, reason)]] 
    
    print(client.user.name + " is ready.")






@client.event
async def on_guild_join(guild):
    client.warnings[guild.id] = {}
@client.event
async def on_member_remove(member):
	for channel in member.guild.channels: 
		if channel.name.startswith('Member'):
			await channel.edit(name=f'Members: {member.guild.member_count}')
			break




@client.event 
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="𝖂𝖊𝖑𝖈𝖔𝖒𝖊⛓")
    discord_em = discord.Embed(title=f"hey! {member.name}!! Welcome to 𝔎𝔯𝔦𝔪𝔰𝔬𝔫 𝔇𝔲𝔫𝔤𝔢𝔬𝔫",color=0x4169E1)
    discord_em.set_image(url="https://images-ext-1.discordapp.net/external/7tQpH4cLGODb0hgXSHzpm6gjr6jBPrPNv_wJsYpU6wA/https/cdn.mee6.xyz/guild-images/801577364471545896/94d5f0df1f34ed56f411cb7ff3f15fbc930849deff7a0d2d8a9259fc419d1e10.jpeg?width=454&height=597")
    await channel.send(embed=discord_em)
    role = discord.utils.get(member.guild.roles,name="𝓢𝓵𝓪𝓿𝓮𝓼")
    await member.add_roles(role)
@client.event 
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="𝕲𝖔𝖔𝖉𝖇𝖞𝖊⛓")
    discord_em = discord.Embed(title=f"WOW {member.name} We are sad that you left",color=0xDC143C)
    discord_em.set_image(url="https://images-ext-1.discordapp.net/external/7tQpH4cLGODb0hgXSHzpm6gjr6jBPrPNv_wJsYpU6wA/https/cdn.mee6.xyz/guild-images/801577364471545896/94d5f0df1f34ed56f411cb7ff3f15fbc930849deff7a0d2d8a9259fc419d1e10.jpeg?width=454&height=597")
    await channel.send(embed=discord_em)
    role = discord.utils.get(member.guild.roles,name="𝓢𝓵𝓪𝓿𝓮𝓼")
    await member.add_roles(role)





# auto mod 
filtered_words = ["nigger",'kkk','hitler']
@client.event
async def on_message(msg):
    
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()

    
    await client.process_commands(msg)
''' welcome '''
client.handler = AntiSpamHandler(client)






@client.event
async def on_message(message):
    await  client.handler.propagate(message)
    await  client.process_commands(message)
    
    
''' end'''





# ping command
@client.command()
async def ping(ctx,arg=None):
    url = ctx.author.avatar_url
    embed = discord.Embed(title=f"Ping! The server ping is {round(client.latency*1000)}")
   
    embed.set_thumbnail(url=url)
    embed.set_footer(text=f"Requested by {ctx.author}")
    await ctx.send(embed=embed)
# clone 



url = f'https://discord.com/api/webhooks/847683665202380810/eOzUMvmfA7uRBW32zgeZrhcwCc0Dl3VejtF9jmWLJ_CtmS2c8Nc0R9MYfo_oGe_-Vv1H'

@client.command()
async def clone(ctx, member : discord.Member,* , arg):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(
            f'https://discord.com/api/webhooks/847683665202380810/eOzUMvmfA7uRBW32zgeZrhcwCc0Dl3VejtF9jmWLJ_CtmS2c8Nc0R9MYfo_oGe_-Vv1H', adapter=AsyncWebhookAdapter(session))
        await webhook.send(f"{arg}", 
        username=f"{member.display_name}",
         avatar_url=f"{member.avatar_url}"
        )



#  Userinfo command 
@client.command()
async def userinfo(ctx, member: discord.Member):

    roles= [role for role in member.roles]
    user = member
    mbed= discord.Embed(title="Userinfo", description=f"here is the info for {user}", color=user.colour)
    mbed.set_author(name=f"UserInfo {member}")
    mbed.set_thumbnail(url=user.avatar_url)
    mbed.set_footer(text=f"requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    mbed.add_field(name="NAME", value=user.name,inline=True)
    mbed.add_field(name="NICKNAME", value=user.nick,inline=True)
    mbed.add_field(name="ID:", value=user.id,inline=True)
    mbed.add_field(name="STATUS", value=user.status,inline=True)
    mbed.add_field(name="TOP ROLE", value=user.top_role.name,inline=True)
    mbed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=True)
    mbed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=True)
    mbed.add_field(name=f"Roles ({len(roles)})", value=",".join([role.mention for role in roles]),inline=True)
    mbed.add_field(name="Is a bot?", value=member.bot,inline=True)
    await ctx.send(embed=mbed)





# server info 
@client.command()
async def serverinfo(ctx):
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + "Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    # embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Verification level", value=str(ctx.guild.verification_level),inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    embed.add_field(name="Bots", value=','.join(list_of_bots),inline=True)
    embed.add_field(name="Created at", value=str(ctx.guild.created_at),inline=True)
    await ctx.send(embed=embed)




#  purge 
@client.command(name="purge")
async def purge(ctx,amount,arg:str=None):
    await ctx.message.delete()
    await ctx.channel.purge(limit=int(amount))
    message_to_delete = await ctx.send(f'{amount} of messages have been deleted')
    await asyncio.sleep(1)
    await message_to_delete.delete()
@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("***You Do Not Have Permissions To use this Command!***")
    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("***Please make sure to input how many messages you want to delete***")





#  lockdown and unlock command 
@client.command()
@commands.has_permissions(manage_channels= True)
async def lockdown(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    embed = discord.Embed(title=f"The channel is now in lockdown")
    await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(manage_channels= True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    embed = discord.Embed(title=f"The channel is now unlocked")
    await ctx.send(embed=embed)






# ban unban and kick 
@client.command(name="kick",help="kicks a member")
async def kick(ctx,member: discord.Member,*, reason=None):
    await ctx.message.delete()
    await member.kick(reason=reason)
    mbed = discord.Embed(title=f"Kicked {member} for {reason}")
    await ctx.send(embed=mbed)

@client.command(name="ban",help="bans a member")
async def ban(ctx,member:discord.Member,*, reason=None):
    await ctx.message.delete()
    await member.ban(reason=reason)
    mbed = discord.Embed(title=f"Banned {member} for {reason}")
    await ctx.send(embed=mbed)
@client.command()
async def unban(ctx,*,member):
    banned_user = await ctx.guild.bans()
    member_name, member_discrim = member.split('#')

    for ban_entry in banned_user:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discrim):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return
@client.command()
async def idunban(ctx,user:discord.User):
    guild = ctx.guild
    mbed = discord.Embed(
        title="Sucess!",
        description=f"Unbanned {user}"
    )
    if ctx.author.guild_permissions.ban_members:
        await ctx.send(embed=mbed)
        await guild.unban(user=user)




# mute and unmute 
@client.command()
async def mute(ctx, member: discord.Member,* , reason=None):
    guild = ctx.message.guild
    mutedRole = discord.utils.get(guild.roles,name="muted")
    if not mutedRole:
        mutedRole = await guild.create_role(name="muted")
    for channel in guild.channels:
        await channel.set_permissions(mutedRole, speak=False,send_messages=False,read_message_history=True,read_messages=False)

    await member.add_roles(mutedRole,reason=reason)
    embed = discord.Embed(title="Muted",description=f"{member} was muted for{reason}")
    await ctx.send(embed=embed)
    await member.send(f"You were muted in {guild.name} for  {reason}")
@client.command(name="unmute", help="UnMute's a user")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    guild = ctx.message.guild
    mutedRole = discord.utils.get(ctx.guild.roles,name="muted")

    await member.remove_roles(mutedRole)
    embed = discord.Embed(title="Unmuted",description=f"{member} was unmuted")
    await ctx.send(embed=embed)
    await member.send(f"You were Unmuted in {guild.name}")



    
# avatar 
@client.command(name="avatar",help="show's user avatar")
async def avatar(ctx, user: discord.Member):
    await ctx.message.delete()
    mbed = discord.Embed(
    color = discord.Color(0xffff),
    title=f"{user}'s avatar"
    )
    mbed.set_image(url=f"{user.avatar_url}")
    await ctx.send(embed=mbed)
@avatar.error
async def av_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        mbed = discord.Embed(
            color = discord.Color(0xffff),
            title=f"{ctx.author}'s avatar"
            )
    mbed.set_image(url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=mbed)




# announce 
@commands.has_permissions(administrator=True)
@client.command()
async def announce(ctx, role: discord.Role, *, msg): # announces to the specified role
    global members
    members = [m for m in ctx.guild.members if role in m.roles]
    for m in members:
        try:
            await m.send(msg)
            await ctx.send(f":white_check_mark: Message sent to {m}")
        except:
            await ctx.send(f":x: No DM could be sent to {m}")
    await ctx.send("Done!")
@announce.error
async def _announcement_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(":x: Role couldn't be found!")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f":x: {ctx.author.mention}, you don't have sufficient permissions.")
    else:
        await ctx.send(error)





@client.command()
async def creemo(ctx, url: str, *, name):
	guild = ctx.guild
	if ctx.author.guild_permissions.manage_emojis:
		async with aiohttp.ClientSession() as ses:
			async with ses.get(url) as r:
				
				try:
					img_or_gif = BytesIO(await r.read())
					b_value = img_or_gif.getvalue()
					if r.status in range(200, 299):
						emoji = await guild.create_custom_emoji(image=b_value, name=name)
						await ctx.send(f'Successfully created emoji: <:{name}:{emoji.id}>')
						await ses.close()
					else:
						await ctx.send(f'Error when making request | {r.status} response.')
						await ses.close()
						
				except discord.HTTPException:
					await ctx.send('File size is too big!')






@client.command()
async def delemo(ctx, emoji: discord.Emoji):
	guild = ctx.guild
	if ctx.author.guild_permissions.manage_emojis:
		await ctx.send(f'Successfully deleted (or not): {emoji}')
		await emoji.delete()




@client.command()
async def remind(ctx,time,*,task):
    def convert(time):
        pos = ['s', 'm', 'h', 'd']

        time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2
 
        return val * time_dict[unit]
    converted_time = convert(time)
    if converted_time == -1:
        await ctx.send("***TIME IS INCORRECT***")
        return
    if converted_time == -2:
        await ctx.send("**TIME MUST BE AN INTEGER**")
        return
    await ctx.send(f"Started reminder for **{task}** and will last **{time}**")
    await asyncio.sleep(converted_time)
    await ctx.send(f"{ctx.author.mention}your reminder for **{task}** has finished!")





@client.command(pass_context=True, name="chnick",help="changes nickname")
async def chnick(ctx,member: discord.Member,*,nick):
    await ctx.message.delete()
    em = discord.Embed(title=f"{member.display_name} has been changed to {nick}")
    await ctx.send(embed=em)
    await member.edit(nick=nick)





@client.command(pass_context = True, name="ccr",help="creates channels")
async def ccr(ctx, amount:int,*,channel_name):
    guild = ctx.message.guild
    await ctx.message.delete()
    for i in range(amount):
        await guild.create_text_channel(channel_name)




@client.command(name="deletechannel",help="deletes a particular channel")
async def delccr(ctx, channel: discord.TextChannel):
    guild = ctx.message.guild
    chname = str(channel)
    await ctx.message.delete()
    _embed = discord.Embed(
        title = "Channel deleted",
        description = f"channel: {channel} has been deleted"
    )
    await ctx.send(embed=_embed)
    await channel.delete()


# snipe command 



snipe_message_content = None
snipe_message_author = None
@client.event
async def on_message_delete(message):
    global snipe_message_content
    global snipe_message_author

    snipe_message_content = message.content
    snipe_message_author = message.author.name
    await sleep(60)
    snipe_message_author = None
    snipe_message_content = None
@client.command()
async def  snipe(message):
    bed= discord.Embed(title="Nothing found to snipe in this channel !")
    if snipe_message_content==None:
        await message.channel.send(embed=bed)
    else:
        embed= discord.Embed(description=f"{snipe_message_content}")
        # embed.set_thumbnail(snipe_message_author.avatar_url)
        embed.set_footer(text=f"Requested by {message.author.name}#{message.author.discriminator}")
        embed.set_author(name=f"Sniped the message deleted by {snipe_message_author}")
        await message.channel.send(embed=embed)
        return




@client.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member: discord.Member=None, *, reason=None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")
        
    if reason is None:
        return await ctx.send("Please provide a reason for warning this user.")

    try:
        first_warning = False
        client.warnings[ctx.guild.id][member.id][0] += 1
        client.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

    except KeyError:
        first_warning = True
        client.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

    count = client.warnings[ctx.guild.id][member.id][0]

    async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
        await file.write(f"{member.id} {ctx.author.id} {reason}\n")

    await ctx.send(f"{member.mention} has {count} {'warning' if first_warning else 'warnings'}.")

@client.command()
@commands.has_permissions(administrator=True)
async def warnings(ctx, member: discord.Member=None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")
    
    embed = discord.Embed(title=f"Displaying Warnings for {member.name}", description="", colour=discord.Colour.red())
    try:
        i = 1
        for admin_id, reason in client.warnings[ctx.guild.id][member.id][1]:
            admin = ctx.guild.get_member(admin_id)
            embed.description += f"**Warning {i}** given by: {admin.mention} for: *'{reason}'*.\n"
            i += 1

        await ctx.send(embed=embed)

    except KeyError: # no warnings
        await ctx.send("This user has no warnings.")





token= "ODQ3MDE2OTUxNTY2MDQxMDk4.YK38Ag.qqPQ6rNshEQXIg5nNqq7jla6nUI"
client.run(token)   
