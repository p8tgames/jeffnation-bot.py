import asyncio
import os
import sys
import discord
from discord.ext import commands
from modules import *
from cogs.hs import *
import glob

files_only = glob.glob("cogs/" + '*.py')

for file in files_only:
    if "__" in file:
        pass
    else:
        filetoimport = file.replace("/", ".")
        filetoimport = filetoimport.replace(".py", "")
        print(filetoimport)


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
                # disallowed to have specific user languages
                return 0

    else:
        # not specified by server owner, assuming its set to yes
        return settings.getlang(authorid)


if not sys.version_info[:2] >= (3, 5):
    print("Error: requires python 3.5.2 or newer")
    exit(1)


async def status_task():  # This is the thing that loops in between different "now playing" states to show info
    while True:
        activity = discord.Game(name="with an Server near you", type=1)
        await bot.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name="if you do j!help", type=1)
        await bot.change_presence(status=discord.Status.idle, activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name="with contributers!", type=1)
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=activity)
        await asyncio.sleep(10)


description = '''Rewritten Version of FuckTardBot, now called JeffNation
You may contact the owner (using j!console) if an issue
was found.'''
bot = commands.Bot(command_prefix='j!',
                   description=description)
# here we set up the bots prefix. the description is
# unused as its only used in the stock help page, we use an custom one

bot.remove_command(
    'help')  # Removing the stock help command for our custom solution. Also it looks messy compared to ours

TOKEN = token.gettoken()  # defining token using the added token.py inside the modules folder


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


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, NotInWhiteList):
        await ctx.author.send(error)
    print(error)


for file in files_only:
    if "__" in file:
        pass
    else:
        filetoimport = file.replace("/", ".")
        filetoimport = filetoimport.replace(".py", "")
        print(filetoimport)
        bot.load_extension(filetoimport)
        print("Succesfully loaded {}!".format(filetoimport.split(".")[1]))

bot.run(TOKEN)
