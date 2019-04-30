from discord.ext import commands

class memegen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cogtest(self, ctx):
        await ctx.send("This cog test is an success!")
        print(ctx.author.id)

    async def on_message(self, message):
        print(message.content)

def setup(bot):
    bot.add_cog(memegen(bot))