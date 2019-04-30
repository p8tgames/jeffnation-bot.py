from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import time
from cogs.hs import langs
import discord
import os
from cogs.hs import *
import datetime

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
                #disallowed to have specific user languages
                return 0

    else:
        #not specified by server owner, assuming its set to yes
        return settings.getlang(authorid)

class help(commands.Cog):  # done
    @commands.command()
    async def help(self, ctx, category="main"):
        guildid = ctx.author.id

        if "main" in category:
            ts = int(time.time())
            embed = discord.Embed(title=langs.helpmain_string[isitallowed(guildid, ctx.author.id)],
                                  colour=discord.Colour(0xaee38f),
                                  description=langs.helpreq_string[isitallowed(guildid, ctx.author.id)],
                                  timestamp=datetime.datetime.utcfromtimestamp(ts))
            embed.set_author(name="Jeff Nation"),
            embed.set_footer(text=langs.helphelp_string[isitallowed(guildid, ctx.author.id)]),

            embed.add_field(name="Admin", value=langs.helpadmin[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="Fun", value=langs.helpfun[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="Infos", value=langs.helpinfos[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="Misc", value=langs.helpmisc[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="Music", value=langs.helpmusic[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name=langs.helpbug1[isitallowed(guildid, ctx.author.id)],
                            value=langs.helpbug2[isitallowed(guildid, ctx.author.id)])

            await ctx.send(
                content="",
                embed=embed)
            return

        if "admin" in category:
            ts = int(time.time())
            embed = discord.Embed(title=langs.ahlpmain[isitallowed(guildid, ctx.author.id)],
                                  colour=discord.Colour(0xaee38f),
                                  description=langs.helpreq_string[isitallowed(guildid, ctx.author.id)],
                                  timestamp=datetime.datetime.utcfromtimestamp(ts))
            embed.set_author(name="Jeff Nation"),
            embed.set_footer(text=langs.helphelp_string[isitallowed(guildid, ctx.author.id)]),

            embed.add_field(name="j!specificlang", value=langs.ahlpban[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="j!serverinfo", value=langs.ahlserverinfo[isitallowed(guildid, ctx.author.id)]),

            await ctx.send(
                content="",
                embed=embed)
            return

        if "fun" in category:
            ts = int(time.time())
            embed = discord.Embed(title=langs.fhlpmain[isitallowed(guildid, ctx.author.id)],
                                  colour=discord.Colour(0xaee38f),
                                  description=langs.helpreq_string[isitallowed(guildid, ctx.author.id)],
                                  timestamp=datetime.datetime.utcfromtimestamp(ts))
            embed.set_author(name="Jeff Nation"),
            embed.set_footer(text=langs.helphelp_string[isitallowed(guildid, ctx.author.id)]),

            embed.add_field(name="j!cat", value=langs.fhlpcat[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="j!dog", value=langs.fhlpdog[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="j!howgay", value=langs.fhlphowgay[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="j!runs", value=langs.fhlpruns[isitallowed(guildid, ctx.author.id)])
            embed.add_field(name="j!isthisbotdown", value=langs.fhlpisthis[isitallowed(guildid, ctx.author.id)])
            embed.add_field(name="j!guess", value=langs.fhlpguess[isitallowed(guildid, ctx.author.id)])

            await ctx.send(
                content="",
                embed=embed)
            return

        if "infos" in category:
            ts = int(time.time())
            embed = discord.Embed(title=langs.ihlpmain[isitallowed(guildid, ctx.author.id)],
                                  colour=discord.Colour(0xaee38f),
                                  description=langs.helpreq_string[isitallowed(guildid, ctx.author.id)],
                                  timestamp=datetime.datetime.utcfromtimestamp(ts))
            embed.set_author(name="Jeff Nation"),
            embed.set_footer(text=langs.helphelp_string[isitallowed(guildid, ctx.author.id)]),

            embed.add_field(name="j!avatar", value=langs.ihlpavatar[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="j!joined", value=langs.ihlpjoined[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="j!source", value=langs.ihlpsource[isitallowed(guildid, ctx.author.id)]),

            await ctx.send(
                content="",
                embed=embed)
            return

        if "misc" in category:
            ts = int(time.time())
            embed = discord.Embed(title=langs.mhlpmain[isitallowed(guildid, ctx.author.id)],
                                  colour=discord.Colour(0xaee38f),
                                  description=langs.helpreq_string[isitallowed(guildid, ctx.author.id)],
                                  timestamp=datetime.datetime.utcfromtimestamp(ts))
            embed.set_author(name="Jeff Nation"),
            embed.set_footer(text=langs.helphelp_string[isitallowed(guildid, ctx.author.id)]),

            embed.add_field(name="j!hw", value=langs.mhlphw[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="j!kickme", value=langs.mhlpkickme[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="j!console", value=langs.mhlpconsole[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="j!add", value=langs.mhlpadd[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="j!choose", value=langs.mhlpchoose[isitallowed(guildid, ctx.author.id)]),

            await ctx.send(
                content="",
                embed=embed)
            return

        if "music" in category:
            ts = int(time.time())
            embed = discord.Embed(title=langs.musicpmain[isitallowed(guildid, ctx.author.id)],
                                  colour=discord.Colour(0xaee38f),
                                  description=langs.helpreq_string[isitallowed(guildid, ctx.author.id)],
                                  timestamp=datetime.datetime.utcfromtimestamp(ts))
            embed.set_author(name="Jeff Nation"),
            embed.set_footer(text=langs.helphelp_string[isitallowed(guildid, ctx.author.id)]),

            embed.add_field(name="j!haha", value=langs.musichaha[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="j!ricardo", value=langs.musicricardo[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="j!yt", value=langs.musicyt[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="j!lofi", value=langs.musiclofi[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="j!smw", value=langs.musicsmw[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="j!knock", value=langs.musicknock[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="j!stop", value=langs.musicstop[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="j!volume", value=langs.musicvolume[isitallowed(guildid, ctx.author.id)]),

            await ctx.send(
                content="",
                embed=embed)
            return

def setup(bot):
    bot.add_cog(help(bot))