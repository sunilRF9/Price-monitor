from flask import Flask, jsonify
from tasks import *

app = Flask(__name__)

@app.route('/')
def index():
     res = clean.delay()
     return jsonify(res.get())

if __name__ == "__main__":
    app.run(debug=True, port=6969)
