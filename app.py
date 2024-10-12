from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/validatePrompt', methods=['POST'])
def validate_prompt():
    data = request.get_json()
    prompt = data.get('prompt', '')
    
    # Lógica de validación (esto se puede personalizar según las reglas de validación)
    is_valid = len(prompt) > 20  # Ejemplo: el prompt debe tener más de 20 caracteres
    feedback = "El prompt es válido." if is_valid else "El prompt debe ser más específico y detallado."

    # Respuesta JSON
    return jsonify({
        "isValid": is_valid,
        "feedback": feedback
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)