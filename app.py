from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, SecDevOps!"  #SecDevOps

if __name__ == "__main__":
    app.run(host='0.0.0.0') #host='0.0.0.0'
