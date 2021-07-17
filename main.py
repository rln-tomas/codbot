from dotenv import load_dotenv
from discord.ext import commands
import os
load_dotenv()

token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix="!!")

@bot.command(name='test')
async def test(ctx, parameter):
    response = parameter
    await ctx.send(parameter) 

bot.run(token)