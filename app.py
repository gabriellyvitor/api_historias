from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuração da chave API da OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return "API de Geração de Histórias"

@app.route('/generate_story', methods=['POST'])
def generate_story():
    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )
        story = response.choices[0].text.strip()
        return jsonify({"story": story}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
