from discord.ext import commands
import discord
import asyncio
import re
# import config


class Replydm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # BOTに対してDMを送信したユーザーに定型文を返す
    @commands.Cog.listener()
    async def on_message(self, message):
        # if message.content.startswith("!check_payment"):
        #     return
        if (type(message.channel) == discord.DMChannel) and (message.author != self.bot.user):

            check_email_pattern = "^[0-9a-z_./?-]+@([0-9a-z-]+.)+[0-9a-z-]+$"
            if re.match(check_email_pattern, message.content):
                await message.channel.send(f"メールを確認しました！")
                await message.channel.send(f"チケットの購入状況を確認いたします。KAMINARI運営からのご連絡をお待ちください")

                # user_a = config.user_a
                # user_b = config.user_b

                embed = discord.Embed()
                embed.color = discord.Color.blue()
                embed.description  = "これは管理者用メッセージです。購入確認申請を受け取りました。"
                embed.add_field(name="送信者", value=message.author)
                embed.add_field(name="メールアドレス", value=message.content)

                admin_account = self.bot.get_user(user_b)
                await admin_account.send(embed=embed)
                admin_account = self.bot.get_user(user_a)
                await admin_account.send(embed=embed)
                return
            
            await message.channel.send(f"これは定型文です。どのようなメッセージが送信されても、この文章が返されます。\n チケットを購入している場合は、購入時に登録したメールアドレスを入力してください。\n 質問・お問い合わせは運営アカウントにDMを送信してください。")
            

            # if message.content.startswith("購入確認申請"):
            #     def check_message_author(mail_msg):
            #         return mail_msg.author == message.author

            #     await message.channel.send(f"KAMINARIのご利用ありがとうございます！")
            #     await message.channel.send(f"チケット購入時に入力したメールアドレスを入力してください。例：example@gmail.com")
            #     try:
            #         mail = await self.bot.wait_for('message', check=check_message_author, timeout=120)
            #     except asyncio.TimeoutError:
            #         await message.channel.send("タイムアウトしました。もう一度やり直してください。")
            #         return

            #     higashingi = 713197653193785344
            #     yuyahirako = 583543106926936074

            #     embed = discord.Embed()
            #     embed.color = discord.Color.blue()
            #     embed.description  = "これは管理者用メッセージです。購入確認申請を受け取りました。"
            #     embed.add_field(name="送信者", value=message.author)
            #     embed.add_field(name="メールアドレス", value=mail.content)

            #     admin_account = self.bot.get_user(yuyahirako)
            #     await admin_account.send(embed=embed)
            #     admin_account = self.bot.get_user(higashingi)
            #     await admin_account.send(embed=embed)
                
            #     return
            # else:
                
            

    # 簡単な応答をする
    @commands.command()
    async def hello_dm(self, message):
        if (type(message.channel) == discord.DMChannel) and (message.author != self.bot.user):
            await message.author.send("World!")
        else:
            await message.channel.send("DMで送信してね！")
    
    

    # @commands.command()
    # async def check_payment(self, message):
    #     if (type(message.channel) == discord.DMChannel) and (message.author != self.bot.user):
    #         def check_message_author(mail_msg):
    #             return mail_msg.author == message.author

    #         # if message.content.startswith("購入確認申請"):
    #         await message.channel.send(f"KAMINARIのご利用ありがとうございます！")
    #         await message.channel.send(f"チケット購入時に入力したメールアドレスを入力してください。")
    #         try:
    #             wait_flag += 1
    #             mail = await self.bot.wait_for('message', check=check_message_author, timeout=120)

    #             higashingi = 713197653193785344
    #             yuyahirako = 583543106926936074

    #             admin_account = self.bot.get_user(yuyahirako)
    #             embed = discord.Embed()
    #             embed.color = discord.Color.blue()
    #             embed.description  = "これは管理者用メッセージです。購入確認申請を受け取りました。"
    #             embed.add_field(name="送信者", value=message.author)
    #             embed.add_field(name="メールアドレス", value=mail.content)
    #             await admin_account.send(embed=embed)

    #         except asyncio.TimeoutError:
    #             await message.channel.send("タイムアウトしました。もう一度やり直してください。")
    #             return

            # await admin_account.send(f"これは管理者用メッセージです。購入確認申請を受け取りました。\n 送信者：{message.author}\n内容：「{mail.content}」")
            # admin_account = self.bot.get_user(higashingi)
            # print(admin_account)
            # await admin_account.send(f"これは管理者用メッセージです。メッセージを受け取りました。\n 送信者：{message.author}\n内容：「{message.content}」")
            # return    


def setup(bot):
    bot.add_cog(Replydm(bot))