import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN', None)

if not TOKEN:
    print('Token not found, add it to .env and try again!')
    exit()

intents = discord.Intents.all()
bot = commands.Bot('/', intents=intents)

@bot.event
async def on_ready():
    print('Manito esta on')

@bot.command()
async def batidao(ctx:commands.Context):
    nome = ctx.author.global_name
    await ctx.reply(f'Pode deixar {nome}')

@bot.command()
async def falar(ctx:commands.Context, texto):
    await ctx.reply(texto)

bot.run(TOKEN)
