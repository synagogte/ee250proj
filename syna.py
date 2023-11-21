import requests
import base64

from flask import Flask
from flask import jsonify
from flask import request
from flask import redirect
import json

app = Flask('Test')

track_list = {}
features_dict = {}

client_id = "83825bd6133a46f89a4c9e1fdc903b64"
client_secret =  "8a215f2776684ff6acfcce1295b9eafd"
redirect_uri = 'http://192.168.64.2:5000/callback'

TOKEN_URL = 'https://accounts.spotify.com/api/token'
SEARCH_URL = 'https://api.spotify.com/v1/search'
USER_TOP_URL = 'https://api.spotify.com/v1/me/top/tracks'


@app.route('/', methods=['GET'])
def home():
    auth_url = f'https://accounts.spotify.com/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=user-top-read'
    print(auth_url)
    print("hi")
    #return "line 25"
    return redirect(auth_url)

#spotify redirects the user to this page
@app.route('/callback')
def callback():
    print("here")
    authorization_code = request.args.get('code')
    print("code:", authorization_code)
    #get the token access 
    credentials = client_id + ":" + client_secret

    credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

    token_response = requests.post(TOKEN_URL, data={
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': redirect_uri,
    }, headers={'Authorization': f'Basic {credentials}', 'Content-Type': 'application/x-www-form-urlencoded'})

    token_data = token_response.json()
    access_token = token_data.get('access_token')

    # Use the access token to make a search request
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'limit': 10}

    search_response = requests.get(USER_TOP_URL, params=params, headers=headers)
    search_data = search_response.json()

    # Print the track information
    if 'items' in search_data:
        for track in search_data['items']:
            print(f"Track: {track['name']}, Artist: {track['artists'][0]['name']}, id: {track['id']}")
            track_list[track['name']] =  track['id']
    else:
        print("No tracks found.")
    print(len(track_list))

    FEATURES_URL = 'https://api.spotify.com/v1/audio-features'
    for name, track_id in track_list.items():
        print("name:", name, "id: ", track_id)
        params = {'ids': track_id}
        search_response = requests.get(FEATURES_URL, params=params, headers=headers)
        search_data = search_response.json()
        #print(search_data)
        if 'audio_features' in search_data:
            for features in search_data['audio_features']:
                print(features["loudness"], features["duration_ms"])
                features_dict[name] = (features["loudness"], features["duration_ms"])
    return jsonify(features_dict)



    # token_data = token_response.json()
    # access_token = token_data.get('access_token')

    # # Use the access token to make a search request
    # headers = {'Authorization': f'Bearer {access_token}'}
    # # params = {'q': 'album:1989 track:style', 'limit':10}
    # params = {'type': 'track', 'limit':10}


    # search_response = requests.get(USER_TOP_URL, params=params, headers=headers)
    # search_data = search_response.json()
    # print(len(search_data))
    # print(search_data)

    # # # Print the track information
    # # if 'items' in search_data:
    # #     for track in search_data['items']:
    # #         print(f"Track: {track['name']}, Artist: {track['artists'][0]['name']}")
    # # else:
    # #     print("No tracks found.")

    # return jsonify(search_data)
    #return search_data

# Print the track information
# if 'tracks' in search_data:
#     for track in search_data['tracks']['items']:
#         print(f"Track: {track['name']}, Artist: {track['artists'][0]['name']}")
# else:
#     print("No tracks found.")


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
