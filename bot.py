import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='(')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def om_member_join(member):
    print(f'{member} join!')

@bot.event
async def om_member_remove(member):
    print(f'{member} leave!')


bot.run('NjgzMjEyOTU4MDc1MzIyNDU0.XloR4A.K-zoas7Gi5R6xdhPqz6NxQ7niQQ')