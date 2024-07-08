from flask import Flask, request, jsonify
from gemini import generate_music_attributes
from musicgen import generate_music
import base64

app = Flask(__name__)


@app.route("/", methods=["POST"])
def generate():
    data = request.get_json()
    message = data.get("message")

    if not message:
        return jsonify({"error": "No message provided"}), 400
    try:
        music_attributes = generate_music_attributes(message)
        audio_bytes = generate_music(music_attributes)
        audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
        return jsonify({"audio": audio_base64}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
