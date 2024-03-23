from pyrogram import Client, filters
from pyrogram.types import Message

from utils.filters import command
from utils.misc import modules_help



@Client.on_message(
    ~filters.scheduled & command(["na", "explore"]) & filters.me & ~filters.forwarded
)
async def naauto(client: Client, message: Message):
    await message.delete()
    a = await message.reply("/explore")


module = modules_help.add_module("nekobin", __file__)
module.add_command("nekobin", "Paste text on nekobin", "[code]")
module.add_command("neko", "Paste text on nekobin", "[code]")
