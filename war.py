from telethon import TelegramClient, events
import os

# உன் விவரங்கள்
api_id = 21018564
api_hash = '8eb4e798cfabe336f65a3406f1fca52e'

client = TelegramClient('mariana_session', api_id, api_hash)

@client.on(events.NewMessage(pattern='!ping'))
async def ping(event):
    await event.respond("ஆன்லைன்ல தான் இருக்கேன் நண்பா! ⚡")

@client.on(events.NewMessage(pattern='!war'))
async def start_war(event):
    await event.respond("வார் மைக் அதிரடி ஆரம்பம்! 🎙️👊")

print("Mariana Bot is starting...")
client.start()
client.run_until_disconnected()
