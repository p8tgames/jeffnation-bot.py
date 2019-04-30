import platform
import os
import cogs.hs.setuplangs

brewinstallmacos = """/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" && """
presetregmacos = "pip3 install discord.py[voice]"
presetoptmacos = " && brew install ffmpeg"

presetoptlinux = " && sudo apt-get install libopus0 && sudo apt-get install ffmpeg"
presetreglinux = "pip3 install discord.py[voice] && sudo apt-get install libffi-devel"

presetregwindows = "pip3 install discord.py[voice]"




print("Setup-Script shipped with JeffNationBot. Installs all dependencies and sets up python for an easy start.\n PLEASE PROVIDE CREDIT WITHIN THE HELP PAGE WITH AN LINK TO OUR GITHUB REPO!")
os = platform.system()

print("What language do you want to use?/Welche Sprache möchtest du nutzen?\n0: English, 1: Deutsch")
choice1 = input("Select Language: ")
choice1 = int(choice1)

if choice1>1:
    print("Wrong language configured! Assuming english...")
    choice1=0

print(cogs.hs.setuplangs.welcome1[choice1])
print(cogs.hs.setuplangs.welcome2[choice1])
if os=="Linux":
    print(cogs.hs.setuplangs.detect[choice1].format("Linux"))
    det = 1
elif os=="Darwin":
    print(cogs.hs.setuplangs.detect[choice1].format("MacOS"))
    det = 2
elif os=="Windows":
    print(cogs.hs.setuplangs.detect[choice1].format("Windows"))
    det = 3


def Linux():
    print(cogs.hs.setuplangs.dtlinux[choice1])
    installation = input(cogs.hs.setuplangs.dtaccept[choice1])
    installation = int(installation)
    if installation == 0 or installation > 3:
        print("Out of range!")
        exit(2)
    else:
        if installation == 1:
            output = presetreglinux + presetoptlinux
        elif installation == 2:
            output = presetreglinux
        elif installation == 3:
            print("Aborted by user!")
            exit(0)

        print("-----------------------------------")
        print(output)
        print("-----------------------------------\n", cogs.hs.setuplangs.copypaste[choice1],
              "\n-----------------------------------")
        done = input(cogs.hs.setuplangs.executesucc[choice1])

        if done == "y":
            print(cogs.hs.setuplangs.grttoken[choice1])
            tokengen()
        if done == "n":
            print(cogs.hs.setuplangs.commanderror[choice1])
        else:
            print("Invalid input!")
            exit(1)


def MacOS():
    macbrew = input(cogs.hs.setuplangs.dtmacospre[choice1] + " ")
    if macbrew=="y":
        mcbr = 0
    elif macbrew=="n":
        mcbr = 1
    else:
        print("Illegal input!")
        exit(1)

    print(cogs.hs.setuplangs.dtmacos[choice1])
    installation = input(cogs.hs.setuplangs.dtaccept[choice1])
    installation = int(installation)
    if installation==0 or installation>3:
        print("Out of range!")
        exit(2)
    else:
        if installation==1:
            output = presetregmacos + presetoptmacos
        elif installation==2:
            output = presetregmacos
        elif installation==3:
            print("Aborted by user!")
            exit(0)

        if mcbr==1:
            output = brewinstallmacos + output
        else:
            output = output
        print("-----------------------------------")
        print(output)
        print("-----------------------------------\n", cogs.hs.setuplangs.copypaste[choice1], "\n-----------------------------------")
        done = input(cogs.hs.setuplangs.executesucc[choice1])

        if done=="y":
            print(cogs.hs.setuplangs.grttoken[choice1])
            tokengen()
        if done=="n":
            print(cogs.hs.setuplangs.commanderror[choice1])
        else:
            print("Invalid input!")
            exit(1)





def Windows():
    print(cogs.hs.setuplangs.dtlinux[choice1])
    installation = input(cogs.hs.setuplangs.dtaccept[choice1])
    installation = int(installation)
    if installation == 0 or installation > 3:
        print("Out of range!")
        exit(2)
    else:
        if installation == 1:
            input(cogs.hs.setuplangs.windowsffmpeg[choice1])
            output = presetregwindows
        elif installation == 2:
            output = presetreglinux
        elif installation == 3:
            print("Aborted by user!")
            exit(0)

        print("-----------------------------------")
        print(output)
        print("-----------------------------------\n", cogs.hs.setuplangs.copypaste[choice1],
              "\n-----------------------------------")
        done = input(cogs.hs.setuplangs.executesucc[choice1])

        if done == "y":
            print(cogs.hs.setuplangs.grttoken[choice1])
            tokengen()
        if done == "n":
            print(cogs.hs.setuplangs.commanderror[choice1])
        else:
            print("Invalid input!")
            exit(1)


def tokengen():
    print(cogs.hs.setuplangs.entertoken[choice1])
    token = input()
    print(cogs.hs.setuplangs.createfile[choice1])
    f = open('modules/token.py', 'w')
    f.write("""def gettoken():\n  token = "{}"\n  return token""".format(token))
    f.close()
    print(cogs.hs.setuplangs.done[choice1])
    print(cogs.hs.setuplangs.runb[choice1], "\n  python3 main.py")
    exit(10)


if det==1:
    Linux()
elif det==2:
    MacOS()
elif det==3:
    Windows()
