import asyncio
import datetime
import logging
import os
import sys
import traceback
import discord
from discord.ext import commands
import random
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import time
from pathlib import Path
from modules import *
from hs import *
from hs import langs
import base64
from io import BytesIO
import platform
import youtube_dl

if platform.system()=="Darwin":
    Image = "Placeholder as PIL broke on my Mac"
else:
    from PIL import Image


youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)




class NotInWhiteList(commands.CheckFailure):
    pass

def in_whitelist(whitelist):
    async def inner_check(ctx):
        if ctx.author.id not in whitelist:
            raise NotInWhiteList("heh ur not sudo lol {}".format(ctx.author.id))
        return True
    return commands.check(inner_check)

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


if not sys.version_info[:2] >= (3, 5):
    print("Error: requires python 3.5.2 or newer")
    exit(1)

async def status_task():
    while True:
        activity = discord.Game(name="with an Server near you",  type=1)
        await bot.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name="if you do jn help", type=1)
        await bot.change_presence(status=discord.Status.idle, activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name="do jn setlang after adding!", type=1)
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=activity)
        await asyncio.sleep(10)

description = '''Rewritten Version of FuckTardBot.
You may contact the owner (using jn console) if an issue
was found.'''
bot = commands.Bot(command_prefix='jn ', description=description)
bot.remove_command('help')
TOKEN = token.gettoken()


ffmpeg_options = {
    'before_options': '-nostdin',
    'options': '-vn'
}


