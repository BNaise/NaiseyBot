import os
import random

import discord
from discord.ext import commands
from discord import app_commands, Interaction
from dotenv import load_dotenv

load_dotenv()

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

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        await client.tree.sync()
        print(f"Synced commands for {client.user}")

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
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def say_hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hi there! ^^ {ralsei_happy}")


@client.tree.command(name="printer", description="Prints what you say")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)


@client.tree.command(name="support", description="Support my creator ^^")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def embeder(interaction: discord.Interaction):
    embed = discord.Embed(title="Click here! :P", url="https://www.youtube.com/@b_naise", description="Please subscribe lol :P", color=discord.Color.from_str("#52f0ef"))
    embed.set_thumbnail(url="https://i.ibb.co/LX2MNMGJ/My-new-new-new-pfp-Final-one-Probably.png")
    embed.set_author(name="B. Naise", url="https://www.youtube.com/@b_naise", icon_url="https://i.ibb.co/LX2MNMGJ/My-new-new-new-pfp-Final-one-Probably.png")
    await interaction.response.send_message(embed=embed)


@client.tree.command(name="hug", description="Send hugs! ^^")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def huger(interaction: discord.Interaction, user: discord.User):
    hug_messages = [
        f"{interaction.user.mention} tightly hugs {user.mention} :people_hugging:{kralsei_hug}{kralsei_hug_blushing}",
        f"{user.mention} got absolutely loved and hugged by {interaction.user.mention} :people_hugging:{kralsei_hug}{kralsei_hug_blushing}",
        f"{interaction.user.mention} hugs {user.mention} so much that they won't let go :people_hugging:{kralsei_hug}{kralsei_hug_blushing}",
        f"Hey {user.mention}! {interaction.user.mention} just sent you a ton of hugs! ^^ :people_hugging:{kralsei_hug}{kralsei_hug_blushing}",
        f"{interaction.user.mention} gives {user.mention} a big warm hug! {vulkin_happy}{kralsei_hug}",
        f"{interaction.user.mention} wraps their arms around {user.mention}! {kralsei_hug_blushing}",
        f"{interaction.user.mention} gives {user.mention} a much-needed hug! {kralsei_hug_blushing}{ralsei_happy}",
        f"{interaction.user.mention} hugs {user.mention} with all their might! {ralsei_happy}{kralsei_hug_blushing}",
        f"{interaction.user.mention} pulls {user.mention} into a cozy hug! {kralsei_hug_blushing}",
        f"{interaction.user.mention} gives {user.mention} a wholesome hug! {ralsei_happy}{kralsei_hug_blushing}",
        f"{interaction.user.mention} hugs {user.mention}. Awwww! {ralsei_happy}{kralsei_hug}",
        f"{interaction.user.mention} has hugged {user.mention}. They are now legally required to be happy. {ralsei_happy}{kralsei_hug_blushing}",
        f"HUG DETECTED! {interaction.user.mention} has hugged {user.mention}! {kralsei_hug}",
        f"{interaction.user.mention} launches themselves at {user.mention} with a hug! {kralsei_hug_blushing}",
        f"{interaction.user.mention} and {user.mention} are temporarily trapped in a hug. {ralsei_happy}{kralsei_hug_blushing}",
        f"{interaction.user.mention} sends a hug directly to {user.mention}'s soul. {kralsei_hug_blushing}",
        f"{interaction.user.mention} hugs {user.mention}. No escape. {ralsei_cute_evil}{kralsei_hug_blushing}"
    ]

    choice = random.choice(hug_messages)

    if interaction.user == user:
        await interaction.response.send_message(f"{interaction.user.mention} gave themselves a hug")
    else:
        await interaction.response.send_message(choice)


@client.tree.command(name="praise", description="Praises the targeted person")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def praiser(interaction: discord.Interaction, user: discord.User):
    praise_messages = [
        f"Hehe ^^\n{user.mention} is such a cutie! ^^ {ralsei_happy}",
        f"Awwwww :3\n{user.mention} is soooo cute! :33 {ralsei_cute}",
        f"{user.mention}! you are so adorable! :3 {ralsei_cute}",
        f"{user.mention}! you are sooo awesome! :3 {ralsei_happy}",
        f"Awwwww! :3 isn't {user.mention} sooooo cute? {ralsei_happy}",
        f"{user.mention} is so cute! :3 {ralsei_cute}",
        f"{user.mention} is so cute that I can hug them endlessly! {ralsei_happy}",
        f"{user.mention} is such a cutie patooti :3 {ralsei_happy}"
    ]
    await interaction.response.send_message(random.choice(praise_messages))


