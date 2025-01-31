import os
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.json.sort_keys = False
CORS(app)

@app.route("/", methods=['GET'])
def hello_hng():
    return jsonify({
        "email": os.getenv("EMAIL", "default-email@example.com"),
        "current_datetime": datetime.now(timezone.utc).replace(tzinfo=None).isoformat(timespec="seconds") + "Z",
        "github_url": os.getenv("GITHUB_URL", "https://github.com/default-user/default-repo")
    }), 200

if __name__ == "__main__":
    app.run