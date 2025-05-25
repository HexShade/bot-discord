import discord
from discord.ext import commands
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN', None)
OPENAPI_KEY = os.getenv('OPENAPI_KEY', None)

if not TOKEN:
    print('Token not found, add it to .env and try again!')
    exit()

openapi_client = None
if OPENAPI_KEY:
    openapi_client = OpenAI(api_key=OPENAPI_KEY)

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

@bot.command()
async def ai(ctx:commands.Context, *, texto):
    if openapi_client is None:
        await ctx.reply('OpenAI not available!')
    else:
        response = openapi_client.responses.create(
            model="gpt-4.1-nano",
            instructions="Voce eh um humano que modera o grupo do Tales, esse servidor eh sobre " \
            "jogos e voce sempre deve ter um humor bipolar, ou bravo ou arrogante ou feliz e " \
            "estranho, voce sempre tem um nome estranho de algum jogo famoso.",
            input=texto,
        )
        await ctx.reply(response.output_text)

bot.run(TOKEN)
