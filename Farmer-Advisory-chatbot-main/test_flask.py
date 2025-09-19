from flask import Flask, render_template, request, jsonify, Response, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Flask is working!"

@app.route("/api/test", methods=["POST"])
def api_test():
    data = request.json
    return jsonify({"you_sent": data})

if __name__ == "__main__":
    app.run(debug=True)


