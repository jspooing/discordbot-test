import discord
from discord.ext.commands import Bot
from discord.ext import commands 

Client=discord.Client()

bot_prefix=""
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print(client.user.name)
    print(client.user.id)
    print('-------------')

@client.command(pass_context=True)
async def 천둥아(ctx):
    await client.say("멍멍")


client.run("NDIxOTkxNDI5MTE2Nzg4NzQ3.DZzmRw.rMaeR_sNA5hx7h5SqNalHBvIsyY")
