import discord
import settings
import AmazonScript.AmazonPreis as am
from requests import get
from settings import DISCORD_API_SECRET
from discord.ext import commands

# il token è ora storato in .env, in sicurezza
# todo: modificare il prefix in modo aggiornato, decidere il case di scrittura, rendere il channelId dinamico


# Crea un'istanza del bot
CHANNEL_ID = 1156612455963828245
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event


#ON_MESSAGE serve a ricevere e controllare tutti i messaggi inviati da una qualsiasi fonte, indifferente tra server e privato.
#Con le varie funzioni è possibile ricevere dati specifici dal messaggio, per esempio l'autore il contenuto e cosi via.

#################### IMPORTANTE !!!!!!! ####################
# Per fare in modo che esso possa leggere tutti i messaggi bisogna impostare : (intent.all) GUARDARE LA RIGA IN ALTO
# ESSO PUO' ESSERE ATTIVATO ANCHE DALLA PAGINA UFFICIALE andando su Privileged Gateway Intents

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


#In questo modo si creano dei comandi con il prefisso scelto
@bot.command(name='amazon')
async def amazon(contest):
    await contest.send('Ciao! Sono un bot!')

@bot.command(name='papera')
async def papera(contest):
    await contest.send(f'Hai ragione, papera é proprio scemo!')



###############################################################
#################### Avvia il bot##############################
###############################################################
bot.run(settings.DISCORD_API_SECRET)
