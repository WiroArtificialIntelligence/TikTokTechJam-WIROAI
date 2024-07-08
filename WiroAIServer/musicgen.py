import requests
import os
from dotenv import load_dotenv

# Retrieve the API token stored in environment variables
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}


def generate_music(description):
    """
    Generate music based on a given description and return the audio in bytes.

    Args:
    description (str): The description to generate music, e.g., "Ambient, BPM 60-80, relaxing vibe."

    Returns:
    bytes: The audio data in bytes.
    """
    payload = {"inputs": description}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


# Example usage
# audio_bytes = generate_music("Ambient, BPM 60-80, and relaxing vibe.")
# save as a .wav file
# with open("output.wav", "wb") as f:
#     f.write(audio_bytes)
