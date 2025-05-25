from flask import Flask, jsonify, request, render_template_string


app = Flask(__name__)

@app.route("/")
def index():
    api_key = obtener_api_key()
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>EMMA Bot</title>

        <!-- Tu script EMMA con la API key directamente -->
        <script
            src="https://bit.ly/grupochess-server"
            data-sm-api-key="eyJzb3VsSWQiOiJkZG5hLXVuaXRlZC1jbHViLW9yZy0tZXhwbG9yZXJjbGF1ZGlhMiIsImF1dGhTZXJ2ZXIiOiJodHRwczovL2RoLnNvdWxtYWNoaW5lcy5jbG91ZC9hcGkvand0IiwiYXV0aFRva2VuIjoiYXBpa2V5X3YxXzdjZGJiNzUyLTc2NjctNDA1ZS1hYzQzLWRjM2E0MTlhOWM1MSJ9"
            data-sm-position="bottomRight"
            data-sm-greeting="Saluda a Claudia"
            data-sm-layout="fullFrame"
            data-sm-profile-picture="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExd296cnUxYmx4MDE3eGxodzk0Y29iZXJiZzBseG96ZHJmZ294ZnFncSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Ts9N22K8Jz7GURYmNd/giphy.gif">
        </script>

    </head>
    <body>
        <h1>Hola desde EMMA 🤖</h1>
    </body>
    </html>
    """
    return render_template_string(html)

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
