from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import os
from cogs.hs import langs
from cogs.hs import *

def isitallowed(guildid, authorid):
    config = os.path.exists('./{}'.format(guildid))
    if config:
        fobj = open("{}".format(guildid))
        text = fobj.read().strip().split()
        # Conditions

        while True:
            s = "0"
            if s in text:
                return settings.getlang(authorid)
            else:
                # disallowed to have specific user languages
                return 0

    else:
        # not specified by server owner, assuming its set to yes
        return settings.getlang(authorid)



class langrelated(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setlang(self, ctx, value=0):
        if value == "english":
            try:
                os.remove("{}".format(ctx.author.id))
            except OSError:
                pass
            with open("{}".format(ctx.author.id), "a") as myfile:
                myfile.write("0".format(value))
                await ctx.send("I've set your preffered language to english!")
        if value == "german":
            try:
                os.remove("{}".format(ctx.author.id))
            except OSError:
                pass
            with open("{}".format(ctx.author.id), "a") as myfile:
                myfile.write("1".format(value))
                await ctx.send("I've set your preffered language to german!")

        try:
            os.remove("{}".format(ctx.author.id))
        except OSError:
            pass
        with open("{}".format(ctx.author.id), "a") as myfile:
            myfile.write("{}".format(value))
            if value == 1:
                await ctx.send("I've set your preffered language to german!")
            elif value == 0:
                await ctx.send("I've set your preffered language to english!")
            else:
                await ctx.send(langs.setlangerr[isitallowed(ctx.guild.id, ctx.author.id)])

    @commands.command()
    @has_permissions(manage_messages=True)
    async def specificlang(self, ctx, value=0):
        if value == "true":
            try:
                os.remove("{}".format(ctx.guild.id))
            except OSError:
                pass
            with open("{}".format(ctx.guild.id), "a") as myfile:
                myfile.write("0".format(value))
                await ctx.send("User specific languages are now allowed in your server!")
        if value == "german":
            try:
                os.remove("{}".format(ctx.guild.id))
            except OSError:
                pass
            with open("{}".format(ctx.guild.id), "a") as myfile:
                myfile.write("1".format(value))
                await ctx.send("User specifc languages are now disallowed in your server!")

        try:
            os.remove("{}".format(ctx.guild.id))
        except OSError:
            pass
        with open("{}".format(ctx.guild.id), "a") as myfile:
            myfile.write("{}".format(value))
            if value == 1:
                await ctx.send("User specific languages are now disallowed in your server!")
            else:
                await ctx.send("User specific languages are now allowed in your server!")

def setup(bot):
    bot.add_cog(langrelated(bot))