import discord
import json
import os
from discord.ext import commands

class DevCommands(commands.Cog, name='Developer Commands'):
	'''These are the developer commands'''

	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		print("cog_dev loaded")

	@commands.command(  # Decorator to declare where a command is.
		name='reload',  # Name of the command, defaults to function name.
		aliases=['rl']  # Aliases for the command.
	)   
	@commands.is_owner()  # Only allow owners to use the command.
	async def reload(self, ctx, cog):
		'''
		Reloads a cog.
		'''
		extensions = self.bot.extensions  # A list of the bot's cogs/extensions.
		if cog == 'all':  # Lets you reload all cogs at once
			for extension in extensions:
				self.bot.unload_extension(cog)
				self.bot.load_extension(cog)
			await ctx.send('Done')
		if cog in extensions:
			self.bot.unload_extension(cog)  # Unloads the cog
			self.bot.load_extension(cog)  # Loads the cog
			await ctx.send('Done')  # Sends a message where content='Done'
		else:
			await ctx.send('Unknown Cog')  # If the cog isn't found/loaded.
	
	@commands.command(name="unload", aliases=['ul'])  
	@commands.is_owner()
	async def unload(self, ctx, cog):
		'''
		Unload a cog.
		'''
		extensions = self.bot.extensions
		if cog not in extensions:
			await ctx.send("Cog is not loaded!")
			return
		self.bot.unload_extension(cog)
		await ctx.send(f"`{cog}` has successfully been unloaded.")
	
	@commands.command(name="load")
	@commands.is_owner()
	async def load(self, ctx, cog):
		'''
		Loads a cog.
		'''
		try:

			self.bot.load_extension(cog)
			await ctx.send(f"`{cog}` has successfully been loaded.")

		except commands.errors.ExtensionNotFound:
			await ctx.send(f"`{cog}` does not exist!")

	@commands.command(name="listcogs", aliases=['lc'])  
	@commands.is_owner()
	async def listcogs(self, ctx):
		'''
		Returns a list of all enabled commands.
		'''
		base_string = "```css\n"  # Gives some styling to the list (on pc side)
		base_string += "\n".join([str(cog) for cog in self.bot.extensions])
		base_string += "\n```"
		await ctx.send(base_string)
	
	@commands.command(name="toggle")
	@commands.is_owner()
	async def toggle(self, ctx, *, command):
		command = self.bot.get_command(command)
		if command is None:
			await ctx.send("Command is not there!")
		elif ctx.command == command:
			await ctx.send("you can not disable this command")
		else:
			command.enabled = not command.enabled
			tenary = "Enabled" if command.enabled else "Disabled"
			await ctx.send(f"Command `{command.name}` has been {tenary}")

def setup(bot):
	bot.add_cog(DevCommands(bot))