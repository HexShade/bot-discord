import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot('/', intents=intents)

@bot.event
async def on_ready():
    print('Manito esta on')

@bot.command()
async def Batidao(ctx:commands.Context):
    nome = ctx.author.global_name
    await ctx.reply(f'Pode deixar {nome}')

@bot.command()
async def Falar(ctx:commands.Context, texto):
    await ctx.reply(texto)

bot.run('MTM3NjE4NjU2MjAxODI4MzcwMw.Geu8DW.-1qT8XiG4s99EE7ysdufQeRbJMbS3nGrC3wRBc')
