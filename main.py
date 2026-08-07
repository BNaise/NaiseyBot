import os
import random

import discord
from discord.ext import commands
from discord import app_commands, Interaction
from dotenv import load_dotenv

import keepalive

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# 1496213896552513708 The Digital world
# 1515429501239169104 Testing

server_id = 1515429501239169104

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            guild = discord.Object(id=server_id)
            synced = await self.tree.sync(guild=guild)
            print(f"Synced {len(synced)} commands to guild {guild.id}")

        except Exception as e:
            print(f"Error syncing commands: {e}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if client.user in message.mentions:
            await message.channel.send(":3")

    # async def on_reaction_add(self, reaction, user):
    #     await reaction.message.channel.send(reaction)

    # async def on_message_edit(self, before, after):
    #     await after.channel.send(f"Message edited by {after.author}\n"
    #                              f"Before: {before.content}\n"
    #                              f"After: {after.content}")

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=server_id)


@client.tree.command(name="hello", description="Say hello", guild=GUILD_ID)

async def say_hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there!")

@client.tree.command(name="printer", description="Prints what you say", guild=GUILD_ID)

async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

@client.tree.command(name="embed", description="Embed demo", guild=GUILD_ID)

async def embeder(interaction: discord.Interaction):
    embed = discord.Embed(title="Title", url="https://www.youtube.com/@b_naise", description="Description", color=discord.Color.from_str("#52f0ef"))
    await interaction.response.send_message(embed=embed)

@client.tree.command(name="hug", description="Send hugs! ^^", guild=GUILD_ID)

async def printer(interaction: discord.Interaction, user: discord.Member):
    hug_messages = [
        f"{interaction.user.mention} tightly hugs {user.mention} :people_hugging:<:kralsei_hug:1534290578974445780><:kralsei_hug_blushing:1534290631114096690>",
        f"{user.mention} got absolutely loved and hugged by {interaction.user.mention} :people_hugging:<:kralsei_hug:1534290578974445780><:kralsei_hug_blushing:1534290631114096690>",
        f"{interaction.user.mention} hugs {user.mention} so much that they won't let go :people_hugging:<:kralsei_hug:1534290578974445780><:kralsei_hug_blushing:1534290631114096690>",
        f"Hey {user.mention}! {interaction.user.mention} just sent you a ton of hugs! ^^ :people_hugging:<:kralsei_hug:1534290578974445780><:kralsei_hug_blushing:1534290631114096690>"
    ]
    await interaction.response.send_message(random.choice(hug_messages))

@client.tree.command(name="praise", description="Praises the targeted person", guild=GUILD_ID)

async def praiser(interaction: discord.Interaction, user: discord.Member):
    praise_messages = [
        f"Hehe ^^\n{user.mention} is such a cutie! ^^",
        f"Awwwww :3\n{user.mention} is soooo cute! :33",
        f"{user.mention}! you are so adorable! :3",
        f"{user.mention}! you are sooo awesome! :3"
    ]
    await interaction.response.send_message(random.choice(praise_messages))

@client.tree.command(name="deltarot", description="Says Deltarots", guild=GUILD_ID)

async def deltarot(interaction: discord.Interaction):
    deltarots = [
        "JARONA!",
        "Freedom’s just a penumbra phantasm for big shots with black knives about the world revolving around the hammer of justice sealed away with cutie mew mew magic at the pirate dojo in my castle town during the sunset of seven suns.",
        "FREEDOM",
        "FRIEND",
        "GASTER",
        "https://cdn.discordapp.com/attachments/1496213900339843125/1534932644113027144/HPBzsS9asAASz6L.png?ex=6a75ecec&is=6a749b6c&hm=b5d38c85790492714f24afa703ee4e8937876f85f41a517a824dce215d67235f&"
    ]

    await interaction.response.send_message(random.choice(deltarots))

keepalive.keep_alive()

client.run(token)