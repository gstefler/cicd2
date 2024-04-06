from flask import Flask
import math

app = Flask(__name__)


@app.route("/health")
def health():
    return "OK"


@app.route("/")
def hello_world():
    return math.pi


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
