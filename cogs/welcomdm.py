from discord.ext import commands
import discord


class Welcomdm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_member_join(self, member):
        # await member.send("新規参加者にDMを送信することができるよ")

    # @commands.Cog.listener()
    # async def on_member_remove(self, member):
    #     await member.send("退出時にもDMを送信することができるよ")
    
    @commands.command()
    async def test(self, message):
        await message.channel.send('test ok')
            


def setup(bot):
    bot.add_cog(Welcomdm(bot))