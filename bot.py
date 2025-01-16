import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!",intents=intents)
bot.remove_command('help')

TOKEN = os.getenv("TOKEN")

@bot.event
async def on_ready():
    bot_intro = [
        "started"
    ]
    for intro_of_bot in bot_intro:
        print("Bot...".ljust(11) + intro_of_bot)

bot.run(TOKEN)