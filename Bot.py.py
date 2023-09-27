
import discord
from discord.ext import commands

# Configura il tuo bot
TOKEN = 'MTE1NTk1NTk0OTc3Mzc5OTQ5NQ.GjRW6Q.ZH08rkshrR_pol-Vbq2iizu0xuWc1ydQdKHIAs'
PREFIX = '!'

# Crea un'istanza del bot
bot = commands.Bot(command_prefix=PREFIX)

# Definisci un evento di risposta al messaggio "ciao"
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignora i messaggi inviati dal proprio bot per evitare cicli infiniti
    if "ciao" in message.content.lower():
        await message.channel.send(f'Ciao, {message.author.mention}!')

# Avvia il bot
bot.run(TOKEN)