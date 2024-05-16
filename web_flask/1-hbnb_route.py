#!/usr/bin/python3
'''
Script displays Hello HBNB on /
displays HBNB on /hbnb
runs on port 5000 on ip 0.0.0.0
'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    '''
    returns "Hello HBNB!"
    '''
    return 'Hello HBNB!'

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    ''' returns "hbnb" '''
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
