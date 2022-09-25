import discord
import random
from discord.ext import commands

class Fun(commands.Cog, name="Fun command"):
	"""Fun command"""
	def __init__(self,bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("cog_fun loaded")
	
	@commands.command(name="emojify")
	async def emojify(self,ctx,*,args):
		emoji = []
		for arg in args:
			if arg.isdecimal():
				num2str = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
				emoji.append(f":{num2str.get(arg)}:")
			elif arg.isalpha():
				emoji.append(f":regional_indicator_{arg}:")
			else:
				emoji.append(arg)
		await ctx.send("".join(emoji))
	
	@commands.group()
	async def rate(self,ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send("please use z!rate <rate what you want>")
	
	@rate.command(name="gay")
	async def gayrate(self,ctx):
		embed=discord.Embed(title="Gay Rate", description=f"Your {random.randint(0,100)}% gay", color=0x7b00ff)
		await ctx.send(embed=embed)
	
	@rate.command(name="pp")
	async def pprate(self,ctx):
		pplen = random.randint(0,13)
		pp = ["B", "="*pplen, "D"]
		pp = "".join(pp)
		embed=discord.Embed(
			title="pp Rate",
			description=f"Your pp is {pp}",
			color=0x7b00ff
		)
		await ctx.send(embed=embed)
	@rate.command(name="cool")
	async def coolrate(self,ctx):
		embed=discord.Embed(title="cool Rate", description=f"Your {random.randint(1,100)}% cool", color=0x7b00ff)
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Fun(bot))