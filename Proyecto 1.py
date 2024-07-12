import discord
from discord.ext import commands
from Cmd import gen_pass

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '!', intents=intents)

token = 'MWAFhuu1937287398DWFDMrefhehj1738'

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

bot.run(token)
