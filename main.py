import discord
import random
from discord.ext import commands
import словать as s
list_ = ['images/mem1.jpg','images/mem2.jpg','images/mem3.jpg']
token = ''

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='1', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def spam(ctx, iteration, *, text):
    for i in range(int(iteration)):
        await ctx.reply(f'```{text}```')

@bot.command()
async def ping(ctx, user_id):
    await ctx.message.delete()
    await ctx.send('||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||<@' + str(user_id) + ">")

@bot.command()
async def sum(ctx, num1, *, num2):
    sum_ = int(num1) + int(num2)
    await ctx.reply(str(sum_))

@bot.command()
async def mem(ctx):
    x = random.randint(1,6)
    if x == 1 or x == 2 or x == 3:
        file1 = 0
        await ctx.send('обычный мем')
    elif x == 4 or x == 5:
        await ctx.send('средний мем')
        file1 = 1
    elif x == 6:
        await ctx.send('редкий мем')
        file1 = 2
        
    with open(file1, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run(token)
