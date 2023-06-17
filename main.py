import discord, requests
import random
from discord.ext import commands
import словать as s
from bs4 import BeautifulSoup
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

@bot.command()
async def spam(ctx, iteration, *, word):
    for i in range(iteration):
        await ctx.reply(str(word))

@bot.command()
async def find(ctx,*,search):
    s=requests.get(f'https://www.google.com/search?q={search}&hl=en&tbm=isch&sxsrf=APwXEdeSDXkW6cshlUSrlZktTpWKEbKi8Q%3A1680718978108&source=hp&biw=1280&bih=899&ei=grwtZNGSApCGxc8PxaSNgA8&iflsig=AOEireoAAAAAZC3KklNBlCtaKkuwgJ0AzvsySJAv5C7l&ved=0ahUKEwjR25yNrpP-AhUQQ_EDHUVSA_AQ4dUDCAY&uact=5&oq=hello&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEOoCECc6BAgjECdQjQRYzQhgyQpoAXAAeACAAWKIAcYDkgEBNZgBAKABAaoBC2d3cy13aXotaW1nsAEK&sclient=img').text
    q=BeautifulSoup(s,'lxml')
    grab=q.findAll('img')[random.randint(1,15)].get('src')
    await ctx.reply(f'поиск по запросу | {search}{grab}')

bot.run(token)
