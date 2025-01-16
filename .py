import discord
from config import token
from discord.ext import commands
import os
import random

class MyBot(commands.Bot):
    def __init__(self, intents):
        super().__init__(command_prefix='!', intents=intents)

    async def on_ready(self):
        print(f'{self.user} olarak giriş yaptık.')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$merhaba'):
            await message.channel.send("Selam!")
        if message.content.startswith('$help'):
            await message.channel.send("komutlar: $selam, $bye, $plastik, $Kagıt!")
        elif message.content.startswith('$bye'):
            await message.channel.send("\U0001f642")
        elif message.content.startswith('$plastik'):
            await message.channel.send("skibidi sigma spagetti gibi gözüken plastiklerimiz dünya için çok zararlı ve ölümcül tehtitler içermektedir. plastik poşetler bu yüzden para ile omaya başladı. plastik malzemeler kullanmaktan kaçının çünkü bu tür maddeler doğada yok olmaz!")
        elif message.content.startswith('$kagıt'):
            await message.channel.send("Kağıt, bizim için çok önemli bir buluştur(sınav için kullanılmadığı sürece). ancak kağıdın da bazı sorunları vardır. Kağıt üretimi için günde yüzlerce kağıt kesilmekte ve bu nedenle deforestation denilen bir kavram ortaya çıktı. bu yüzden kağıt kullanırken miktarı abartmayın!")
        else:
            await message.channel.send(f"{message.content} not recognized")

# Ayrıcalıklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
intents.message_content = True

# Botu başlat
bot = MyBot(intents=intents)

# Bu bağlam menüsü komutu yalnızca mesajlar üzerinde çalışır


@bot.event
async def on_ready():
    await bot.tree.sync()  # Komutları senkronize et

# Botu çalıştır
bot.run(token)
