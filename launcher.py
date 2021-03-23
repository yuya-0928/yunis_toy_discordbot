from discord.ext import commands
import discord
# import config
# import cogs.Replydm as Replydm
import sys
import os
import datetime

# token = config.DISCORD_BOT_TOKEN

token = os.environ['DISCORD_BOT_TOKEN']

intents = discord.Intents.default()  # デフォルトのIntentsオブジェクトを生成
intents.typing = False  # typingを受け取らないように
intents.members = True

bot = commands.Bot(command_prefix="!", intents = intents)

@bot.event
async def on_ready():
    print("on_ready")
    print('--------')
    print(bot.user.name)
    print(bot.user.id)
    print('--------')
    d_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    text = f'BOTが起動しました。\n ボット名：{bot.user}\n 時刻：{d_time}!'
    channel = bot.get_channel(823932867201597472)
    # Memberjoin.setup(bot)
    await channel.send(text)
    await channel.send('start success')


# 起動確認のコマンド
# @bot.command()
# async def test(message):
#     await message.channel.send('test ok')

# 終了コマンド
@bot.command()
async def shutdown(message):
    await message.channel.send("shutdown bot")
    sys.exit()


bot.load_extension("cogs.greet")
bot.load_extension("cogs.notify")
bot.load_extension("cogs.debug")
bot.load_extension("cogs.replydm")
bot.load_extension("cogs.welcomdm")
bot.load_extension("cogs.channelautodelete")
bot.run(token)