from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "API is alive ✅",
        "status": "running"
    })

@app.route("/hello/<name>")
def hello(name):
    return jsonify({
        "message": f"Hello, {name} 😎"
    })

@app.route("/sum", methods=["POST"])
def sum_numbers():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    return jsonify({
        "result": a + b
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
