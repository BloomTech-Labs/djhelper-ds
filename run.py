from mapping import *

from dotenv import load_dotenv
import os

import requests
from flask import Flask, request, jsonify, Response

import pandas as pd
import json

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

load_dotenv() # load environment variables

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "it's live!"


@app.route('/prepare_search_track/<name>', methods=['GET', 'POST'])
def search_by_name(name):
    myparams = {
        'type': 'track',
        'limit': 10}
    myparams['q'] = name
    resp = requests.get(SEARCH_ENDPOINT, headers=headers, params=myparams)
    return resp.json()


@app.route('/track_search_ready/<name>', methods=['GET', 'POST'])
def search(name):
    data = search_by_name(name)
    users_response = []
    for i, track in enumerate(data['tracks']['items']):
        user_dict = (i, track['artists'][0]['name'], track['name'], track['id'], track['external_urls']['spotify'], track['explicit'],
        track['preview_url'], track['album']['images'][1]['url'])
        users_response.append(user_dict)
    _track_df = pd.DataFrame(users_response, columns = ['ind','artist_name', 'song_name', 
                                                    'id', 'external_urls', 'explicit', 'preview', 'image'])
    _track_df = _track_df.drop(['ind'], axis=1)

    _track_df['preview'] = _track_df['preview'].apply(get_rid_of_nulls)
    _track_df.index += 1

    return (json.dumps(json.loads(_track_df.to_json(orient='index')), indent=2)) # orient='values', 'records', 'index', 'columns'


@app.route('/audio_features/<name>', methods=['GET', 'POST'])
def audio_feat(name):
    data = search_by_name(name)
    users_response = []
    for i, track in enumerate(data['tracks']['items']):
        user_dict = (i, track['artists'][0]['name'], track['name'], track['id'], track['external_urls']['spotify'], track['explicit'],
        track['preview_url'], track['album']['images'][1]['url'])
        users_response.append(user_dict)
    _track_df = pd.DataFrame(users_response, columns = ['ind','artist_name', 'song_name', 
                                                    'id', 'external_urls', 'explicit', 'preview', 'image'])
    _track_df = _track_df.drop(['ind'], axis=1)

    _track_df['preview'] = _track_df['preview'].apply(get_rid_of_nulls)

    '''start index count from 1 instead of 0'''
    _track_df.index += 1
    
    '''apply the function'''
    _audiofeat = get_audio_features(_track_df['id'])
    
    '''creat columns names for the dataframe'''
    _audiofeat = pd.DataFrame(_audiofeat, columns = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
    'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature'])

    _audiofeat_df = _audiofeat.drop(['analysis_url', 'track_href', 'type', 'uri'], axis = 1)

    tracks_plus_df = _track_df.merge(_audiofeat_df, how = 'left', left_on = 'id', right_on = 'id')

    tracks_plus_df.index += 1

    return (json.dumps(json.loads(tracks_plus_df.to_json(orient='index')), indent=2))


@app.route('/predict/<track_id>', methods=['GET', 'POST'])
def dj_rec(track_id):
    neighbors=4
    max_distance=5.0
    '''[:-10] will return only 10 closest songs to the original track_id
    by removing [:-10], code will return 20 songs. It will take double of time to make a prediction though'''
    rel_artists = sp.artist_related_artists(sp.track(track_id=track_id)['artists'][0]['id'])['artists'][:-10]
    artist_log = []
    for a in rel_artists:
        artist_log.append(a['id'])
    feat_log = []
    for artist in artist_log:
        for track in sp.artist_top_tracks(artist)['tracks']:
            feat_log.append(sp.audio_features(track['id'])[0])

    catalog = pd.DataFrame.from_dict(feat_log)

    root = pd.DataFrame.from_dict(sp.audio_features(tracks=[track_id]))

    merged_df = root.append(catalog, ignore_index=True)

    dropped_df = merged_df.drop(columns=['uri', 'track_href', 'id', 'duration_ms', 'time_signature', 'mode', 'loudness', 'type', 'analysis_url'])
    scaled_df = StandardScaler().fit_transform(dropped_df)
    trans_array = scaled_df.copy()

    trans_array[:,0] = [u*2.4 for u in trans_array[:,0]] # acousticness
    trans_array[:,1] = [((u*u)**0.5)*u for u in trans_array[:,1]] # danceability
    trans_array[:,2] = [u*1.7 for u in trans_array[:,2]] # energy
    trans_array[:,3] = [u*1.4 for u in trans_array[:,3]] # instrumentalness
    trans_array[:,4] = [u*0.9 for u in trans_array[:,4]] # key
    trans_array[:,5] = [u*1.0 for u in trans_array[:,5]] # liveness
    trans_array[:,6] = [u*1.0 for u in trans_array[:,6]] # speechiness
    trans_array[:,7] = [u*1.1 for u in trans_array[:,7]] # tempo
    trans_array[:,8] = [u*2.5 for u in trans_array[:,8]] # valence

    knn = NearestNeighbors()
    knn.fit(trans_array)

    rec = knn.kneighbors(trans_array[[0]], n_neighbors=neighbors+1)

    predict_response = []
    for n in range(1,neighbors+1):
        if rec[0][0][n] <= max_distance:
            pred_dict = (merged_df.loc[rec[1][0][n],'id'], rec[0][0][n])
        predict_response.append(pred_dict)

    pred = pd.DataFrame(predict_response, columns=['recommendation', 'distance'])

    df_predict_tracks = pd.DataFrame() # create dataframe

    a = [sp.track(ii)['artists'][0]['name'] for ii in pred['recommendation']]
    b = [sp.track(ii)['name'] for ii in pred['recommendation']]
    c = [sp.track(ii)['id'] for ii in pred['recommendation']]
    d = [sp.track(ii)['external_urls']['spotify'] for ii in pred['recommendation']]
    e = [sp.track(ii)['explicit'] for ii in pred['recommendation']]
    f = [sp.track(ii)['preview_url'] for ii in pred['recommendation']]
    g = [sp.track(ii)['album']['images'][1]['url'] for ii in pred['recommendation']]

    # Save the results
    df_predict_tracks['artist_name'] = a
    df_predict_tracks['song_name'] = b
    df_predict_tracks['id'] = c
    df_predict_tracks['url'] = d
    df_predict_tracks['explicit'] = e
    df_predict_tracks['preview'] = f
    df_predict_tracks['image'] = g

    df_predict_tracks['preview'] = df_predict_tracks['preview'].apply(get_rid_of_nulls)

    df_predict_tracks.index +=1

    return json.dumps(json.loads(df_predict_tracks.to_json(orient='index')), indent=2)


if __name__ == "__main__":
    app.run(debug=True)
