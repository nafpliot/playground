from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    output = {"id": os.environ['POD_NAME'], "message": "Hello world!"}
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')