@client.tree.command(name="deltarot", description="Says Deltarots")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
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
        "Hey undyne!\nHow many human souls do we need to break the barrier?",
        f"{gaster_dance}",
        f"{friend_inside_me}",
        f"CHAOS CHAOS! {jevil_dance}"
    ]

    choice = random.choice(deltarots)

    if choice == "Hey undyne!\nHow many human souls do we need to break the barrier?":
        file = discord.File("files/undyne-seven.webp")
        await interaction.response.send_message(choice, file=file)
    else:
        await interaction.response.send_message(choice)


@client.tree.command(name="gamble", description="Let's go gambling!")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def gamble(interaction: discord.Interaction):
    gamble = ["I can't stop winning!",
              "Aww dang it!"]
    await interaction.response.send_message(random.choice(gamble))


@client.tree.command(name="silly", description="Silly :P")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def silliness(interaction: discord.Interaction, user: discord.User = None):
    if not user:
        silly = ["Bleh",
                 "Meow :3",
                 "Mrewwww :3",
                 "Nyaaaaa~",
                 "Nyon!",
                 "Ueueleuleuleue!",
                 f"{kris_wiggle}"]
    else:
        silly = [f"Ummmm {user.mention}! {interaction.user.mention} is purring at you {ralsei_happy}",
                 f"{user.mention}! {interaction.user.mention} is pulling your hair {ralsei_cute_evil}",
                 f"{user.mention}! {interaction.user.mention} wants to.. eat you? {ralsei_shocked}"]

    choice = random.choice(silly)

    await interaction.response.send_message(choice)

@client.tree.command(name="permahug", description="Permanently hug someone ^^")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def perma_huger(interaction: discord.Interaction, user: discord.User):
    hug_messages = [
        f"{interaction.user.mention} permanently hugs {user.mention} {kralsei_hug}{kralsei_hug_blushing}",
        f"{interaction.user.mention} hugs {user.mention} permanently {kralsei_hug_blushing}",
        f"{interaction.user.mention} hugs {user.mention} and they won't let go, ever {kralsei_hug_blushing}",
        f"{interaction.user.mention} hugs {user.mention} and never let's go until the end of time and beyond {kralsei_hug_blushing}",
        f"{interaction.user.mention} has trapped {user.mention} with an eternal hug {kralsei_hug}"
    ]

    choice = random.choice(hug_messages)

    if interaction.user == user:
        await interaction.response.send_message(f"{interaction.user.mention} you can't just do that!")
    else:
        await interaction.response.send_message(choice)

@client.tree.command(name="hugeveryone", description="Hugs everyone ^^")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def hug_everyone(interaction: discord.Interaction):

    hug_messages = \
    [
        f"{interaction.user.mention} tightly hugs @everyone :people_hugging:{kralsei_hug}{kralsei_hug_blushing}",
        f"Hey @everyone! {interaction.user.mention} just sent you guys a ton of hugs! ^^ {kralsei_hug_blushing}{ralsei_happy}",
        f"{interaction.user.mention} gives @everyone a big warm hug! {vulkin_happy}{kralsei_hug}",
        f"{interaction.user.mention} wraps their arms around @everyone! {kralsei_hug_blushing}",
        f"{interaction.user.mention} gives @everyone a much-needed hug! {kralsei_hug_blushing}{ralsei_happy}",
        f"{interaction.user.mention} hugs @everyone with all their might! {ralsei_happy}{kralsei_hug_blushing}",
        f"{interaction.user.mention} pulls @everyone into a cozy hug! {kralsei_hug_blushing}",
        f"{interaction.user.mention} gives @everyone a wholesome hug! {ralsei_happy}{kralsei_hug_blushing}",
        f"{interaction.user.mention} hugs @everyone. Awwww! {ralsei_happy}{kralsei_hug}",
        f"HUG DETECTED! {interaction.user.mention} has hugged @everyone! {kralsei_hug}",
        f"{interaction.user.mention} and @everyone are temporarily trapped in a hug. {ralsei_happy}{kralsei_hug_blushing}",
        f"{interaction.user.mention} sends a hug directly to @everyone's soul. {kralsei_hug_blushing}",
        f"{interaction.user.mention} hugs @everyone. No escape. {ralsei_cute_evil}{kralsei_hug_blushing}"
    ]

    choice = random.choice(hug_messages)

    await interaction.response.send_message(choice)

client.run(os.getenv('DISCORD_TOKEN'))