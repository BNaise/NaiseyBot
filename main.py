import os
import random

import discord
from discord.ext import commands
from discord import app_commands, Interaction
from dotenv import load_dotenv

load_dotenv()

# server_id = 1496213896552513708 # The Digital world
# server_id = 1515429501239169104 # Testing
# server_id = 1516741859181989898 # Naise SMP
# server_id = 1504594980566732861 # Naise Server

# GUILD_ID = discord.Object(id=server_id)

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        await client.tree.sync()
        print(f"Synced commands for {client.user}")

        # async def try_except():
        #     try:
        #         guild = discord.Object(id=server_id)
        #         synced = await self.tree.sync(guild=guild)
        #         print(f"Synced {len(synced)} commands to guild {guild.id}")
        #
        #     except Exception as e:
        #         print(f"Error syncing commands: {e}")

        # await try_except()

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

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

@client.tree.command(name="hello", description="Say hello")

async def say_hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there! ^^")

@client.tree.command(name="printer", description="Prints what you say")

async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

@client.tree.command(name="support", description="Support my creator ^^")

async def embeder(interaction: discord.Interaction):
    embed = discord.Embed(title="B. Naise", url="https://www.youtube.com/@b_naise", description="Please subscribe lol :P", color=discord.Color.from_str("#52f0ef"))
    embed.set_thumbnail(url="https://i.ibb.co/LX2MNMGJ/My-new-new-new-pfp-Final-one-Probably.png")
    await interaction.response.send_message(embed=embed)

@client.tree.command(name="hug", description="Send hugs! ^^")

async def huger(interaction: discord.Interaction, user: discord.Member):

    hug_messages = [
        f"{interaction.user.mention} tightly hugs {user.mention} :people_hugging:<:kralsei_hug:1534290578974445780><:kralsei_hug_blushing:1534290631114096690>",
        f"{user.mention} got absolutely loved and hugged by {interaction.user.mention} :people_hugging:<:kralsei_hug:1534290578974445780><:kralsei_hug_blushing:1534290631114096690>",
        f"{interaction.user.mention} hugs {user.mention} so much that they won't let go :people_hugging:<:kralsei_hug:1534290578974445780><:kralsei_hug_blushing:1534290631114096690>",
        f"Hey {user.mention}! {interaction.user.mention} just sent you a ton of hugs! ^^ :people_hugging:<:kralsei_hug:1534290578974445780><:kralsei_hug_blushing:1534290631114096690>"
    ]

    choice = random.choice(hug_messages)

    if interaction.user == user:
        await interaction.response.send_message(f"{interaction.user.mention} gave themselves a hug")
    else:
        await interaction.response.send_message(choice)

@client.tree.command(name="praise", description="Praises the targeted person")

async def praiser(interaction: discord.Interaction, user: discord.Member):
    praise_messages = [
        f"Hehe ^^\n{user.mention} is such a cutie! ^^ <:ralsei_happy:1535296967486472263>",
        f"Awwwww :3\n{user.mention} is soooo cute! :33 <:ralsei_cute:1535297013518704680>",
        f"{user.mention}! you are so adorable! :3 <:ralsei_cute:1535297013518704680>",
        f"{user.mention}! you are sooo awesome! :3 <:ralsei_happy:1535296967486472263>",
        f"Awwwww! :3 isn't {user.mention} sooooo cute? <:ralsei_happy:1535296967486472263>",
        f"{user.mention} is so cute! :3 <:ralsei_cute:1535297013518704680>",
        f"{user.mention} is so cute that I can hug them endlessly! <:ralsei_happy:1535296967486472263>",
        f"{user.mention} is such a cutie patooti :3 <:ralsei_happy:1535296967486472263>"
    ]
    await interaction.response.send_message(random.choice(praise_messages))

@client.tree.command(name="deltarot", description="Says Deltarots")

async def deltarot(interaction: discord.Interaction):
    deltarots = [
        "JARONA!",
        "Freedom’s just a penumbra phantasm for big shots with black knives about the world revolving around the hammer of justice sealed away with cutie mew mew magic at the pirate dojo in my castle town during the sunset of seven suns.",
        "FREEDOM",
        "FRIEND",
        "GASTER",
        "PENUMBRA PHANTASM",
        "Friend inside me!",
        "BIG SHOT",
        "Papyrus is the roaring knight trust",
        "Always bet on papyrus knight!",
        "DECEMBER",
        "Yeah... the WORLD is kinda REVOLVING...",
        "Mike...",
        "1997",
        "1225",
        "Rip Onion :'(",
        "HERE I COME SANFRANDISCOOOOOOOO!",
        "SUSTINGUS",
        "Hey guys, I think I found a glue!",
        "Mysterious wind",
        "Hey i think this kinda took a weird route.",
        "Human... I remember... You're genocides...",
        "Hey undyne!\nHow many human souls do we need to break the barrier?"
    ]

    choice = random.choice(deltarots)

    if choice == "Hey undyne!\nHow many human souls do we need to break the barrier?":
        file = discord.File("files/undyne-seven.webp")
        await interaction.response.send_message(choice, file=file)
    else:
        await interaction.response.send_message(choice)

@client.tree.command(name="gamble", description="Let's go gambling!")

async def gamble(interaction: discord.Interaction):
    gamble = ["I can't stop winning!",
              "Aww dang it!"]
    await interaction.response.send_message(random.choice(gamble))

client.run(os.getenv('DISCORD_TOKEN'))