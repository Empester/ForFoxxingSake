import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import subprocess


load_dotenv()

# Basic config
GUILD_ID = 1322769222639816707
PREFIX = "!"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX), intents=intents)

#bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = os.getenv("TOKEN")

@bot.hybrid_command(name='ping', description="Returns latency.", with_app_command=True)
async def ping(ctx):
    latency = round(bot.latency*1000)
    await ctx.send(f"Ping: {latency}ms")

# Linux specific, remove if ran on windows
@bot.hybrid_command(name="stats", description="Returns the bot's stats.", with_app_command=True)
async def stats(ctx):
    result1 = subprocess.run(["uname"], capture_output=True, text=True)
    result2 = subprocess.run(["uname", "-n"], capture_output=True, text=True)
    await ctx.send(f"{result1.stdout}")



@bot.command(name='desync', description="Desyncs Guild_ID")
async def desync(ctx):
    guild = discord.Object(id=GUILD_ID)
    bot.tree.clear_commands(guild=guild)
    await bot.tree.sync(guild=guild)
    await ctx.send("bot.tree.clear_commands(guild=guild) was a success.")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if bot.user.mentioned_in(message) and message.content.strip() == bot.user.mention:
        await message.reply("What did you call me for?")
    if message.content.startswith(PREFIX):
        await bot.process_commands(message)
        
@bot.event
async def on_ready():
    bot_intro = [
        "started"
    ]
    for intro_of_bot in bot_intro:
        print("Bot...".ljust(11) + intro_of_bot)
    guild = discord.Object(id=GUILD_ID)
    bot.tree.copy_global_to(guild=guild)
    await bot.tree.sync(guild=guild)


# async def setup_hook():
#     guild = discord.Object(id=GUILD_ID)
#     bot.tree.copy_global_to(guild=guild)
#     await bot.tree.sync(guild=guild)

# bot.setup_hook=setup_hook
bot.run(TOKEN)
