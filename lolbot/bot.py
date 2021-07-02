import discord
from discord.ext import commands
bot= commands.Bot(command_prefix="!")

@bot.command()
async def test(ctx):
    await ctx.send("great")
    
    
bot.run('ODYwNTY3MzAzODE2NjA5ODEy.YN9HwQ.OIxTOveMX_ISq2HoCeBBtKzT-SU')