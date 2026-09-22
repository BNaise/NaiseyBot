import os
import random

import discord
from discord.ext import commands
from discord import app_commands, Interaction
from dotenv import load_dotenv

import funcs

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
ralsei_heart = "<:ralsei_heart:1547658659121602652>"

bot: commands.Bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

    await bot.tree.sync()
    print(f"Synced commands for {bot.user}")

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

@bot.tree.command(name="hello", description="Say hello")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def say_hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hi there! ^^ {ralsei_happy}")


@bot.tree.command(name="printer", description="Prints what you say")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(printer="Type whatever you want to print :3")
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)


@bot.tree.command(name="support", description="Support my creator! ^^")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def embeder(interaction: discord.Interaction):
    embed = discord.Embed(title="Click here! :P", url="https://www.youtube.com/@b_naise", description="Please subscribe lol :P", color=discord.Color.from_str("#52f0ef"))
    embed.set_thumbnail(url="https://i.ibb.co/LX2MNMGJ/My-new-new-new-pfp-Final-one-Probably.png")
    embed.set_author(name="B. Naise", url="https://www.youtube.com/@b_naise", icon_url="https://i.ibb.co/LX2MNMGJ/My-new-new-new-pfp-Final-one-Probably.png")
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="hug", description="Send hugs! ^^")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(who="Who wants the huggiesss? ^^")
async def huger(interaction: discord.Interaction, who: discord.User):

    target = who.mention
    user = interaction.user.mention

    messages = \
    [
        f"{user} tightly hugs {target} :people_hugging:{kralsei_hug}{kralsei_hug_blushing}",
        f"{target} got absolutely loved and hugged by {user} {kralsei_hug}{kralsei_hug_blushing}{ralsei_heart}",
        f"{user} hugs {target} so much that they won't let go :people_hugging:{kralsei_hug}{kralsei_hug_blushing}",
        f"Hey {target}! {user} just sent you a ton of hugs! ^^ {kralsei_hug}{kralsei_hug_blushing}{ralsei_heart}",
        f"{user} gives {target} a big warm hug! {vulkin_happy}{kralsei_hug}",
        f"{user} wraps their arms around {target}! {kralsei_hug_blushing}",
        f"{user} gives {target} a much-needed hug! {kralsei_hug_blushing}{ralsei_happy}",
        f"{user} hugs {target} with all their might! {ralsei_happy}{kralsei_hug_blushing}",
        f"{user} pulls {target} into a cozy hug! {kralsei_hug_blushing}",
        f"{user} gives {target} a wholesome hug! {ralsei_happy}{kralsei_hug_blushing}{ralsei_heart}",
        f"{user} hugs {target}. Awwww! {ralsei_happy}{kralsei_hug}",
        f"HUG DETECTED! {user} has hugged {target}! {kralsei_hug}{ralsei_heart}",
        f"{user} launches themselves at {target} with a hug! {kralsei_hug_blushing}",
        f"{user} and {target} are temporarily trapped in a hug. {ralsei_happy}{kralsei_hug_blushing}",
        f"{user} sends a hug directly to {target}'s soul. {kralsei_hug_blushing}{ralsei_heart}",
        f"{user} hugs {target}. No escape. {ralsei_cute_evil}{kralsei_hug_blushing}"
    ]

    choice = random.choice(messages)

    if target == user:
        await interaction.response.send_message(f"{user} gave themselves a hug")
    else:
        await interaction.response.send_message(choice)


@bot.tree.command(name="praise", description="Praises the targeted person")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(who="Who to praise? :3")
async def praiser(interaction: discord.Interaction, who: discord.User):

    target = who.mention

    user = interaction.user.mention

    messages = \
    [
        f"Hehe ^^\n{target} is such a cutie! ^^ {ralsei_happy}",
        f"Awwwww :3\n{target} is soooo cute! :33 {ralsei_cute}",
        f"{target}! you are so adorable! :3 {ralsei_cute}",
        f"{target}! you are sooo awesome! :3 {ralsei_happy}",
        f"Awwwww! :3 isn't {target} sooooo cute? {ralsei_happy}",
        f"{target} is so cute! :3 {ralsei_cute}",
        f"{target} is so cute that I can hug them endlessly! {ralsei_happy}",
        f"{target} is such a cutie patooti :3 {ralsei_happy}"
    ]

    choice = random.choice(messages)

    if target == user:
        await interaction.response.send_message(f"{user} gave themselves a hug")
    else:
        await interaction.response.send_message(choice)


