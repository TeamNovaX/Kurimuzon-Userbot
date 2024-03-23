from pyrogram import Client, filters
from pyrogram.types import Message

from utils.filters import command
from utils.misc import modules_help



@Client.on_message(
    ~filters.scheduled & filters.text & filters.me & ~filters.forwarded
)
async def naauto(client: Client, message: Message):
    if not message.from_user.id == 5416991774:
        return
    if "has challanged you!" in message:
        await message.click(0)


module = modules_help.add_module("autonaruto", __file__)
module.add_command("na", "Paste text on nekobin", "[code]")
module.add_command("explore", "Paste text on nekobin", "[code]")
