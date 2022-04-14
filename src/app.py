import socket
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h3>Hello World from a Flask app.</h3>"

@app.route("/health")
def health():
    return jsonify(status="UP")

def fetchHostAndIP():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return str(hostname), str(ip)

@app.route("/details")
def details():
    hostname, ip = fetchHostAndIP()
    return render_template("index.html", HOSTNAME=hostname, IP=ip)

if __name__ == '__main__':
    app.run()