@bot.tree.command(name="deltarot", description="Says Deltarots")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def deltarot(interaction: discord.Interaction):
    deltarots = \
    [
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


@bot.tree.command(name="gamble", description="Let's go gambling!")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def gamble(interaction: discord.Interaction):
    gamble = \
    [
        "I can't stop winning!",
        "Aww dang it!"
    ]
    await interaction.response.send_message(random.choice(gamble))


@bot.tree.command(name="silly", description="Silly :P")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(who="Who to silly? ^?^")
async def silliness(interaction: discord.Interaction, who: discord.User = None):

    user = interaction.user.mention

    if not who:
        silly = \
            [
                 "Bleh",
                 "Meow :3",
                 "Mrewwww :3",
                 "Nyaaaaa~",
                 "Nyon!",
                 "Ueueleuleuleue!",
                 f"{kris_wiggle}"
            ]
    else:
        target = who.mention
        silly = \
            [
                 f"Ummmm {target}! {user} is purring at you {ralsei_happy}",
                 f"Hehe {target}! {user} is meowing at you :3 {ralsei_happy}",
                 f"{user} is meowing at {target}! ~ ^w^ ~",
                 f"{target} is getting nuzzled by {user} {kralsei_hug_blushing}",
                 f"{user} is gently patting {target}'s head {ralsei_happy}",
                 f"{target}! {user} tackles you with a hug :3 {ralsei_happy}{kralsei_hug}"
            ]

    choice = random.choice(silly)

    await interaction.response.send_message(choice)

@bot.tree.command(name="permahug", description="Permanently hug someone ^^")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(who="Who wants to be perma hugged ^?^")
async def perma_huger(interaction: discord.Interaction, who: discord.User):

    target = who.mention
    user = interaction.user.mention

    messages = \
    [
        f"{user} permanently hugs {target} {kralsei_hug}{kralsei_hug_blushing}",
        f"{user} hugs {target} permanently {kralsei_hug_blushing}",
        f"{user} hugs {target} and they won't let go, ever {kralsei_hug_blushing}",
        f"{user} hugs {target} and never let's go until the end of time and beyond {kralsei_hug_blushing}",
        f"{user} has trapped {target} with an eternal hug {kralsei_hug}"
    ]

    choice = random.choice(messages)

    if user == target:
        await interaction.response.send_message(f"{user} you can't just do that!")
    else:
        await interaction.response.send_message(choice)

@bot.tree.command(name="hugeveryone", description="Hugs everyone ^^")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def hug_everyone(interaction: discord.Interaction):

    user = interaction.user.mention

    messages = \
    [
        f"{user} tightly hugs @everyone :people_hugging:{kralsei_hug}{kralsei_hug_blushing}",
        f"Hey @everyone! {user} just sent you guys a ton of hugs! ^^ {ralsei_heart}{kralsei_hug_blushing}{ralsei_happy}",
        f"{user} gives @everyone a big warm hug! {vulkin_happy}{kralsei_hug}",
        f"{user} wraps their arms around @everyone! {kralsei_hug_blushing}",
        f"{user} gives @everyone a much-needed hug! {kralsei_hug_blushing}{ralsei_happy}{ralsei_heart}",
        f"{user} hugs @everyone with all their might! {ralsei_happy}{kralsei_hug_blushing}",
        f"{user} pulls @everyone into a cozy hug! {kralsei_hug_blushing}",
        f"{user} gives @everyone a wholesome hug! {ralsei_happy}{kralsei_hug_blushing}",
        f"{user} hugs @everyone. Awwww! {ralsei_happy}{kralsei_hug}{ralsei_heart}",
        f"HUG DETECTED! {user} has hugged @everyone! {kralsei_hug}",
        f"{user} and @everyone are temporarily trapped in a hug. {ralsei_happy}{kralsei_hug_blushing}",
        f"{user} sends a hug directly to @everyone's soul. {kralsei_hug_blushing}{ralsei_heart}",
        f"{user} hugs @everyone. No escape. {ralsei_cute_evil}{kralsei_hug_blushing}"
    ]

    choice = random.choice(messages)

    await interaction.response.send_message(choice)

@bot.tree.command(name="calculate", description="Type equations to calculate")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(equation="Type \"list\" to get a list of functions")
async def calculator(interaction: discord.Interaction, equation: str):
    if equation == "9+10":
        await interaction.response.send_message(f"{equation} =\n21")
    elif equation == "9 + 10":
        await interaction.response.send_message(f"{equation} =\n21")
    else:
        try:
          await interaction.response.send_message(f"{equation} =\n{funcs.calculate(equation)}")
        except Exception as e:
          await interaction.response.send_message(f"Error: {e}")

@bot.tree.command(name="bored", description="Bored -_-")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def say_hello(interaction: discord.Interaction):
    file = discord.File("files/bernii_bored.gif")
    await interaction.response.send_message(file=file)

@bot.tree.command(name="roll", description="Rolls a random number between the Starting number and Finishing number")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(start="Enter starting number (default is 1)")
@app_commands.describe(finish="Enter finishing number")
async def roll(interaction: discord.Interaction, finish: int, start: int = 1):
    if finish:
        if finish >= start:
            random_number = random.randint(start, finish)
            await interaction.response.send_message(str(random_number))
        elif finish < start:
            await interaction.response.send_message("Finishing number should be bigger then starting number.")
    else:
        await interaction.response.send_message("Please enter a number")

@bot.tree.command(name="kiss", description="Kiss :3")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(who="Who to kiss? :3")
async def kiss(interaction: discord.Interaction, who: discord.User):
    user = interaction.user.mention

    target = who.mention

    messages = \
        [
            f"{user} kissed {target}! They're so cute! {ralsei_happy}",
            f"OMG- GUYS- {user} JUST KISSED {target}!!!! {ralsei_cute}",
            f"{user} **VIOLENTLY** pulled {target} to them and **SMOOCHED** them on the **LIPS**, not letting **ANYONE ELSE** in {ralsei_cute_evil}",
            f"Hehehehe, {user} gave {target} a little smooooch! {ralsei_happy}"
        ]

    choice = random.choice(messages)

    if target == user:
        await interaction.response.send_message(f"{user} kissed themselves? ...how? {ralsei_shocked}")
    elif who:
        await interaction.response.send_message(choice)

@bot.tree.command(name="cheekkiss", description="Cheek kiss :3")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(who="Who to cheek kiss? :3")
async def kiss(interaction: discord.Interaction, who: discord.User):
    user = interaction.user.mention

    target = who.mention

    messages = \
        [
            f"{user} gave {target} a cute kiss on the cheek! Awwhh! :3 {ralsei_happy}",
            f"{user} gave {target} a little cheek smooch! ^^ {ralsei_happy}",
            f"{user} not so violently pulled {target} to them and pekced them on the cheek, letting everyone else in ^w^ {ralsei_happy}",
            f"Hey guys, {user} gave {target} a little cheek smooch!!! :3 {ralsei_cute}",
            f"Hehehe {user} is so cute, they just kissed {target} on the cheek ^^ {ralsei_cute}",
            f"Hehehe- {user} gave {target} a peck on the cheek!!!! :3 {ralsei_heart}"
        ]

    choice = random.choice(messages)

    if target == user:
        await interaction.response.send_message(f"{user} kissed themselves on the cheek? ...how? {ralsei_shocked}")
    elif who:
        await interaction.response.send_message(choice)

funcs.keep_alive()

bot.run(os.getenv('DISCORD_TOKEN'))