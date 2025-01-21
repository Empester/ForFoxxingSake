import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

GUILD_ID = 1322769222639816707

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents)
#bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = os.getenv("TOKEN")

@bot.hybrid_command(name='ping', description="Returns latency.", with_app_command=True)
async def ping(ctx):
    latency = round(bot.latency*1000)
    await ctx.send(f"Ping: {latency}ms")

@bot.command(name='nvim', description="Replies with a sentence")
async def nvim(ctx):

    await ctx.reply("I use nvim btw")

@bot.command(name='desync', description="Desyncs Guild_ID")
async def desync(ctx):
    guild = discord.Object(id=GUILD_ID)
    bot.tree.clear_commands(guild=guild)
    await bot.tree.sync(guild=guild)
    await ctx.send("bot.tree.clear_commands(guild=guild) was a success.")


@bot.event
async def on_mention(ctx,message):
    if message.author.bot == False and bot.user.mentioned_in(message) and len(message.content) == len(bot.user.mention)+1:
        await ctx.reply("Yes, I do indeed can respond to you.")
    else:
        return

@bot.event
async def on_ready():
    bot_intro = [
        "started"
    ]
    for intro_of_bot in bot_intro:
        print("Bot...".ljust(11) + intro_of_bot)


async def setup_hook():
    guild = discord.Object(id=GUILD_ID)
    bot.tree.copy_global_to(guild=guild)
    await bot.tree.sync(guild=guild)

bot.setup_hook=setup_hook
bot.run(TOKEN)
