import logging
import os

import discord
from anyio import run
from dotenv import load_dotenv
from harmonia_core import HarmoniaCore

load_dotenv()

TOKEN = os.environ["DEV_BOT_TOKEN"]

intents = discord.Intents.default()
intents.message_content = True

FORMATTER = logging.Formatter(
    fmt="%(asctime)s %(levelname)s    %(message)s", datefmt="[%Y-%m-%d %H:%M:%S]"
)
discord.utils.setup_logging(formatter=FORMATTER)

logger = logging.getLogger("discord")


async def main() -> None:
    async with HarmoniaCore(intents=intents, command_prefix="!") as bot:
        await bot.start(TOKEN)


if __name__ == "__main__":
    try:
        run(main)
    except KeyboardInterrupt:
        logger.info("Shutting down...")