class knocking:
    @bot.command()
    async def knock(ctx):
        """Plays knocking sounds in Voice Chat"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("./knock.mp3"))
        await ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

    @bot.command()
    async def smw(ctx):
        """Plays knocking sounds in Voice Chat"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("./smw.mp3"))
        await ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

    @bot.command()
    async def haha(ctx):
        """Plays knocking sounds in Voice Chat"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("./gnome.mp3"))
        await ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

    #https://www.youtube.com/watch?v=hHW1oY26kxQ
    @bot.command()
    async def lofi(self, ctx):
        """Streams from a url (same as yt, but doesn't predownload)"""

        async with ctx.typing():
            player = await YTDLSource.from_url("https://www.youtube.com/watch?v=hHW1oY26kxQ", loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    @bot.command()
    async def stop(ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

    @smw.before_invoke
    @haha.before_invoke
    @lofi.before_invoke
    @knock.before_invoke
    async def ensure_voice(ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

    @bot.command()
    async def knocksound(ctx):
        await ctx.send(file=discord.File("knock.mp3"))




@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    activity = discord.Game(name="with an Server near you", url="google.com", type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("changed status to playing {}!".format(activity))
    bot.loop.create_task(status_task())
    print("entered loop!")


async def on_error(ctx, event, *args, **kwargs):
    message = args[0] #Gets the message object
    logging.warning(traceback.format_exc()) #logs the error
    await ctx.send("You caused an error!") #send the message to the channel



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, NotInWhiteList):
        await ctx.author.send(error)
smw


class misc:
    # some random strings mentioned in RUN_STRINGS listed above.

    # I have not made this below, the original is attached both in the readme AND as link below.
    #https://github.com/skittles9823/SkittBot/blob/master/tg_bot/modules/thonkify.py

    @bot.command()
    async def thonkify(ctx, *, meme):
        from modules import thonkify_dict as thonkifydict


        if (len(meme)) > 39:
            await ctx.send("frick you dont overload me")
            return

        tracking = Image.open(BytesIO(base64.b64decode(
            'iVBORw0KGgoAAAANSUhEUgAAAAYAAAOACAYAAAAZzQIQAAAALElEQVR4nO3BAQ0AAADCoPdPbQ8HFAAAAAAAAAAAAAAAAAAAAAAAAAAAAPwZV4AAAfA8WFIAAAAASUVORK5CYII=')))

        # remove characters thonkify can't parse
        for character in meme:
            if character not in thonkifydict.thonkifydict:
                meme = meme.replace(character, "")


        x = 0
        y = 896
        image = Image.new('RGBA', [x, y], (0, 0, 0))

        for character in meme:
            value = thonkifydict.thonkifydict.get(character)
            addedimg = Image.new('RGBA', [x + value.size[0] + tracking.size[0], y], (0, 0, 0))
            addedimg.paste(image, [0, 0])
            addedimg.paste(tracking, [x, 0])
            addedimg.paste(value, [x + tracking.size[0], 0])
            image = addedimg
            x = x + value.size[0] + tracking.size[0]

        image.save("thonk.png")
        await ctx.send(file=discord.File("./thonk.png"))


    @bot.command() #no need
    async def runs(ctx):
        """Gives out an random funny string."""
        await ctx.send(strings.getrunstring())


    # adds 2 numbers
    @bot.command() # no need
    async def add(ctx, left: int, right: int):
        """Adds two numbers together."""
        await ctx.send(left + right)

    # scientific af
    @bot.command(pass_context=True)  # done
    async def howgay(ctx, member: discord.User = None):
        """Check how gay someone is. Can be used for yourself."""
        guildid = ctx.guild.id

        complicatedcalc = strings.getrandomgay()

        if member:
            msg = langs.howgayyou_strings[isitallowed(guildid, ctx.author.id)].format(member, complicatedcalc)

        else:
            complicatedcalc = strings.getrandomgay()
            msg = langs.howgayi_strings[isitallowed(guildid, ctx.author.id)].format(complicatedcalc)

        ts = int(time.time())
        # await ctx.send('{0.name} joined in {0.joined_at}'.format(member))
        embed = discord.Embed(title=langs.gay2[isitallowed(guildid, ctx.author.id)], description=msg)
        await ctx.send(
            content="",
            embed=embed)


    # Choose one of 2 options someone provides.
    @bot.command(description='For when you wanna settle the score some other way')
    async def choose(ctx, *choices: str): # no need
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))


    # To get the date and time when a specific User joined.
    @bot.command()#done
    async def joined(ctx, member: discord.Member):
        """Says when a member joined."""
        guildid = ctx.guild.id

        ts = int(time.time())
        # await ctx.send('{0.name} joined in {0.joined_at}'.format(member))
        embed = discord.Embed(title=langs.join1[isitallowed(guildid, ctx.author.id)].format(member.name),
                              colour=discord.Colour(0x50e3c2),
                              timestamp=datetime.datetime.utcfromtimestamp(ts))
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=langs.join2[isitallowed(guildid, ctx.author.id)].format(member))

        embed.add_field(name=langs.join3[isitallowed(guildid, ctx.author.id)].format(member), value="{0.joined_at}".format(member))

        await ctx.send(
            content="",
            embed=embed)

    # If i was you, id disable this.
    @bot.command()
    async def console(ctx, *content: str):
        """Leave an message in the console. Don't spam folks."""
        guildid = ctx.guild.id
        authorid = ctx.author.id
        print(content, "{0}".format(ctx.author.name),  " {0}".format(authorid))
        await ctx.send(langs.console[isitallowed(guildid, ctx.author.id)])

    @bot.command()
    async def avatar(ctx, member: discord.User = None):
        """Gets an users avatar."""
        guildid = ctx.guild.id

        ts = int(time.time())
        if member:
            embed = discord.Embed(title=langs.avatar[isitallowed(guildid, ctx.author.id)].format(member.name),
                                  colour=discord.Colour(0x50e3c2),
                                  timestamp=datetime.datetime.utcfromtimestamp(ts))

            embed.set_image(url=member.avatar_url)

            await ctx.send(
                content="",
                embed=embed)
        else:
            await ctx.send(langs.avatarerror[isitallowed(guildid, ctx.author.id)])

    @bot.command()
    async def hw(ctx):
        """Displays how many days until it's halloween"""
        guildid = ctx.guild.id

        await ctx.send("There are {} days left until halloween.".format((settings.gethw() - datetime.date.today()).days))

    @bot.command()
    async def guess(ctx, guess=-1, max=10):

        guildid = ctx.guild.id
        answer = random.randint(1, max)
        if guess == -1:
            await ctx.send(langs.guessi_strings[isitallowed(guildid, ctx.author.id)])
            return
        if guess == answer:
            await ctx.send(langs.guesss_strings[isitallowed(guildid, ctx.author.id)])
        else:
            await ctx.send(langs.guessf_strings[isitallowed(guildid, ctx.author.id)].format(answer))

    @bot.command()
    async def isthisbotdown(ctx):
        await ctx.send(strings.getdownstring())

    @bot.command()
    async def kickme(ctx):
        guildid = ctx.guild.id
                    
        try:
            await ctx.send(langs.kickmes_strings[isitallowed(guildid, ctx.author.id)])
            await discord.guild.Member.kick(ctx.author)
        except Exception:
            await ctx.send(langs.kickmef_strings[isitallowed(guildid, ctx.author.id)])

    @bot.command()#why would i want that modular tho
    async def trump_dab(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/392794420610859013/497747996172353546/trump_dab.jpg")

    @bot.command()#modular
    async def cat(ctx):  
        ts = int(time.time())


        embed = discord.Embed(title="Cat gif",
                                colour=discord.Colour(0x50e3c2),
                                timestamp=datetime.datetime.utcfromtimestamp(ts))
        embed.set_image(url=webz.getkat())

        await ctx.send(
            content="",
            embed=embed)

    @bot.command()#modular
    async def dog(ctx):
        
        ts = int(time.time())

        embed = discord.Embed(title="Dog gif",
                                colour=discord.Colour(0x50e3c2),
                                timestamp=datetime.datetime.utcfromtimestamp(ts))
        embed.set_image(url=webz.getdoggo())

        await ctx.send(
            content="",
            embed=embed)

    @bot.command()
    async def source(ctx):
        await ctx.send(file=discord.File("source/source.zip"))


    @bot.command()
    async def slap(ctx, *, user):
        if user:
            temp = random.choice(strings.SLAP_TEMPLATES)
            item = random.choice(strings.ITEMS)
            hit = random.choice(strings.HIT)
            throw = random.choice(strings.THROW)

            repl = temp.format(user1="{}".format(ctx.author.name), user2="{}".format(user), item=item, hits=hit, throws=throw)
            await ctx.send(repl)
        else:
            temp = random.choice(strings.SLAP_TEMPLATES)
            item = random.choice(strings.ITEMS)
            hit = random.choice(strings.HIT)
            throw = random.choice(strings.THROW)

            repl = temp.format(user1="Jeff Nation", user2=ctx.author.name, item=item, hits=hit, throws=throw)
            await ctx.send(repl)




    @bot.command(name="serverinfo", pass_context=True, hidden=True)
    @has_permissions(manage_roles=True)
    async def _serverinfo(ctx):

        guildid = ctx.guild.id
        guild = ctx.guild
        ts = int(time.time())
        embed = discord.Embed(title=langs.si1[isitallowed(guildid, ctx.author.id)].format(guild.name),
                              colour=discord.Colour(0xaee38f),
                              description=langs.si2[isitallowed(guildid, ctx.author.id)],
                              timestamp=datetime.datetime.utcfromtimestamp(ts))
        image = discord.Guild.icon_url
        embed.set_author(name=guild.name)
        embed.set_footer(text=langs.si3[isitallowed(guildid, ctx.author.id)])

        embed.add_field(name=langs.si4[isitallowed(guildid, ctx.author.id)], value="{}".format(guild.created_at))
        embed.add_field(name=langs.si5[isitallowed(guildid, ctx.author.id)], value="{}".format(guild.member_count))
        embed.add_field(name=langs.si6[isitallowed(guildid, ctx.author.id)], value="{}".format(guild.afk_channel))
        embed.add_field(name=langs.si7[isitallowed(guildid, ctx.author.id)], value="{}".format(guild.default_role))
        embed.add_field(name=langs.si8[isitallowed(guildid, ctx.author.id)], value="{}".format(guild.roles))

        await ctx.author.send(
            content="",
            embed=embed)

    @bot.command()
    @has_permissions(manage_messages=True)
    async def setlang(ctx, value=0):
        if value=="english":
            try:
                os.remove("{}".format(ctx.author.id))
            except OSError:
                pass
            with open("{}".format(ctx.author.id), "a") as myfile:
                myfile.write("0".format(value))
                await ctx.send("I've set your preffered language to english!")
        if value=="german":
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
            if value==1:
                await ctx.send("I've set your preffered language to german!")
            else:
                await ctx.send("I've set your preffered language to english!")

    @bot.command()
    @has_permissions(manage_messages=True)
    async def specificlang(ctx, value=0):
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


class help: #done
    @bot.command()
    async def help(ctx, category="main"):
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
            embed.add_field(name=langs.helpbug1[isitallowed(guildid, ctx.author.id)], value=langs.helpbug2[isitallowed(guildid, ctx.author.id)])

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

            embed.add_field(name="jn specificlang", value=langs.ahlpban[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="jn serverinfo", value=langs.ahlserverinfo[isitallowed(guildid, ctx.author.id)]),

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

            embed.add_field(name="jn cat", value=langs.fhlpcat[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="jn dog", value=langs.fhlpdog[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="jn howgay", value=langs.fhlphowgay[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="jn runs", value=langs.fhlpruns[isitallowed(guildid, ctx.author.id)])
            embed.add_field(name="jn isthisbotdown", value=langs.fhlpisthis[isitallowed(guildid, ctx.author.id)])
            embed.add_field(name="jn guess", value=langs.fhlpguess[isitallowed(guildid, ctx.author.id)])

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

            embed.add_field(name="jn avatar", value=langs.ihlpavatar[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="jn joined", value=langs.ihlpjoined[isitallowed(guildid, ctx.author.id)]),

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

            embed.add_field(name="jn hw", value=langs.mhlphw[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="jn kickme", value=langs.mhlpkickme[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="jn console", value=langs.mhlpconsole[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="jn add", value=langs.mhlpadd[isitallowed(guildid, ctx.author.id)]),
            embed.add_field(name="jn choose", value=langs.mhlpchoose[isitallowed(guildid, ctx.author.id)]),

            await ctx.send(
                content="",
                embed=embed)
            return


class sudos:  # done
    @bot.command()
    @in_whitelist(sudo.SUDO_LIST)
    async def stestlang(ctx):
        guildid = ctx.author.id
        await ctx.send("{}".format(guildid))
        await ctx.send("PHASE 1 SUCCESS")
        settings.gettest(guildid) == guildid
        try:
            await ctx.send("PHASE 3 SUCCESS!")
            await ctx.send("ALL SYSTEMS OK")
        except Exception:
            await ctx.send("PHASE 3 FAILURE! settings.py DID NOT RECEIVE guildid")

    @bot.command()
    @in_whitelist(sudo.SUDO_LIST)
    async def stestlangext(ctx):
        guildid = ctx.auhtor.id
        await ctx.send("{}".format(guildid))
        await ctx.send("PHASE 1 SUCCESS")
        if settings.gettestext(guildid) == 0:
            try:
                await ctx.send("PHASE 3 SUCCESS!")
                await ctx.send("ALL SYSTEMS OK")
                await ctx.send("CONFIRMATION CODE: {}".format(settings.gettestext(guildid)))
            except Exception:
                await ctx.send("PHASE 3 FAILURE! settings.py DID NOT RECEIVE guildid")
            else:
                await ctx.send("PHASE 3 FAILURE! settings.py DID NOT RECEIVE guildid")



bot.run(TOKEN)
