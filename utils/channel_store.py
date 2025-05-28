import json
from config import CHANNELS_FILE

def load_channels():
    try:
        with open(CHANNELS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_channel(channel_id):
    channels = load_channels()
    if channel_id not in channels:
        channels.append(channel_id)
        with open(CHANNELS_FILE, 'w') as f:
            json.dump(channels, f)
