from flask import Flask
from threading import Thread

def try_except():
    try:
        guild = discord.Object(id=server_id)
        synced = await self.tree.sync(guild=guild)
        print(f"Synced {len(synced)} commands to guild {guild.id}")

    except Exception as e:
        print(f"Error syncing commands: {e}")

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8000)

def keep_alive():
    t = Thread(target=run)
    t.start()