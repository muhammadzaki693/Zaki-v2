import discord
from discord.ext import commands

class CogUtils(commands.Cog,name="utils"):
	"""Utilities for the bot"""
	def __init__(self,bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print("cog_utils loaded")
	
	@commands.command(name="ping")
	async def ping(self,ctx):
		await ctx.send("Pong! {}".format(self.bot.latency * 1000))
	
	@commands.command(name="say")
	async def say(self,ctx,*,args):
		await ctx.send("".join(args))

def setup(bot):
	bot.add_cog(CogUtils(bot))