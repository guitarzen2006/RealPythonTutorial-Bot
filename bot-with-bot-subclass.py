# bot.py
import os
import random
from dotenv import load_dotenv

# 1
from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')


#2
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord')

@bot.command(name='99', help='When the \'!99\' is invoked, a random Brooklyn 99 quote is displayed. ')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 100 emoji.', 
        'Bingpot!', 
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt. '
        ),
    ]
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice. eg roll_dice [number of dice] [number of sides]')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides +1 )))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


bot.run(token)