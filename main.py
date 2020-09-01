import os
from db import col as mongoCol
from link import generateLink
import json
from flask import Flask, request, Response, redirect
from flask_api import status
# app = Flask(__name__, static_folder='./frontend/build', static_url_path='/')
app = Flask(__name__, static_folder='./public', static_url_path='/')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        req = request.get_json()
        generatedLink = generateLink()
        mongoCol.insert_one(
            {"link": req.get('linkToRedirect'), "postfix": generatedLink})
        response = Response(json.dumps(
            {'createdLink': generatedLink}), status=status.HTTP_200_OK, mimetype="application/json")
    else:
        response = Response('Cannot get /create')
    return response


@app.route('/<postfix>', methods=['GET'])
def render_redirect_page(postfix):
    return app.send_static_file('index.html')


@app.route('/ls/<postfix>', methods=['GET'])
def postfix(postfix):
    el = mongoCol.find_one({"postfix": postfix})
    if el:
        return {'url': el["link"]}
    else:
        return Response('404', status=status.HTTP_404_NOT_FOUND)


# if __name__ == '__main__':
#     app.run(debug=True,
#             port=os.environ.get("PORT", 8080))
