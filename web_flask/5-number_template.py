#!/usr/bin/python3
'''
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
You must use the option strict_slashes=False in your route definition
/python/<text>: display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
The default value of text is “is cool”

/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
'''
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    ''' this is the root path '''
    return 'Hello HBNB'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    ''' the "/hbnb" path '''
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    ''' the c is fun page
    replaces _ with space
    '''

    return 'C {}'.format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    ''' Python is cool
    set default text to is cool
    replace _ with ' '
    '''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    ''' this path takes an int argument '''
    if isinstance(n, int):
        return '{} is a number'.format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    ''' render a template if param is int '''
    if isinstance(n, int):
        return render_template('5-number.html', num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
