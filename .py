import discord
from discord.ext import commands
from config import token

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
        elif message.content.startswith('$bye'):
            await message.channel.send("\U0001f642")
        else:
            await message.channel.send(message.content)

# Ayrıcalıklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
intents.message_content = True

# Botu başlat
bot = MyBot(intents=intents)

# Bu bağlam menüsü komutu yalnızca mesajlar üzerinde çalışır
@bot.tree.context_menu(name='Report to Moderators')
async def report_message(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message(
        f'Thanks for reporting this message by {message.author.mention} to our moderators.', ephemeral=True
    )

    log_channel = interaction.guild.get_channel(123456789012345678)  # Burayı kendi kanal ID'nizle değiştirin

    embed = discord.Embed(title='Reported Message', color=discord.Color.red())
    if message.content:
        embed.description = message.content
    else:
        embed.description = "No content in the message."

    embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
    embed.timestamp = message.created_at

    url_view = discord.ui.View()
    url_view.add_item(discord.ui.Button(label='Go to Message', style=discord.ButtonStyle.url, url=message.jump_url))

    await log_channel.send(embed=embed, view=url_view)

@bot.event
async def on_ready():
    await bot.tree.sync()  # Komutları senkronize et

# Botu çalıştır
bot.run(token)
