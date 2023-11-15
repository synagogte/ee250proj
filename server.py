from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask('Test')


@app.route('/', methods=['GET'])
def test1():
    return "hi"




if __name__ == '__main__':
    app.run(host='0.0.0.0')
