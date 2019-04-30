from discord.ext import commands
import time
from modules import *
from cogs.hs import *
from cogs.hs import langs
import base64
from io import BytesIO
from PIL import Image
import random
import os
import datetime
import discord


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


class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def thonkify(self, ctx, *, meme):
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

    @commands.command()  # no need
    async def runs(self, ctx):
        """Gives out an random funny string."""
        await ctx.send(strings.getrunstring())

    # adds 2 numbers
    @commands.command()  # no need
    async def add(self, ctx, left: int, right: int):
        """Adds two numbers together."""
        await ctx.send(left + right)

    # scientific af
    @commands.command(pass_context=True)  # done
    async def howgay(self, ctx, member: discord.User = None):
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
    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, ctx, *choices: str):  # no need
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))

    # To get the date and time when a specific User joined.
    @commands.command()  # done
    async def joined(self, ctx, member: discord.Member):
        """Says when a member joined."""
        guildid = ctx.guild.id

        ts = int(time.time())
        # await ctx.send('{0.name} joined in {0.joined_at}'.format(member))
        embed = discord.Embed(title=langs.join1[isitallowed(guildid, ctx.author.id)].format(member.name),
                              colour=discord.Colour(0x50e3c2),
                              timestamp=datetime.datetime.utcfromtimestamp(ts))
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=langs.join2[isitallowed(guildid, ctx.author.id)].format(member))

        embed.add_field(name=langs.join3[isitallowed(guildid, ctx.author.id)].format(member),
                        value="{0.joined_at}".format(member))

        await ctx.send(
            content="",
            embed=embed)

    # If i was you, id disable this.
    @commands.command()
    async def console(self, ctx, *content: str):
        """Leave an message in the console. Don't spam folks."""
        guildid = ctx.guild.id
        authorid = ctx.author.id
        print(content, "{0}".format(self, ctx.author.name), " {0}".format(authorid))
        await ctx.send(langs.console[isitallowed(guildid, ctx.author.id)])

    @commands.command()
    async def avatar(self, ctx, member: discord.User = None):
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

    @commands.command()
    async def hw(self, ctx):
        """Displays how many days until it's halloween"""
        guildid = ctx.guild.id

        await ctx.send(
            "There are {} days left until halloween.".format((settings.gethw() - datetime.date.today()).days))

    @commands.command()
    async def guess(self, ctx, guess=-1, max=10):

        guildid = ctx.guild.id
        answer = random.randint(1, max)
        if guess == -1:
            await ctx.send(langs.guessi_strings[isitallowed(guildid, ctx.author.id)])
            return
        if guess == answer:
            await ctx.send(langs.guesss_strings[isitallowed(guildid, ctx.author.id)])
        else:
            await ctx.send(langs.guessf_strings[isitallowed(guildid, ctx.author.id)].format(answer))

    @commands.command()
    async def isthisbotdown(self, ctx):
        await ctx.send(strings.getdownstring())

    @commands.command()
    async def kickme(self, ctx):
        guildid = ctx.guild.id

        try:
            await ctx.send(langs.kickmes_strings[isitallowed(guildid, ctx.author.id)])
            await discord.guild.Member.kick(ctx.author)
        except Exception:
            await ctx.send(langs.kickmef_strings[isitallowed(guildid, ctx.author.id)])

    @commands.command()  # why would i want that modular tho
    async def trump_dab(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/392794420610859013/497747996172353546/trump_dab.jpg")

    @commands.command()  # modular
    async def cat(self, ctx):
        ts = int(time.time())

        embed = discord.Embed(title="Cat gif",
                              colour=discord.Colour(0x50e3c2),
                              timestamp=datetime.datetime.utcfromtimestamp(ts))
        embed.set_image(url=webz.getkat())

        await ctx.send(
            content="",
            embed=embed)

    @commands.command()  # modular
    async def dog(self, ctx):

        ts = int(time.time())

        embed = discord.Embed(title="Dog gif",
                              colour=discord.Colour(0x50e3c2),
                              timestamp=datetime.datetime.utcfromtimestamp(ts))
        embed.set_image(url=webz.getdoggo())

        await ctx.send(
            content="",
            embed=embed)

    @commands.command()
    async def source(self, ctx):
        await ctx.send("https://github.com/p8tgames/jeffnation-bot.py")

    @commands.command()
    async def slap(self, ctx, *, user):
        if user:
            temp = random.choice(strings.SLAP_TEMPLATES)
            item = random.choice(strings.ITEMS)
            hit = random.choice(strings.HIT)
            throw = random.choice(strings.THROW)

            repl = temp.format(user1="{}".format(self, ctx.author.name), user2="{}".format(user), item=item, hits=hit,
                               throws=throw)
            await ctx.send(repl)
        else:
            temp = random.choice(strings.SLAP_TEMPLATES)
            item = random.choice(strings.ITEMS)
            hit = random.choice(strings.HIT)
            throw = random.choice(strings.THROW)

            repl = temp.format(user1="Jeff Nation", user2=ctx.author.name, item=item, hits=hit, throws=throw)
            await ctx.send(repl)


def setup(bot):
    bot.add_cog(misc(bot))
