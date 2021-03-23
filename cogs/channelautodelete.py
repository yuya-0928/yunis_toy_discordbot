from discord.ext import commands
import discord
import asyncio


class Channelautodelete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    

    @commands.command()
    async def delete_channel(self, message):
        if message.channel == 814279508323598429:
            return
        await message.channel.send("チャンネルを削除します")
        print(message.channel.id)
        await message.channel.delete()        

    @commands.command()
    async def delete_channel_sec(self, message, sec):
        if message.channel == 814279508323598429:
            return
        sec = int(sec)
        await message.channel.send(f"チャンネルを{ sec }秒後にメッセージを送信します")
        loop = asyncio.get_event_loop()
        future = loop.create_future()
        # do_delete = loop.call_later(sec, lambda: asyncio.ensure_future(await message.channel.send("実行テスト")))
        # do_delete
        
        # await asyncio.sleep(sec)
        # await message.channel.send("実行テスト")
        



def setup(bot):
    bot.add_cog(Channelautodelete(bot))