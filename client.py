import requests
import sys
import time
sys.path.append('/home/pi/Dexter/GrovePi/Software/Python')

import grovepi

potentiometer = 2 #port A2
soundsensor = 1 #port A1

# The URL for the Flask server's endpoint
url = "http://172.20.10.5:5000/"
posturl = "http://172.20.10.5:5000/post_test"

#get example:
# Send a GET request to the server
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the content of the response
    print("Response from server:", response.text)
else:
    # Print an error message if something went wrong
    print("Failed to retrieve data from the server. Status code:", response.status_code)

#TODO: sample and send data from potentiometer and thing
#post example:
# The string data you want to send
data_to_send = {'duration': '1', 'energy':'0.8'}

# Send a POST request to the server with the string data
response = requests.post(posturl, json=data_to_send)

# Check if the request was successful
if response.status_code == 200:
    # Print the content of the response
    print("Response from server:", response.json())
else:
    # Print an error message if something went wrong
    print("Failed to send data to the server. Status code:", response.status_code)



while(True):
    p = grovepi.analogRead(potentiometer)
    s = grovepi.analogRead(soundsensor)
    print(p)
    print(s)
    time.sleep(0.2)