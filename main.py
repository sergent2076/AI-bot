import discord
from discord.ext import commands
from model import detect_cat
import os, random, requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck возвращает фото утки'''
    print('hello')
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('check')
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(detect_cat(image_path=f"./{attachment.filename}",model_path="keras_model.h5", labels_path="labels.txt"))

    else:
        await ctx.send("Вы забыли загрузить картинку :(")

@bot.command()
async def help(ctx):
    await ctx.send(f'Привет! команда такая - делает эта, а команда такая - делает это. Пользуйся)


bot.run("")
