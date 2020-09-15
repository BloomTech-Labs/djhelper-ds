import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from dotenv import load_dotenv
import os

import requests
from flask import Flask, request, jsonify, Response

import pandas as pd
import json

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

'''Functions'''

load_dotenv() # load environment variables

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


SEARCH_ENDPOINT = 'https://api.spotify.com/v1/search'
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID', default="OOPS")
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET', default="OOPS")

data = {'grant_type': 'client_credentials'}
url = 'https://accounts.spotify.com/api/token'
response = requests.post(url, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
token = (response.json()['access_token'])

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(token)
    }


def get_rid_of_nulls(value):
    if pd.isnull(value):
        return 'http://bit.ly/2nXRRfX'
    else:
        return value


def get_audio_features(track_ids):
    saved_tracks_audiofeat = [ ]
    for ix in range(0,len(track_ids),50):
        audio_feats = sp.audio_features(track_ids[ix:ix+50])
        saved_tracks_audiofeat += audio_feats
    return saved_tracks_audiofeat


