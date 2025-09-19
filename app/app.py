from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def ping():
    return jsonify(ok=True, service="jenkins-flask-starter")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
