import requests
#TODO: import grove stuff

# The URL for the Flask server's endpoint
url = "http://10.25.95.81:5000/"
posturl = "http://10.25.95.81:5000/post_test"

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
