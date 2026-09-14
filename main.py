import os
import random

import discord
from discord.ext import commands
from discord import app_commands, Interaction
from dotenv import load_dotenv

import keep_alive

import re
import math

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

def calculate(expr):
    if expr.strip().lower() == "list":
        return "\n".join([
            "+  -  *  /  x  ^",
            "sqrt(x)",
            "sin(x)  cos(x)  tan(x)          [radians]",
            "asin(x) acos(x) atan(x)         [radians]",
            "sind(x) cosd(x) tand(x)         [degrees]",
            "asind(x) acosd(x) atand(x)      [degrees]",
            "sinh(x) cosh(x) tanh(x)",
            "log(x) log(x, base) log10(x) log2(x)",
            "exp(x)",
            "abs(x)",
            "factorial(x)",
            "round(x) round(x, n)",
            "floor(x) ceil(x)",
            "gcd(a, b) lcm(a, b)",
            "hypot(a, b)",
            "mod(a, b)",
            "min(a, b, ...) max(a, b, ...)",
            "deg(x) rad(x)",
            "pi  e",
        ])
    expr = expr.replace('x', '*').replace('X', '*').replace('^', '**')
    if not re.fullmatch(r'[\d+\-*/().\s^a-zA-Z,]+', expr):
        raise ValueError("Invalid characters in expression")
    allowed_names = {
        "sqrt": math.sqrt,
        # radians (standard)
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "asin": math.asin,
        "acos": math.acos,
        "atan": math.atan,
        # degrees
        "sind": lambda x: math.sin(math.radians(x)),
        "cosd": lambda x: math.cos(math.radians(x)),
        "tand": lambda x: math.tan(math.radians(x)),
        "asind": lambda x: math.degrees(math.asin(x)),
        "acosd": lambda x: math.degrees(math.acos(x)),
        "atand": lambda x: math.degrees(math.atan(x)),
        # hyperbolic
        "sinh": math.sinh,
        "cosh": math.cosh,
        "tanh": math.tanh,
        "log": math.log,
        "log10": math.log10,
        "log2": math.log2,
        "exp": math.exp,
        "pi": math.pi,
        "e": math.e,
        "abs": abs,
        "factorial": math.factorial,
        "round": round,
        "floor": math.floor,
        "ceil": math.ceil,
        "gcd": math.gcd,
        "lcm": math.lcm,
        "hypot": math.hypot,
        "mod": lambda a, b: a % b,
        "min": min,
        "max": max,
        "deg": math.degrees,
        "rad": math.radians,
    }
    return eval(expr, {"__builtins__": {}}, allowed_names)

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
@app_commands.describe(user="Who wants the huggiesss? ^^")
async def huger(interaction: discord.Interaction, user: discord.User):
    hug_messages = [
        f"{interaction.user.mention} tightly hugs {user.mention} :people_hugging:{kralsei_hug}{kralsei_hug_blushing}",
        f"{user.mention} got absolutely loved and hugged by {interaction.user.mention} {kralsei_hug}{kralsei_hug_blushing}{ralsei_heart}",
        f"{interaction.user.mention} hugs {user.mention} so much that they won't let go :people_hugging:{kralsei_hug}{kralsei_hug_blushing}",
        f"Hey {user.mention}! {interaction.user.mention} just sent you a ton of hugs! ^^ {kralsei_hug}{kralsei_hug_blushing}{ralsei_heart}",
        f"{interaction.user.mention} gives {user.mention} a big warm hug! {vulkin_happy}{kralsei_hug}",
        f"{interaction.user.mention} wraps their arms around {user.mention}! {kralsei_hug_blushing}",
        f"{interaction.user.mention} gives {user.mention} a much-needed hug! {kralsei_hug_blushing}{ralsei_happy}",
        f"{interaction.user.mention} hugs {user.mention} with all their might! {ralsei_happy}{kralsei_hug_blushing}",
        f"{interaction.user.mention} pulls {user.mention} into a cozy hug! {kralsei_hug_blushing}",
        f"{interaction.user.mention} gives {user.mention} a wholesome hug! {ralsei_happy}{kralsei_hug_blushing}{ralsei_heart}",
        f"{interaction.user.mention} hugs {user.mention}. Awwww! {ralsei_happy}{kralsei_hug}",
        f"{interaction.user.mention} has hugged {user.mention}. They are now legally required to be happy. {ralsei_happy}{kralsei_hug_blushing}",
        f"HUG DETECTED! {interaction.user.mention} has hugged {user.mention}! {kralsei_hug}{ralsei_heart}",
        f"{interaction.user.mention} launches themselves at {user.mention} with a hug! {kralsei_hug_blushing}",
        f"{interaction.user.mention} and {user.mention} are temporarily trapped in a hug. {ralsei_happy}{kralsei_hug_blushing}",
        f"{interaction.user.mention} sends a hug directly to {user.mention}'s soul. {kralsei_hug_blushing}{ralsei_heart}",
        f"{interaction.user.mention} hugs {user.mention}. No escape. {ralsei_cute_evil}{kralsei_hug_blushing}"
    ]

    choice = random.choice(hug_messages)

    if interaction.user == user:
        await interaction.response.send_message(f"{interaction.user.mention} gave themselves a hug")
    else:
        await interaction.response.send_message(choice)


