from flask import Flask
from flask import jsonify
from flask import request
import json

#TODO spotify api calls, create a database that has the songs and their duration / energy


app = Flask('Test')

num_duration = 0
num_energy = 0

#main landing page
@app.route('/', methods=['GET'])
def test1():
    return "duration: " + str(num_duration) + " energy: " + str(num_energy)
    #TODO return the song that was selected

#handles incoming post request
@app.route('/post_test', methods=['POST', 'GET'])
def receive_string():
    #need to declare that these are globals
    global num_duration
    global num_energy

    # Extract the data from the POST request
    duration = request.json.get('duration')
    energy = request.json.get('energy')

    #TODO: use num_duration and num_energy which come from the rpi sensors to select a song.
    num_duration = float(duration)
    num_energy = float(energy)

    # Return a response
    return jsonify({"duration": duration, "energy": energy}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
