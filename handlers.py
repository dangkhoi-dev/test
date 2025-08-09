from config import ALLOWED_CHANNEL_ID, CODE_CHECK_CHANNEL_ID
from verification import handle_verification, handle_code_check

async def on_message_handler(client, message):
    print(f"📩 Nhận được tin nhắn từ kênh ID: {message.channel.id}")

    if message.author == client.user or message.author.bot:
        return

    if message.channel.id not in [ALLOWED_CHANNEL_ID, CODE_CHECK_CHANNEL_ID]:
        return

    if message.channel.id == ALLOWED_CHANNEL_ID:
        await handle_verification(message)

    elif message.channel.id == CODE_CHECK_CHANNEL_ID:
        await handle_code_check(message)

