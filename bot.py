import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import requests
import os

Client = discord.Client()
bot_prefix = "xh"
client = commands.Bot(command_prefix=bot_prefix)


@client.event
async def on_ready():


    print("Bot Online!")
    print(f"Name: {client.user.id}")
    print(f"ID: {client.user.id}")
    for s in client.guilds:
        print(f" - {s.name} ({s.id})")

    await client.change_presence(activity=discord.Game(name=f"mit seinem Programmierer cNite"))

@client.command()
async def ping(ctx):
   await ctx.send("Pong!")


@client.command()
async def magic8(ctx):
    ran = random.randint(0, 2)
    if ran == 0:
        await ctx.send("Yep!")
    if ran == 1:
        await ctx.send("Nope!")
    if ran == 2:
        await ctx.send("Maybe!")


@client.command()
async def bewerben(ctx):
    await ctx.send( "```Schreibe eine Bewerbung nach folgenden Kriterien:```"
                   "```Wie alt bist du?```"
                   "```Wie heißt du ingame?```"
                   "```RC Video Link (falls vorhanden)```"
                   "```Hast du earnings?```"
                   "```Warum wir?```"
                   "```Fortnite Tracker Link:```")




@client.command()
async def hilfe(ctx):
    await ctx.send("```                             Help Command                                                                                            "
                   "Der Bot hört auf den Prefix 'xh'                                                                                                                                                                                                                                                                        "
                   "xhbewerben, die Kriterien für die Bewerber                                                                                          "
                   "xhping, für ein echo                                                                                                                                                      "
                   "xhmagic8, damit du immer eine antwort bekommst ;D                                                                                   ```")



client.run(str(os.environ.get('BOT_TOKEN')))
