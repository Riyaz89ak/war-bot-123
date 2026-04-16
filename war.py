from telethon import TelegramClient, events
import os

# உன்னுடைய விவரங்கள் இங்கே இணைக்கப்பட்டுள்ளன
api_id = 21018564
api_hash = '8eb4e798cfabe336f65a3406f1fca52e'

client = TelegramClient('mariana_session', api_id, api_hash)

print("Mariana War Machine is Connecting... 🔥")

@client.on(events.NewMessage(pattern='!war_on'))
async def start_war(event):
    await event.respond("வார் மைக் தயார்! 🎙️ அதிரடி ஆரம்பம்! 👊")

@client.on(events.NewMessage(pattern='!ping'))
async def ping(event):
    await event.respond("பாட் உயிரோடுதான் இருக்கு நண்பா! ⚡")

print("Bot is running...")
client.start()
client.run_until_disconnected()
