from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h3>Hello World from a Flask app.</h3>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)