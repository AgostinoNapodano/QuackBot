import discord
from discord import Client
from requests import get
from settings import DISCORD_API_SECRET

# Configura il tuo bot
# il token è ora storato in .env, in sicurezza
# todo: modificare il prefix in modo aggiornato, decidere il case di scrittura, rendere il channelId dinamico
TOKEN = DISCORD_API_SECRET
PREFIX = '!'

# Crea un'istanza del bot
CHANNEL_ID = 1156612455963828245

bot = Client(intents=discord.Intents.all())


@bot.event
async def on_message(message):
    author = message.author
    testoMs = message.content
    canale = message.channel
    if author == bot.user:
        return
    if testoMs.startswith('!btc'):
        response = get("https://api.kucoin.com/api/v1/market/stats?symbol=BTC-EUR")
        prezzo_attuale = float(response.json()['data']['buy'])
        canale = bot.get_channel(CHANNEL_ID)
        testo = f'Il prezzo attuale per il 1 BTC é pari a {prezzo_attuale} euro'
        await canale.send(testo)
    if testoMs.startswith('!papera'):
        await canale.send(f'Hai ragione, papera é proprio scemo, {author.mention}!')
    if testoMs.startswith('!checkprise'):
        testoMs = testoMs.split()[1]
        response = get(testoMs)
        testo = f'Il prezzo attuale per il 1 BTC é pari a {response} euro'


# Avvia il bot
bot.run(TOKEN)
