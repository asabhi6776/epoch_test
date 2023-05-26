from flask import Flask, render_template
from time import time

app = Flask(__name__)

@app.route('/')
def display_epoch():
    current_epoch = int(time())
    return render_template('index.html', epoch=current_epoch)

if __name__ == '__main__':
    app.run()
