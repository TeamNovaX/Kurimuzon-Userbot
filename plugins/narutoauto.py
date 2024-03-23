from time import perf_counter

from pyrogram import Client, filters
from pyrogram.types import Message

from utils.filters import command
from utils.misc import modules_help


@Client.on_message(filters.text)
async def nauto(_, message: Message):
    if message.from_user.id == 5416991774:
      if "has challenged you" in messages.text:
        await message.click(0)

module = modules_help.add_module("ping", __file__)
module.add_command("ping", "Check ping to Telegram servers", aliases=["p"])
