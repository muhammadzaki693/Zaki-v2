import discord
from discord.ext import commands

class Maths(commands.Cog, name="math"):
	"""maths command"""
	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("cog_maths loaded")

	@commands.command(name="add", aliases=["adittion"])
	async def add(self, ctx, num1, *args):
		"""Adds numbers together"""
		total = int(num1)
		for arg in args:
			total += int(arg)
		await ctx.send(f"{total}")

	@commands.command(name="subtract", aliases=["subtraction"])
	async def subtract(self, ctx, num1, *args):
		"""Subtracts numbers together"""
		total = int(num1)
		for arg in args:
			total -= int(arg)
		await ctx.send(f"{total}")
	
	@commands.command(name="multiply", aliases=["multiplication"])
	async def multiply(self, ctx, num1, *args):
		"""Multiplies numbers together"""
		total = int(num1)
		for arg in args:
			total *= int(arg)
		await ctx.send(f"{total}")
		
	@commands.command(name="divide", aliases=["division"])
	async def divide(self, ctx, num1, *args):
		"""Divides numbers together"""
		total = int(num1)
		for arg in args:
			total /= int(arg)
		await ctx.send(f"{total}")
	
	@commands.command(name="mod", aliases=["modulo"])
	async def mod(self, ctx, num1, num2):
		"""Modulo"""
		result = 0
		result = int(num1) % int(num2)
		
		await ctx.send(result)
	
	@commands.command(name="sqrt", aliases=["square root"])
	async def sqrt(self, ctx, num):
		"""Square root"""
		result = int(num)**0.5
		await ctx.send(result)
	
	@commands.command(name="pow", aliases=["power"])
	async def pow(self, ctx, num1, num2):
		"""Power"""
		result = int(num1) ** int(num2)
		await ctx.send(result)

def setup(bot):
	bot.add_cog(Maths(bot))