import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
  

bot_prefix= "$"
client = commands.Bot(command_prefix=bot_prefix, case_insensitive=True)
TOKEN = '' #token goes here

# I want a custom help menu here
client.remove_command('help')

"""
TODO:
- Allow for aliases
"""
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
	if message.author == client.user:
		return

	await client.process_commands(message)
	
#to verify setup
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')


#displays info about this bot
@client.command()
async def about(ctx):
	embed = discord.Embed(title="About Ashe Bot", color=0x0098ff)
	
	embed.add_field(name="Version", value="1.0.0", inline=False)
	embed.add_field(name="Developer", value="Jack Bai", inline=False)
	embed.add_field(name="Source", value="https://github.com/bai-rongzhuo/ashe-bot", inline=False)

	await ctx.send(embed=embed)



#displays the current cait build; will be updated manually until I can hook this to the riot api
@client.command()
async def builds(ctx):
	embed = discord.Embed(title="Caitlyn Builds", description="Updated for Patch 8.17", color=0x0098ff)
	
	embed.add_field(name="Skill Order", value="R > W > Q > E or R > Q > W > E")
	embed.add_field(name="Runes", value="Precision primary, Sorcery secondary.", inline=False)
	embed.add_field(name="Precision", value="**LETHAL TEMPO**\nTriumph\nLegend: Bloodline / Legend: Alacrity\nCoup de Grace / Cut Down\n", inline=True)
	embed.add_field(name="Sorcery", value="Celerity / Absolute Focus\n Gathering Storm", inline=True)
	embed.add_field(name="Item Builds", value="This is a guideline only.  Build according to the state of your game.", inline=False)
	embed.add_field(name="Common", value="Blade of the Ruined King\nBerserker's Greaves\nRunaan's Hurricane\nInfinity Edge\nGuardian Angel\nMortal Reminder", inline=True)
	embed.add_field(name="Situationals", value="The Bloodthirster\nRapid Firecannon\nStatikk Shiv\nStormrazor", inline=True)
	
	await ctx.send(embed=embed)
@client.command()
async def build(ctx):
    await builds.invoke(ctx)

@client.event
async def on_member_join(member):

	await client.get_channel(313493970250629120).send("Welcome! Feel free to set your roles in <#316142433828208643>")
	


@client.command()
async def help(ctx):
	embed = discord.Embed(title="Help with Ashe Bot", description="Prefix for this bot is \"$\".",color=0x0098ff)
	embed.add_field(name="builds", value="Displays the builds, runes, and skill order for the current patch.")
	embed.add_field(name="help", value="Displays this screen.", inline=False)
	embed.add_field(name="about", value="Displays information about this bot.", inline=False)
	await ctx.send(embed=embed)
	
	
client.run(TOKEN)