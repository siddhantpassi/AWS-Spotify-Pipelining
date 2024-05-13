import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):

    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    
    canada_top50_url = 'https://open.spotify.com/playlist/37i9dQZEVXbMda2apknTqH'
    canada_top50_uri = canada_top50_url.split('/')[-1]
    
    data = spotify.playlist_tracks(canada_top50_uri)
    
    botoclient = boto3.client("s3")
    
    filename = "spotify_raw_data"+str(datetime.now())+".json"
    
    botoclient.put_object(
        Bucket="s2passi-spotipy-project",
        Key="raw-data/to-be-processed/"+filename,
        Body=json.dumps(data) )