from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timezone

app = Flask(__name__)
app.json.sort_keys = False
CORS(app)

@app.route("/", methods=['GET'])
def hello_hng():
    response_body = {
        "email" : "deedeesmith46@gmail.com",
        "current_datetime" : datetime.now(timezone.utc).isoformat(timespec="seconds") + "Z",
        "github_url" : "https://github.com/mariams58/Hng12_stage0"
    }
    return jsonify(response_body), 200

if __name__ == "__main__":
    app.run