import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

baseUrl = '/api/v1/'

bonjours = [
    {'id': 1, 'description': 'Bonjour!', 'language': 'fr'},
    {'id': 2, 'description': 'Hallo!', 'language': 'nl'},
    {'id': 3, 'description': 'Hello!', 'language': 'en'}
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hi all! Please stay in your kot and practise social distancing!</h1>"


@app.route(baseUrl + 'bonjours/all', methods=['GET'])
def bonjour_all():
    return jsonify(bonjours)


@app.route(baseUrl + 'bonjours', methods=['GET'])
def bonjour_language():
    # check for provided language parameter in request
    if 'language' in request.args:
        language = request.args['language']
    else:
        return "Please provide a language"

    result = []

    for bonjour in bonjours:
        if bonjour['language'] == language:
            result.append(bonjour)

    return jsonify(result)


app.run()
print('ok')
