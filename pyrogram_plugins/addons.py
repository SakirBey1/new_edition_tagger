from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(Config.BOT_ID):
            await msg.reply(
                f'''`Hey` {msg.from_user.mention} `beni` {msg.chat.title} `grubuna eklediğin için teşekkürler⚡️`\n\n**Grublarda 10k yakın üye etiketleme özelliğim vardır komutlar için /help yazmanız yeterlidir✨**''')

        elif str(new_user.id) == str(Config.OWNER_ID):
            await msg.reply('İşte bu gelen benim sahibim.')
            
@Client.on_message(filters.command("pyrogram"))
async def _py(client: Client, message: Message):
    await message.reply_text('Pyrogram is a Python library for Telegram bots.')



 
@Client.on_message(filters.command("id"))
async def _id(_, message: Message):
    msg = message.reply_to_message or message
    out_str = "**User İnfo:**\n"
    out_str += f" ⚡️ __Grup ID__ : `{(msg.forward_from_chat or msg.chat).id}`\n"
    out_str += f" 💎 __Yanıtlanan Kullanıcı Adı__ : {msg.from_user.first_name}\n"
    out_str += f" 💬 __Mesaj ID__ : `{msg.forward_from_message_id or msg.message_id}`\n"
    if msg.from_user:
        out_str += f" 🙋🏻‍♂️ __Yanıtlanan Kullanıcı ID__ : `{msg.from_user.id}`\n"
 
    await message.reply(out_str)

@Client.on_message(filters.command("info"))
async def _id(_, message: Message):
    msg = message.reply_to_message or message
    out_str = "**User İnfo:**\n"
    out_str += f" ⚡️ __Grup ID__ : `{(msg.forward_from_chat or msg.chat).id}`\n"
    out_str += f" 💎 __Yanıtlanan Kullanıcı Adı__ : {msg.from_user.first_name}\n"
    out_str += f" 💬 __Mesaj ID__ : `{msg.forward_from_message_id or msg.message_id}`\n"
    if msg.from_user:
        out_str += f" 🙋🏻‍♂️ __Yanıtlanan Kullanıcı ID__ : `{msg.from_user.id}`\n"
 
    await message.reply(out_str)

@Client.on_message(filters.command("ping"))
async def pingy(client, message):
    start = datetime.now()
    hmm = await message.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await hmm.edit(
        f"█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄\n**Ping: {round(ms)}**")
