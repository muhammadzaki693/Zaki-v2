import os
import discord
import asyncio
import random
from itertools import cycle
from random import choice
from discord.ext import commands
from keep_alive import keep_alive
from discord.ext import commands
from discord import Embed
import json

bot = commands.Bot(
	command_prefix="zz",  # Change to desired prefix
	case_insensitive=True,  # Commands aren't case-sensitive
	owner_id=758298255389097984,  # Set to "", if you don't want to set an owner
)

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send("program error: command not found")
	if isinstance(error, commands.CheckFailure):
		await ctx.send("program error: check failed")
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("program error: missing required argument")
	if isinstance(error, commands.BadArgument):
		await ctx.send("program error: bad argument")
	if isinstance(error,commands.DisabledCommand):
		await ctx.send("program error: command disabled")

async def change_status():
	await bot.wait_until_ready()
	status=cycle(["i'm alive",f"on {len(bot.guilds)} server", "discord.py"])
	while not bot.is_closed():
		await bot.change_presence(activity=discord.Game(name=next(status)))
		await asyncio.sleep(10)

@bot.command(name="about")
async def about_me(ctx):
	embed = Embed(
		title="About Me",
		description="idk",
		color=discord.Color.blue()
	)
	await ctx.send(embed=embed)

extensions = [
	'cogs.cog_dev',
	"cogs.cog_maths",
	"cogs.cog_utils",
	"cogs.cog_fun"# Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.
bot.loop.create_task(change_status())  # Starts a task to change the status.
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  # Starts the bot.