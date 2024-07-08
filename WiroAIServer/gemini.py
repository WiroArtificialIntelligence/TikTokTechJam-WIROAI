"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

from dotenv import load_dotenv
import os
import google.generativeai as genai


def generate_music_attributes(message):
    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    # Create the model
    # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    response = model.generate_content(
        [
            "Analyze the text and map it into music attributes(genre, bpm, and vibe). Don't include any explaination just answer in single sentence with genre, bpm, and vibe in it.",
            "Message: Morning: I was late for work and had to rush to catch the subway. Afternoon: I was super busy meeting with clients and working on other team projects. Evening: I met up with my friends and spent good quality time with them.",
            "Music Attribute: lofi jazz hiphop, slow tempo, chill",
            "Message: Morning: I went to the gym and had a good session! Afternoon: I went to two lectures. Evening: I was just chilling at my crib playing valorant.",
            "Music Attribute: indie, medium tempo, fulfilling",
            f"Message: ${message}",
            "Music Attribute: ",
        ]
    )

    return response.text
