import logging

import discord
from anyio import Path
from discord.ext import commands


class HarmoniaCore(commands.Bot):
    """The core of Harmonia"""

    def __init__(
        self, intents: discord.Intents, command_prefix: str = "!", *args, **kwargs
    ) -> None:
        super().__init__(
            intents=intents,
            command_prefix=command_prefix,
            activity=discord.Game(name="musical notes 🎶"),
            *args,
            **kwargs,
        )
        self.logger = logging.getLogger("discord")

    async def setup_hook(self) -> None:
        """Setup hook to set any stuff up"""
        cogsPath = Path(__file__).parent.joinpath("cogs")
        async for cog in cogsPath.rglob("*.py"):
            self.logger.debug(f"Loading cog: {cog.name[:-3]}")
            await self.load_extension(f"cogs.{cog.name[:-3]}")

    async def on_ready(self) -> None:
        currUser = None if self.user is None else self.user.name
        self.logger.info(f"{currUser} is fully ready!")
