from flask import Flask, render_template, jsonify
from forensic_engine import analyze_events, load_sample_events

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/sample")
def sample_evidence():
    try:
        events = load_sample_events()
        return jsonify(analyze_events(events))
    except (OSError, ValueError, KeyError) as error:
        return jsonify({"error": str(error)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)