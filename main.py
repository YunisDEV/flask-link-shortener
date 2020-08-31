from db import col
import json
from flask import Flask, request, Response
from flask_api import status
app = Flask(__name__, static_folder='./frontend/build', static_url_path='/')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        req = request.get_json()
        generatedLink = generateLink()
        response =
    else:
        response = Response('Cannot get /create')
    return response


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', debug=False,
                  port=os.environ.get("PORT", 8080))
