import discord
from discord.ext import commands
from Cmd import gen_pass
import os
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '!', intents=intents)

    token = 'IEWHFU238422IUH3DSJADN2393201931EYGYF12D1Y239Y1H2UBG'

@bot.event
async def on_read():
    print(f'Saludos! {bot.user}!')

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(20))

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def test2(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')

@bot.command(name = 'meme')
async def memes(ctx):
    with open('imagenes/meme1.jpg', 'rb') as g:
        picture = discord.File(g)
    await ctx.send(file = picture)

@bot.command(name = 'memes')
async def memes(ctx):
    img_mem = random.choice(os.listdir('imagenes'))
    with open(f'imagenes/{img_mem}', 'rb') as g:
        picture = discord.File(g)
    await ctx.send(file = picture)

#NEW
@bot.command(name = 'play')
async def juegos(ctx):
    img_SudoF = random.choice(os.listdir('SF'))
    img_SudoN = random.choice(os.listdir('SN'))
    img_SudoD = random.choice(os.listdir('SD'))
   #Sudoku facil
    with open(f'SF/{img_SudoF}', 'rb') as f:
        izi = discord.File(f)
    await ctx.send(file = izi)
    #sudoku medio
    with open(f'SN/{img_SudoN}', 'rb') as m:
        mid = discord.File(m)
    await ctx.send(file = mid)
    #sudoku dificil
    with open(f'SD/{img_SudoD}', 'rb') as d:
        hard = discord.File(d)
    await ctx.send(file = hard)
#/NEW

bot.run(token)
