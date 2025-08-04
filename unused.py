# Unused functions for the Discord bot

# Unused function to auto-delete a message if a given string is in it
'''
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "bad word" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - don't use that word!")

    await bot.process_commands(message)
'''

# Unused commands to add / remove a given role
'''
@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=new_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} is now assigned to {new_role}")
    else:
        await ctx.send("Role doesn't exist")

@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=new_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} has had the {new_role} removed")
    else:
        await ctx.send("Role doesn't exist")
'''

# Unused DM command
'''
@bot.command()
async def dm(ctx, *, message):
    await ctx.author.send(f"You said {message}")
'''

# Unused reply command    
'''
@bot.command()
async def reply(ctx):
    await ctx.reply("This is a reply to your message!")
'''

# Unused command to create a poll
'''
@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="New Poll", description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")
'''
 
# Unused functions for dealing with role permission commands
"""
@bot.command()
@commands.has_role(new_role)
async def check_role(ctx):
    await ctx.send("You indeed have the {new_role} role!")

@check_role.error
async def check_role_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You do not the role required to do this!")
"""