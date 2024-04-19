#!/usr/bin/python3

"""
  script that starts a Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',strict_slashes=False)
def hello_hbnb():
    """
     returns Hello HBNB!
    """
    return 'Hello HBNB!'

@app.route('/hbnb',strict_slashes=False)
def hbnb():
    """
     returns  HBNB!
    """
    return 'HBNB!'

@app.route('/c/<text>',strict_slashes=False)
def cisfun(text):
    """
     returns  “C ” followed by the value of the text variable!
     variable
    """
    return 'C ' + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>',strict_slashes=False)
def print_python(text):
    """
     returns  “python ” followed by the value of the text variable!
     variable
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>',strict_slashes=False)
def print_n(n):
    """
      display “n is a number” only if n is an integer
    """
    return "{:d} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def display_templete(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_even(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        even_num = 'even'
    else:
        even_num = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           even_num=even_num)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
