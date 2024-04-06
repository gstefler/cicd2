from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/health")
def health():
    return "OK"

# return the user agent


@app.route("/")
def hello():
    return f"Hello, World! Your user agent is {request.headers.get('User-Agent')}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
