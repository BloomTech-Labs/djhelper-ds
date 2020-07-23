import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from dotenv import load_dotenv
import os

import requests
from flask import Flask, request, jsonify, Response

import pandas as pd
import json

load_dotenv() # load environment variables


app = Flask(__name__)

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


SEARCH_ENDPOINT = 'https://api.spotify.com/v1/search'
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID', default="OOPS")
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET', default="OOPS")

data = {'grant_type': 'client_credentials'}
url = 'https://accounts.spotify.com/api/token'
response = requests.post(url, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
token = (response.json()['access_token'])


@app.route('/')
def hello_world():
    return "it's live!"


@app.route('/prepare_search_track/<name>', methods=['GET', 'POST'])
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


@app.route('/track_search_ready/<name>', methods=['GET', 'POST'])
def search(name):
    data = search_by_name(name)
    users_response = []
    for i, track in enumerate(data['tracks']['items']):
        user_dict = (i, track['artists'][0]['name'], track['name'], track['id'], track['external_urls']['spotify'], track['explicit'])
        users_response.append(user_dict)
    _track_df = pd.DataFrame(users_response, columns = ['ind','artist_name', 'song_name', 
                                                    'id', 'external_urls', 'explicit'])
    _track_df = _track_df.drop(['ind'], axis=1)
    _track_df.index += 1

    return (json.dumps(json.loads(_track_df.to_json(orient='index')), indent=2)) # orient='values', 'records', 'index', 'columns'


@app.route('/audio_features/<name>', methods=['GET', 'POST'])
def audio_feat(name):
    data = search_by_name(name)
    users_response = []
    for i, track in enumerate(data['tracks']['items']):
        user_dict = (i, track['artists'][0]['name'], track['name'], track['id'], track['external_urls']['spotify'], track['explicit'])
        users_response.append(user_dict)
    _track_df = pd.DataFrame(users_response, columns = ['ind','artist_name', 'song_name', 
                                                    'id', 'external_urls', 'explicit'])
    _track_df = _track_df.drop(['ind'], axis=1)

    '''start index count from 1 instead of 0'''
    _track_df.index += 1

    '''create get audio features function'''
    def get_audio_features(track_ids):
        saved_tracks_audiofeat = [ ]
        for ix in range(0,len(track_ids),50):
            audio_feats = sp.audio_features(track_ids[ix:ix+50])
            saved_tracks_audiofeat += audio_feats
        return saved_tracks_audiofeat
    
    '''apply the function'''
    _audiofeat = get_audio_features(_track_df['id'])
    
    '''creat columns names for the dataframe'''
    _audiofeat = pd.DataFrame(_audiofeat, columns = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
    'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature'])

    _audiofeat_df = _audiofeat.drop(['analysis_url', 'track_href', 'type', 'uri'], axis = 1)

    tracks_plus_df = _track_df.merge(_audiofeat_df, how = 'left', left_on = 'id', right_on = 'id')

    tracks_plus_df.index += 1

    return (json.dumps(json.loads(tracks_plus_df.to_json(orient='index')), indent=2))


if __name__ == "__main__":
    app.run(debug=True)
