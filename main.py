import json
from keep_alive import keep_alive
import time

# Start the keep_alive webserver
keep_alive()

# Load your bot’s json
with open("settings.json", "r") as f:
    data = json.load(f)

# Fake “bot loop” so Replit stays alive
while True:
    print("Bot is running with data:", data)
    time.sleep(60)  # wait 1 minute
