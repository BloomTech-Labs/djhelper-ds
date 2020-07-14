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


load_dotenv()

# Authenticate with Spotify using the Client Credentials flow
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

spotify_client_id = '1544e44f656f402894c4b6b4c0efdf9b'
spotify_client_sectret = '0681b6fa2930480fbcfe9a31a8e05bae'

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


def spotify_authenticate(spotify_client_id, spotify_client_sectret):
    data = {'grant_type': 'client_credentials'}
    url = 'https://accounts.spotify.com/api/token'
    response = requests.post(url, data=data, auth=(spotify_client_id, spotify_client_secret))
    return response.json()['access_token']


@app.route('/backend-search', methods=["GET"])
def search():
    token = spotify_authenticate()
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








# FLASK_APP=app3.py flask run