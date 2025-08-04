import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!!", intents=intents)

# Print statement indicating bot is online
@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} is active as of {datetime.now().strftime('%I:%M:%S %p')}.")

# Sends message if a user joins the server
@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server, {member.name}!")

# Hello message command
@bot.command(help="Phaelin says hello to the user", brief="Phaelin says hello")
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}!")

@bot.command(help="Deletes all messages in the bot testing grounds channel", brief="Deletes messages")
async def purge(ctx):
    required_role = "Orivar"

    # Only if user has "Orivar" role
    if not any(role.name == required_role for role in ctx.author.roles):
        await ctx.send("You don't have permission to use this command.")
        return
    
    # Checks to make sure the channel is correct
    if ctx.channel.id != 1385894699100930130:
        await ctx.send("This command can only be used in the appropriate channel.")
        return
    
    # Purge messages
    elif ctx.channel.id == 1385894699100930130:
        deleted = await ctx.channel.purge(limit=100)
        await ctx.send(f"Purged {len(deleted)} messages.", delete_after=5)

# Runs the bot
bot.run(token, log_handler=handler, log_level=logging.DEBUG)