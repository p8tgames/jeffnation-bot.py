#Hard coded settings. Can only be changed through heroku or by editing this file.
import datetime
from pathlib import Path
import os
from discord.ext import commands


def getlang(guildid):
    config = os.path.exists('./{}'.format(guildid))
    if config:
        fobj = open("{}".format(guildid))
        text = fobj.read().strip().split()
        # Conditions

        while True:
            s = "0"
            if s in text:
                lang = 0
                return lang
            else:
                lang = 1
                return lang

    else:
        return 0
    #else:
    #    with open("{}".format(guildid), "a") as myfile:
    #        myfile.write("0")
    #        lang = 0
    #        return lang

def getlanghlp(guildid):
    config = os.path.exists('./{}'.format(guildid))
    if config:
        fobj = open("{}".format(guildid))
        text = fobj.read().strip().split()
        # Conditions

        while True:
            s = "0"
            if s in text:
                lang = 0
                return lang
            else:
                lang = 1
                return lang

    else:
        return 0

def gettest(guildid):
    try:
        if guildid == guildid:
            print(guildid)
            return guildid
    except Exception:
        return "0"


def gettestext(guildid):
    #try:
    #    if guildid == guildid:
    #        with open("467442592158711809") as myfile:
    #            if '0' in myfile.read():
    #                lang = 0
    #                print("{}".format(lang))
    #                return lang
    #            else:
    #                if '1' in myfile.read():
    #                    lang = 1
    #                    print("{}".format(lang))
    #                    return lang
    #    else:
    #        return guildid
    #except Exception:
    #    return "-1"

    fobj = open("{}".format(guildid))
    text = fobj.read().strip().split()

    # Conditions
    try:
        while True:
            s = "0"  # Takes input of a string from user
            if s in text:  # string in present in the text file
                lang = 0
                return lang
            else:
                lang = 1
                return lang

    except Exception:
        lang = 0
        return lang



def gethw():
    halloween = datetime.date(2019, 10, 31)
    chistmas = datetime.date(2019, 12, 24)
    return halloween


def gbanget(aid):
    fobj = open("{}".format(aid))
    text = fobj.read().strip().split()

    # Conditions
    try:
        while True:
            s = "yes"  # Takes input of a string from user
            if s in text:  # string in present in the text file
                lang = "YES"
                return lang
            else:
                lang = "NO"
                return lang

    except Exception:
        lang = "NO"
        return lang








