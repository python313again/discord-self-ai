import discord
from discord.ext import commands
import asyncio
import lib
import random

bot = commands.Bot(command_prefix="!", self_bot=True)

TARGET_CHANNEL_ID = 752025169048109067


last_message_time = None
in_cooldown = False

@bot.event
async def on_message(message):
    global last_message_time, in_cooldown

    
    if message.author == bot.user:
        return

    if message.channel.id == TARGET_CHANNEL_ID:
        
        slow_mode_delay = message.channel.slowmode_delay

        
        if slow_mode_delay > 0:
            
            if last_message_time is not None:
                time_diff = message.created_at - last_message_time
                
                if time_diff.total_seconds() < slow_mode_delay:
                    if not in_cooldown:
                        in_cooldown = True
                        print(f"Entering cooldown, waiting for {slow_mode_delay - time_diff.total_seconds()} seconds")
                    return
                else:
                    
                    in_cooldown = False

        
        if message.reference and message.reference.message_id:
            ref_message = await message.channel.fetch_message(message.reference.message_id)
            if ref_message.author == bot.user:
                print("Skipping, it's already my reply.")
                return

        
        author_mention = message.author.mention
        print(f"Processing message from {author_mention}: {message.content}")

        
        response = lib.send(message.author.id, message.content).lower()

        
        if "NULL".lower() not in response:
            await message.reply(response)
            last_message_time = message.created_at

    
    elif not in_cooldown and last_message_time is not None:
        time_since_last_message = (message.created_at - last_message_time).total_seconds()
        if time_since_last_message > 60:
            start_conversation_chance = 0.1 
            if random.random() < start_conversation_chance:
                await message.channel.send("hi")
                last_message_time = message.created_at

   
    await bot.process_commands(message)

bot.run("add bot token")