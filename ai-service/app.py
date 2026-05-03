from flask import Flask
from flask_cors import CORS
from routes.describe import describe_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(describe_bp)

@app.route("/")
def home():
    return {"message": "AI Service Running 🚀"}

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    print("Starting AI Service...")
    app.run(host="0.0.0.0", port=5002, debug=True)