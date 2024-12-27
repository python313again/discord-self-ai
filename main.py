import discord
from discord.ext import commands
import asyncio
import lib

bot = commands.Bot(command_prefix="!", self_bot=True)


TARGET_CHANNEL_ID = 752025169048109067

@bot.event
async def on_message(message):
    
    if message.author == bot.user:
        return

    
    if message.channel.id == TARGET_CHANNEL_ID:
        
        
        slow_mode_delay = message.channel.slowmode_delay

        
        if slow_mode_delay > 0:
        
            await asyncio.sleep(slow_mode_delay)

        
        author_mention = message.author.mention
        
        
        sent = lib.send(message.content)

        if sent != "NULL":
            
            await message.channel.send(f"{author_mention} {sent}")

    await bot.process_commands(message)


bot.run("YOUR_BOT_TOKEN")
