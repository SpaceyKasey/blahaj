from discord.ext import commands


class SyncRoles(commands.Cog):
    """Sync color and GRSM roles with the server"""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_group(name="sync")
    async def sync(self, ctx: commands.Context) -> None:
        ...

    @sync.command(name="color", aliases=["colour"])
    async def syncColorRoles(self, ctx: commands.Context) -> None:
        """Sync color roles with the server

        Args:
            ctx (commands.Context): The context of the command
        """
        raise NotImplementedError


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SyncRoles(bot))
