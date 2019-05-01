from PIL import Image
from discord.ext import commands
import discord

template1 = (500, 550)
template2 = (232, 119)
template3 = (750, 427)
template4 = (360, 264)
template5 = (734, 635)


class memegen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cogtest(self, ctx):
        await ctx.send("This cog test is an success!")
        print(ctx.author.id)

    @commands.command()
    async def jpeg(self, ctx, url=''):
        if url == '':
            for attachment in ctx.message.attachments:
                if attachment.height:
                    await attachment.save("image.png")
                    filename = attachment.filename
                    filename = str(filename)
                    if filename.endswith(".png") or filename.endswith(".jpg" or ".jpeg"):
                        if filename.endswith(".png"):
                            extension = ".png"
                            await attachment.save("image" + extension)
                            im = Image.open("image.png")
                            im = im.convert('RGB')
                            im.save("image.jpg")
                        else:
                            extension = ".jpg"
                            await attachment.save("image" + extension)

                        image = Image.open("image.jpg")
                        image.save("imageout.jpg", quality=1, optimize=True)
                        await ctx.send(file=discord.File("imageout.jpg"))
                    else:
                        await ctx.send("Unsupported image!")
        else:
            await ctx.send("The owner was gonna work on adding URL support but he got lazy meh")

    @commands.command()
    async def whodidthis(self, ctx):
        for attachment in ctx.message.attachments:
            if attachment.height:
                filename = attachment.filename
                filename = str(filename)
                if filename.endswith(".png") or filename.endswith(".jpg" or ".jpeg"):
                    if filename.endswith(".png"):
                        extension = ".png"
                        await attachment.save("image" + extension)
                        im = Image.open("image.png")
                        im = im.convert('RGB')
                        im.save("image.jpg")
                    else:
                        extension = ".jpg"
                        await attachment.save("image" + extension)

                    image = Image.open("image.jpg")
                    image = image.resize(template1, Image.ANTIALIAS)
                    im2 = Image.open("cogs/templatesformemes/template1.png")
                    im2.paste(image)
                    im2.save("image.png")
                    await ctx.send(file=discord.File("image.png"))
                else:
                    await ctx.send("Unsupported image!")

    @commands.command()
    async def reggie(self, ctx):
        for attachment in ctx.message.attachments:
            if attachment.height:
                filename = attachment.filename
                filename = str(filename)
                if filename.endswith(".png") or filename.endswith(".jpg" or ".jpeg"):
                    if filename.endswith(".png"):
                        extension = ".png"
                        await attachment.save("image" + extension)
                        im = Image.open("image.png")
                        im = im.convert('RGB')
                        im.save("image.jpg")
                    else:
                        extension = ".jpg"
                        await attachment.save("image" + extension)

                    image = Image.open("image.jpg")
                    image = image.resize(template2, Image.ANTIALIAS)
                    im2 = Image.open("cogs/templatesformemes/template2.png")
                    im2.paste(image, (147, 292))
                    im2.save("image.png")
                    await ctx.send(file=discord.File("image.png"))
                else:
                    await ctx.send("Unsupported image!")

    @commands.command()
    async def cry(self, ctx):
        for attachment in ctx.message.attachments:
            if attachment.height:
                filename = attachment.filename
                filename = str(filename)
                if filename.endswith(".png") or filename.endswith(".jpg" or ".jpeg"):
                    if filename.endswith(".png"):
                        extension = ".png"
                        await attachment.save("image" + extension)
                        im = Image.open("image.png")
                        im = im.convert('RGB')
                        im.save("image.jpg")
                    else:
                        extension = ".jpg"
                        await attachment.save("image" + extension)

                    image = Image.open("image.jpg")
                    image = image.resize(template3, Image.ANTIALIAS)
                    im2 = Image.open("cogs/templatesformemes/template3.png")
                    image.paste(im2)
                    image.save("image.png")
                    await ctx.send(file=discord.File("image.png"))
                else:
                    await ctx.send("Unsupported image!")

    @commands.command()
    async def jacksvideos(self, ctx):
        for attachment in ctx.message.attachments:
            if attachment.height:
                filename = attachment.filename
                filename = str(filename)
                if filename.endswith(".png") or filename.endswith(".jpg" or ".jpeg"):
                    if filename.endswith(".png"):
                        extension = ".png"
                        await attachment.save("image" + extension)
                        im = Image.open("image.png")
                        im = im.convert('RGBA')
                        im.save("image.png")
                    else:
                        extension = ".jpg"
                        await attachment.save("image" + extension)
                        im = Image.open("image" + extension)
                        im = im.convert('RGBA')
                        im.save("image.png")

                    image = Image.open("image.png")
                    image = image.resize(template4, Image.ANTIALIAS)
                    im2 = Image.open("cogs/templatesformemes/template4.png")
                    im3 = Image.open("cogs/templatesformemes/template4.png")
                    im3 = im3.convert('RGBA')
                    im2.paste(image, (456, 351))
                    im2.paste(im3, (0, 0), im3)
                    im2.save("image.png")
                    await ctx.send(file=discord.File("image.png"))
                else:
                    await ctx.send("Unsupported image!")

    @commands.command()
    async def alex(self, ctx):
        for attachment in ctx.message.attachments:
            if attachment.height:
                filename = attachment.filename
                filename = str(filename)
                if filename.endswith(".png") or filename.endswith(".jpg" or ".jpeg"):
                    if filename.endswith(".png"):
                        extension = ".png"
                        await attachment.save("image" + extension)
                        im = Image.open("image.png")
                        im = im.convert('RGBA')
                        im.save("image.png")
                    else:
                        extension = ".jpg"
                        await attachment.save("image" + extension)
                        im = Image.open("image" + extension)
                        im = im.convert('RGBA')
                        im.save("image.png")

                    image = Image.open("image.png")
                    image = image.resize(template5, Image.ANTIALIAS)
                    im2 = Image.open("cogs/templatesformemes/template5.png")
                    im3 = Image.open("cogs/templatesformemes/template5.png")
                    im3 = im3.convert('RGBA')
                    im2.paste(image, (767, 0))
                    im2.paste(im3, (0, 0), im3)
                    im2.save("image.png")
                    await ctx.send(file=discord.File("image.png"))
                else:
                    await ctx.send("Unsupported image!")


def setup(bot):
    bot.add_cog(memegen(bot))
