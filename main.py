from flask import Flask, request, jsonify, render_template
from googletrans import Translator
from gtts import gTTS
import os

app = Flask(__name__)
translator = Translator()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    text = data.get('text')
    language = data.get('language')

    try:
        translation = translator.translate(text, dest=language)
        tts = gTTS(text=translation.text, lang=language)
        audio_file = f'static/output_{language}.mp3'
        tts.save(audio_file)

        return jsonify(audio_url=audio_file)
    except Exception as e:
        print(e)
        return jsonify(error=str(e)), 500


if __name__ == '__main__':
    app.run(debug=True)
