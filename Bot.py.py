
from discord import Client
from requests import get

# Configura il tuo bot
TOKEN = 'MTE1NTk1NTk0OTc3Mzc5OTQ5NQ.GjRW6Q.ZH08rkshrR_pol-Vbq2iizu0xuWc1ydQdKHIAs'
PREFIX = '!'

# Crea un'istanza del bot
CHANNEL_ID=1156612455963828245

bot = Client()

@bot.event
async def on_ready():
    response = get("https://api.kucoin.com/api/v1/market/stats?symbol=BTC-EUR")
    prezzo_attuale = float(response.json()['data']['buy'])
    canale = bot.get_channel(CHANNEL_ID)
    testo = f'Il prezzo attuale per il 1 BTC é pari a {prezzo_attuale} euro'
    await canale.send(testo)

@bot.event
async def on_message(ctx):
    author = ctx.author
    testo = ctx.content
    canale = ctx.channel
    if author == bot.user:
        return
    await canale.send(f'Hai ragione, papera é proprio scemo, {author.mention}!')


# Avvia il bot
bot.run(TOKEN)
