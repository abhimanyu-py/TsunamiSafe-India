
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/risk")
def risk():
    return render_template("risk.html")

@app.route("/vulnerability")
def vulnerability():
    return render_template("vulnerability.html")

@app.route("/preparedness")
def preparedness():
    return render_template("preparedness.html")

@app.route("/emergency")
def emergency():
    return render_template("emergency.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/api/risk-calculator", methods=["POST"])
def risk_calculator():
    data = request.get_json(silent=True) or {}
    try:
        level = int(data.get("level", 1))
    except (TypeError, ValueError):
        return jsonify({"error": "Enter a valid level from 1 to 3"}), 400

    if level not in (1, 2, 3):
        return jsonify({"error": "Level must be 1, 2, or 3"}), 400

    labels = {1: "Lower", 2: "Moderate", 3: "Higher"}
    return jsonify({
        "level": labels[level],
        "message": (
            "This is a demonstration only, not a real tsunami forecast. "
            "Follow official warnings and evacuation instructions."
        )
    })

if __name__ == "__main__":
    app.run(debug=True)
