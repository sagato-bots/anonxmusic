from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Sagato-bots"


if __name__ == "__main__":
    app.run()
