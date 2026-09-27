It's a silly little fluxer bot for silly little things like hugging and some silly deltarune joke stuff like flowery voice clips and deltarots etc.


## Deploying

This bot is built to run on [Render](https://render.com) (free tier works fine, with the usual caveat that free instances spin down after inactivity and take ~50s to wake back up, I recommend setting up uptimerobot for that which pings it every 5 minutes or so).

### 1. Fork/clone this repo

### 2. Create a Web Service on Render
- **New → Web Service**, connect this repo
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python main.py`

### 3. Set environment variables
In the service's **Environment** tab:
| Key | Value |
|---|---|
| `DISCORD_TOKEN` | Your Discord bot token |

### 5. Deploy
Render will auto-build and start the bot. Check the **Logs** tab for:
Bot is online! Logged in as <your bot's username>

### Running locally instead

pip install -r requirements.txt

Create a `.env` file:
DISCORD_TOKEN=your_bot_token

Then:
python main.py
