from flask import Flask
from flask import Response
flask_app = Flask('flaskapp')


@flask_app.route('/hello')
def hello_world():
    return Response(
        'Hello world from Flask!\nPrueba iso-8859-1: áéíóúñ',
        mimetype='text/plain'
    )

app = flask_app.wsgi_app
