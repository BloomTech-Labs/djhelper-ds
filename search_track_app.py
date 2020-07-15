import spotipy

from dotenv import load_dotenv
import os

import os
import requests
from flask import Flask, \
    request, \
    jsonify

import json

load_dotenv() # load environment variables


SEARCH_ENDPOINT = 'https://api.spotify.com/v1/search'
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID', default="OOPS")
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET', default="OOPS")

app = Flask(__name__)


data = {'grant_type': 'client_credentials'}
url = 'https://accounts.spotify.com/api/token'
response = requests.post(url, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
token =  (response.json()['access_token'])


@app.route('/prepare_search_track/<name>')
def search_by_name(name):
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(token)
    }
    myparams = {'type': 'track',
    'limit': 10}
    myparams['q'] = name
    resp = requests.get(SEARCH_ENDPOINT, headers=headers, params=myparams)
    return resp.json()


@app.route('/track_search_ready/<name>')
def search(name):
    data = search_by_name(name)
    users_response = []
    for i, track in enumerate(data['tracks']['items']):
        user_dict = (i, track['artists'][0]['name'], track['name'], track['id'], track['external_urls']['spotify'])
        users_response.append(user_dict)
    return jsonify(users_response)


if __name__ == "__main__":
    app.run(debug=True)
