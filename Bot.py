import discord
import settings
import QuackBot.Scripts.AmazonScript.AmazonPrezzo as am
from requests import get
from discord.ext import commands

# Crea un'istanza del bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


# ON_MESSAGE serve a ricevere e controllare tutti i messaggi inviati da una qualsiasi fonte, indifferente tra server
# e privato. Con le varie funzioni è possibile ricevere dati specifici dal messaggio, per esempio l'autore il
# contenuto e cosi via.

#################### IMPORTANTE !!!!!!! ####################
# Per fare in modo che esso possa leggere tutti i messaggi bisogna impostare : (intent.all) GUARDARE LA RIGA IN ALTO
# ESSO PUO' ESSERE ATTIVATO ANCHE DALLA PAGINA UFFICIALE andando su Privileged Gateway Intents
@bot.command()
async def amazon(ctx):
    await ctx.send(am.amazonMain())


@bot.command()
async def papera(contesto):
    await contesto.send('Hai ragione, papera é proprio scemo!')


@bot.command()
async def btc(contesto):
    response = get("https://api.kucoin.com/api/v1/market/stats?symbol=BTC-EUR")
    prezzo_attuale = float(response.json()['data']['buy'])
    testo = f'Il prezzo attuale per il 1 BTC é pari a {prezzo_attuale} euro'
    await contesto.send(testo)


@bot.event
async def on_message(message):
    author = message.author
    # testoMs = message.content -> Questo contiene il contenuto del messaggio, sono divisi dagli spazzi, esempio CIAO
    # MARIO testoMs[0]=CIAO testoMs[1]=MARIO canale = message.channel
    if author == bot.user:
        return
    else:
        await bot.process_commands(message)


###############################################################
#################### Avvia il bot##############################
###############################################################
bot.run(settings.DISCORD_API_SECRET)
