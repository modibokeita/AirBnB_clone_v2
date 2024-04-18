#!/usr/bin/python3

"""
  script that starts a Flask web application
"""

from flask import Flask

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

@app.route('//c/<text>',strict_slashes=False)
def cisfun(text):
    """
     returns  “C ” followed by the value of the text variable!
     variable
    """
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
