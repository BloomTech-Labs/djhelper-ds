import os
import requests
from flask import Flask, \
    request, \
    jsonify
from flask_cors import CORS
from flask import Flask
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import json

import spotipy.util as util
import sys

# Number of titles to get from each channel
MAX_RESULT = 20

# Spotify credentials
SPOTIFY_USERNAME = 'XxxX'
CLIENT_ID = 'XxxX'
CLIENT_SECRET = 'XxxX'
SCOPE = 'playlist-modify-private'


load_dotenv()

# Authenticate with Spotify using the Client Credentials flow
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

spotify_client_id = 'XxxX'
spotify_client_sectret = 'XxxX'


data = {'grant_type': 'client_credentials'}
url = 'https://accounts.spotify.com/api/token'
res = requests.post(url, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
    # return response.json()['access_token']
token = res.json()['access_token']

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


def init_spotify_client():
    try:
        print('Initialising Spotify Client....')
        token = util.prompt_for_user_token(SPOTIFY_USERNAME, SCOPE,
                                           client_id=CLIENT_ID,
                                           client_secret=CLIENT_SECRET,
                                           redirect_uri='http://127.0.0.1:5000/callback/')
        spotify_client = spotipy.Spotify(auth=token)
        print('\nClient initialised!\n')
        return spotify_client
    except:
        sys('\nError initialising Spotify Client!\n')




def spotify_authenticate(CLIENT_ID, CLIENT_SECRET):
    data = {'grant_type': 'client_credentials'}
    url = 'https://accounts.spotify.com/api/token'
    response = requests.post(url, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
    return response.json()['access_token']


@app.route('/backend-search', methods=["GET"])
def search():
    # data = {'grant_type': 'client_credentials'}
    # url = 'https://accounts.spotify.com/api/token'
    # res = requests.post(url, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
    # # return response.json()['access_token']
    # token = res.json()['access_token']

    search_url = 'https://api.spotify.com/v1/search'
    #i know i shouldnt be doing this
    search_txt = request.headers.get('search_text','')
    if search_txt == '':
        search_txt = request.args.get('search_text','')

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(token), # token
    }
    params = (
        ('q', '{}*'.format(search_txt)),
        ('type', 'track'),
        ('limit', 10)
    )

    response = requests.get(search_url, headers=headers, params=params).json()
    return json.dumps(response)


# @app.route('/search', methods=["GET"])
# def search():
#     # user_input = str(request.args['lookup'])
#     # lookup = user_input
#     lookup = 'A lannister always pays his debts'
#     results = sp.search(q=lookup, limit=10) #, type="track")
#     # return jsonify(results)
#     for i, track in enumerate(results['tracks']['items']):
#         return jsonify(' ', i, track['name'],'-', track['artists'][0]['name'], '-', track['id'],
#          '-', track['external_urls']['spotify'])





# FLASK_APP=application3.py flask run

# pip freeze > requirements.txt
# FLASK_ENV=development
# FLASK_APP=server