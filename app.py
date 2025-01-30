from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def hello_hng():
    email = "deedeesmith4@gmail.com"
    current_datetime = datetime.now().isoformat()
    github_url = "https://github.com/mariams58/Hng12_stage0.git"
    return jsonify({
        'email': email,
        'current_datetime': current_datetime,
        'github_url': github_url
    })

if __name__ == "__main__":
    app.run
