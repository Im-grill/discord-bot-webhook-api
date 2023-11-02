import discord
from discord.ext import commands
import requests

# Đảm bảo rằng bạn đã thay thế các giá trị này bằng các biến môi trường hoặc cách khác để bảo mật thông tin
BOT_TOKEN = 'MTE2OTM5NDM5NDAzMDQxNTkxMg.GhKoyu.ULjEg8AuSHLstoMHjwYXn9oWqioW9iop3WXjHo'
WEBHOOK_URL = 'https://discord.com/api/webhooks/1169393961572507738/Nl7Ss7aO9sfAZuhBavRejkiGcDcfOqe-K0BLlSwQIGT-Brn0-zXIiOoQ0D5UPCIAXhGF'

bot = commands.Bot(command_prefix='tc')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    # Đảm bảo bot không phản hồi chính nó
    if message.author == bot.user:
        return
    
    # Xử lý lệnh nếu có
    await bot.process_commands(message)
    
    # Tạo và gửi webhook
    data = {
        "content": message.content,
        "username": message.author.display_name
    }
    result = requests.post(WEBHOOK_URL, json=data)
    if result.status_code != 204:
        print(f"Failed to send message: {result.status_code}")

bot.run(BOT_TOKEN)
