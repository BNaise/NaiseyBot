import os
import random

import discord
from discord.ext import commands
from discord import app_commands, Interaction
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# 1496213896552513708 The Digital world
# 1515429501239169104 Testing

server_id = 1496213896552513708

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

async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there!")

@client.tree.command(name="printer", description="Prints what you say", guild=GUILD_ID)

async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

@client.tree.command(name="embed", description="Embed demo", guild=GUILD_ID)

async def embeded(interaction: discord.Interaction):
    embed = discord.Embed(title="Title", url="https://www.youtube.com/@b_naise", description="Description", color=discord.Color.from_str("#52f0ef"))
    await interaction.response.send_message(embed=embed)

@client.tree.command(name="hug", description="Send hugs! ^^", guild=GUILD_ID)

async def printer(interaction: discord.Interaction, member: discord.Member):
    hug_messages = [
        f"{interaction.user.mention} tightly hugs {member.mention} :people_hugging:<:kralsei_hug:1534290578974445780><:kralsei_hug_blushing:1534290631114096690>",
        f"{member.mention} got absolutely loved and hugged by {interaction.user.mention} :people_hugging:<:kralsei_hug:1534290578974445780><:kralsei_hug_blushing:1534290631114096690>",
        f"{interaction.user.mention} hugs {member.mention} so much that they won't let go :people_hugging:<:kralsei_hug:1534290578974445780><:kralsei_hug_blushing:1534290631114096690>",
        f"Hey {member.mention}! {interaction.user.mention} just sent you a ton of hugs! ^^ :people_hugging:<:kralsei_hug:1534290578974445780><:kralsei_hug_blushing:1534290631114096690>"
    ]
    await interaction.response.send_message(random.choice(hug_messages))

@client.tree.command(name="praise", description="Praises the targeted person", guild=GUILD_ID)

async def printer(interaction: discord.Interaction, member: discord.Member):
    praise_messages = [
        f"Hehe ^^\n{member.mention} is such a cutie! ^^",
        f"Awwwww :3\n{member.mention} is soooo cute! :33",
        f"{member.mention}! you are so adorable! :3",
        f"{member.mention}! you are sooo awesome! :3"
    ]
    await interaction.response.send_message(random.choice(praise_messages))

client.run(token)