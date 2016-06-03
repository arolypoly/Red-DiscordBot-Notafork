import discord
from discord.ext import commands


class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def remind(self, ctx, *text, user: discord.Member = None):
        """This does stuff!"""

        # Your code will go here
        await self.bot.say(user.mention + ctx.message.author + text)

    async def parse(self, string: str):
        await self.bot.say(string)


def setup(bot):
    bot.add_cog(Mycog(bot))
