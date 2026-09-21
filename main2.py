import os
import random
import re
import math
import cmath

import discord
from discord.ext import commands
from discord import app_commands, Interaction
from dotenv import load_dotenv

import keep_alive

# Emoji's
kralsei_hug = "<:kralsei_hug:1534290578974445780>"
kralsei_hug_blushing = "<:kralsei_hug_blushing:1534290631114096690>"
ralsei_happy = "<:ralsei_happy:1535296967486472263>"
ralsei_cute = "<:ralsei_cute:1535297013518704680>"
ralsei_laughing = "<:ralsei_laughing:1535297049098977361>"
ralsei_cute_evil = "<:ralsei_cute_evil:1535297118250467470>"
ralsei_shocked = "<:ralsei_shocked:1535297165231005777>"
kris_wiggle = "<a:kris_wiggle:1538120840720158740>"
driving_in_my_caaar = "<:driving_in_my_caaar:1538225748928761907>"
errrm = "<:errrm:1538225795703644160>"
mama_miba = "<:mama_miba:1538225824808046643>"
lancer = "<:lancer:1538225863462621215>"
dess_shocked = "<:dess_shocked:1538225908027105280>"
ralsei_splat = "<:ralsei_splat:1538225944005972128>"
spamton_dance = "<a:spamton_dance:1538226075916705834>"
YOUR_TAKING_TOO_LONG = "<:YOUR_TAKING_TOO_LONG:1538226123694145606>"
your_taking_too_long = "<:your_taking_too_long:1538226157046997062>"
vulkin_happy = "<:vulkin_happy:1538226201347498094>"
friend_inside_me = "<:friend_inside_me:1538226240799113216>"
the_final_starwalker = "<:the_final_starwalker:1538226301473783958>"
the_original_starwalker = "<:the_original_starwalker:1538226330045390918>"
tenna_dance = "<a:tenna_dance:1538226437235146762>"
tenna_dance_2 = "<a:tenna_dance_2:1538226501034709012>"
jevil_dance = "<a:jevil_dance:1538226552721117315>"
gaster_dance = "<a:gaster_dance:1538226632999833651>"
boooom = "<a:boooom:1538226668089376869>"
ralsei_heart = "<:ralsei_heart:1547658659121602652>"

def debug():
    load_dotenv()

    bot: commands.Bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

    server_id = 1515429501239169104

    guild_id = discord.Object(id=server_id)

    @bot.event
    async def on_ready():
        print(f'Logged on as {bot.user}!')

        try:
            guild = discord.Object(id=server_id)
            synced = await bot.tree.sync(guild=guild)
            print(f"Synced {len(synced)} commands to guild {guild.id}")

        except Exception as e:
            print(f"Error syncing commands: {e}")

        # async def on_message(self, message):
        #     if message.author == self.user:
        #         return
        #
        #     if client.user in message.mentions:
        #         await message.channel.send(":3")

        # async def on_reaction_add(self, reaction, user):
        #     await reaction.message.channel.send(reaction)

        # async def on_message_edit(self, before, after):
        #     await after.channel.send(f"Message edited by {after.author}\n"
        #                              f"Before: {before.content}\n"
        #                              f"After: {after.content}")

    @bot.tree.command(name="hello", description="Say hello", guild=guild_id)
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def say_hello(interaction: discord.Interaction):
        await interaction.response.send_message(f"Hi there! ^^ {ralsei_happy}")

    bot.run(os.getenv('DISCORD_TOKEN2'))