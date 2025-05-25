from flask import Flask, jsonify, request,render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite peticiones desde otros orígenes (útil para frontends separados)

# 🔐 Simulamos obtener la API key de forma segura

@app.route("/")
def index():
    api_key = obtener_api_key()
    html = f"""
    <html>
    <head><title>Widget con EMMA</title></head>
    <body>
      <script
        src="https://bit.ly/grupochess-server"
        data-sm-api-key="{api_key}"
        data-sm-position="bottomRight"
        data-sm-greeting="Saluda a EMMA"
        data-sm-layout="fullFrame"
        data-sm-profile-picture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNZgOFYTqro2hjPTDFOJWMEiVv6C_Fo0Bz3Q&s"
      ></script>
    </body>
    </html>
    """
    return render_template_string(html)

def obtener_api_key():

    with open("api_key.txt", "r") as myfile:
        api_key = myfile.read()
    # En producción, esto puede venir de una base de datos, archivo seguro o variable de entorno
    return {
        "api_key": api_key
    }

@app.route('/get-api-key', methods=['GET'])
def get_api_key():
    return jsonify(obtener_api_key())

@app.route('/save-api-key', methods=['POST'])
def save_api_key():
    # Aquí podrías implementar la lógica para guardar la API key de forma segura
    apiKey= request.json.get('api_key')
    if not apiKey:
        return jsonify({"error": "API key is required"}), 400
    # Lógica para guardar la API key
    with open("api_key.txt", "w") as myfile:
        myfile.write(apiKey)
    
    # Por ejemplo, guardarla en una base de datos o archivo seguro
    return jsonify({"message": "API key saved successfully"}), 201
if __name__ == '__main__':
    app.run(debug=True, port=5000)
