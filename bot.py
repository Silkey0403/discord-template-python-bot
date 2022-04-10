import discord

from discord.ext import commands

intents = discord.Intents.all() # Syntax required when intents are active.
bot = commands.Bot(command_prefix="!", help_command=None, intents=intents) #command_prefix default is !.

TOKEN = "TOKEN HERE" #Bot Token

@bot.event
async def on_ready():
    print(bot.user.name)
    print('Bot Start!')
    game = discord.Game('Activity')
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(TOKEN)
