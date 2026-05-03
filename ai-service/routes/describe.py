from flask import Blueprint, request, jsonify
from services.prompt_loader import load_prompt
from services.groq_client import call_groq
import json

describe_bp = Blueprint("describe", __name__)

@describe_bp.route("/describe", methods=["POST"])
def describe():
    data = request.json
    text = data.get("text")

    if not text:
        return {"error": "Invalid input"}, 400

    prompt = load_prompt("describe_prompt.txt", text)
    ai_response = call_groq(prompt)

    # Try to convert string → JSON
    try:
        parsed = json.loads(ai_response)
        return jsonify(parsed)
    except Exception:
        # fallback if model returns extra text
        return jsonify({"raw_response": ai_response})