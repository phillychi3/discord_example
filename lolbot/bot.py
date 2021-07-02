import discord
from discord.ext import commands
bot= commands.Bot(command_prefix="!")
@bot.command()
async def test(ctx):
    await.send.ctx("great")
bot.run('TOKEN')