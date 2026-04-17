from telethon import TelegramClient, events
import os

# உன் விவரங்கள்
api_id = 21018564
api_hash = '8eb4e798cfabe336f65a3406f1fca52e'

client = TelegramClient('mariana_session', api_id, api_hash)

@client.on(events.NewMessage(incoming=True, func=lambda e: e.voice))
async def handle_voice_message(event):
    # வாய்ஸ் மெசேஜை டவுன்லோட் செய்கிறது
    path = await event.download_media()
    output = "war_voice.mp3"
    
    # FFmpeg மூலம் கரகரப்பு (Distortion) சேர்க்கிறது
    os.system(f"ffmpeg -i {path} -af 'volume=25dB, overdrive=15, acontrast=100' {output} -y")
    
    await event.respond("குரல் கரகரப்பாக மாற்றப்பட்டது! வார் மைக் தயார். 🔥")
    # இங்கே வாய்ஸ் சாட்டில் பிளே செய்யும் கமெண்ட் வரும் (pytgcalls தேவைப்படும்)
    # தற்காலிகமாக மாற்றப்பட்ட பைலை உனக்கே திருப்பி அனுப்புகிறேன், செக் பண்ணி பார்:
    await client.send_file(event.chat_id, output)
    os.remove(path)

print("Mariana Voice Changer Bot is running...")
client.start()
client.run_until_disconnected()