@bot.tree.command(name="praise", description="Praises the targeted person")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(user="Who to praise? :3")
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


@bot.tree.command(name="deltarot", description="Says Deltarots")
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


@bot.tree.command(name="gamble", description="Let's go gambling!")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def gamble(interaction: discord.Interaction):
    gamble = ["I can't stop winning!",
              "Aww dang it!"]
    await interaction.response.send_message(random.choice(gamble))


@bot.tree.command(name="silly", description="Silly :P")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(user="Who to silly? ^?^")
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
                 f"Hehe {user.mention}! {interaction.user.mention} is meowing at you :3 {ralsei_happy}",
                 f"{interaction.user.mention} is meowing at {user.mention}! ~ ^w^ ~",
                 f"{user.mention} is getting nuzzled by {interaction.user.mention} {kralsei_hug_blushing}",
                 f"{interaction.user.mention} is gently patting {user.mention}'s head {ralsei_happy}",
                 f"{user.mention}! {interaction.user.mention} tackles you with a hug :3 {ralsei_happy}{kralsei_hug}"]

    choice = random.choice(silly)

    await interaction.response.send_message(choice)

@bot.tree.command(name="permahug", description="Permanently hug someone ^^")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(user="Who wants to be perma hugged ^?^")
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

@bot.tree.command(name="hugeveryone", description="Hugs everyone ^^")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def hug_everyone(interaction: discord.Interaction):

    hug_messages = \
    [
        f"{interaction.user.mention} tightly hugs @everyone :people_hugging:{kralsei_hug}{kralsei_hug_blushing}",
        f"Hey @everyone! {interaction.user.mention} just sent you guys a ton of hugs! ^^ {ralsei_heart}{kralsei_hug_blushing}{ralsei_happy}",
        f"{interaction.user.mention} gives @everyone a big warm hug! {vulkin_happy}{kralsei_hug}",
        f"{interaction.user.mention} wraps their arms around @everyone! {kralsei_hug_blushing}",
        f"{interaction.user.mention} gives @everyone a much-needed hug! {kralsei_hug_blushing}{ralsei_happy}{ralsei_heart}",
        f"{interaction.user.mention} hugs @everyone with all their might! {ralsei_happy}{kralsei_hug_blushing}",
        f"{interaction.user.mention} pulls @everyone into a cozy hug! {kralsei_hug_blushing}",
        f"{interaction.user.mention} gives @everyone a wholesome hug! {ralsei_happy}{kralsei_hug_blushing}",
        f"{interaction.user.mention} hugs @everyone. Awwww! {ralsei_happy}{kralsei_hug}{ralsei_heart}",
        f"HUG DETECTED! {interaction.user.mention} has hugged @everyone! {kralsei_hug}",
        f"{interaction.user.mention} and @everyone are temporarily trapped in a hug. {ralsei_happy}{kralsei_hug_blushing}",
        f"{interaction.user.mention} sends a hug directly to @everyone's soul. {kralsei_hug_blushing}{ralsei_heart}",
        f"{interaction.user.mention} hugs @everyone. No escape. {ralsei_cute_evil}{kralsei_hug_blushing}"
    ]

    choice = random.choice(hug_messages)

    await interaction.response.send_message(choice)

@bot.tree.command(name="calculate", description="Type equations to calculate")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(equation="Type \"list\" to get a list of functions")
async def calculator(interaction: discord.Interaction, equation: str):
    try:
      await interaction.response.send_message(f"{equation} =\n{calculate(equation)}")
    except Exception as e:
      await interaction.response.send_message(f"Error: {e}")

keep_alive.keep_alive()

bot.run(os.getenv('DISCORD_TOKEN'))