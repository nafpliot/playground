from flask import Flask, jsonify
import urllib, json, os

app = Flask(__name__)

@app.route('/')
def index():
    url = "http://server:5000"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    output = {"id": os.environ['POD_NAME'], "message": data['message'][::-1]}
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')