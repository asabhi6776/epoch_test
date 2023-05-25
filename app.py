from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def index():
    return str(round(time.time()))

if __name__ == "__main__":
    app.run(use_reloader=True)
