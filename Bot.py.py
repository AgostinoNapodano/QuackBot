
import discord
from discord.ext import commands

# Configura il tuo bot
TOKEN = 'MTE1NTk1NTk0OTc3Mzc5OTQ5NQ.GjRW6Q.ZH08rkshrR_pol-Vbq2iizu0xuWc1ydQdKHIAs'
PREFIX = '!'

# Crea un'istanza del bot
bot = commands.Bot(command_prefix=PREFIX)

@bot.command(name='saluta', help='Il bot ti saluterà in un canale testuale.')
async def saluta(ctx):
    author = ctx.author
    await ctx.send(f'Ciao, {author.mention}!')

@bot.command(name='papera', help='Il bot risponderà con una risposta personalizzata.')
async def papera(ctx):
    await ctx.send(f'Che papera cornuta, {ctx.author.mention}!')

# Avvia il bot
bot.run(TOKEN)
