from flask import Flask, jsonify, request, render_template_string

from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://theaihumans.com"}})
@app.route("/")

def index():
    return """
    <script
        src="https://bit.ly/grupochess-server"
        data-sm-api-key="eyJzb3VsSWQiOiJkZG5hLXVuaXRlZC1jbHViLW9yZy0tZXhwbG9yZXJjbGF1ZGlhMiIsImF1dGhTZXJ2ZXIiOiJodHRwczovL2RoLnNvdWxtYWNoaW5lcy5jbG91ZC9hcGkvand0IiwiYXV0aFRva2VuIjoiYXBpa2V5X3YxXzdjZGJiNzUyLTc2NjctNDA1ZS1hYzQzLWRjM2E0MTlhOWM1MSJ9"
        data-sm-position="bottomRight"
        data-sm-greeting="Saluda a Claudia"
        data-sm-layout="fullFrame"
        data-sm-profile-picture="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExd296cnUxYmx4MDE3eGxodzk0Y29iZXJiZzBseG96ZHJmZ294ZnFncSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Ts9N22K8Jz7GURYmNd/giphy.gif">
    </script>
    """


def obtener_api_key():
    with open("api_key.txt", "r") as myfile:
        return myfile.read().strip()  # Devuelve solo el string

@app.route('/get-api-key', methods=['GET'])
def get_api_key():
    return jsonify({"api_key": obtener_api_key()})

@app.route('/save-api-key', methods=['POST'])
def save_api_key():
    apiKey = request.json.get('api_key')
    if not apiKey:
        return jsonify({"error": "API key is required"}), 400
    with open("api_key.txt", "w") as myfile:
        myfile.write(apiKey)
    return jsonify({"message": "API key saved successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
