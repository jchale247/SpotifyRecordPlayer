#!/usr/bin/python3
import spotipy
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from spotipy.oauth2 import SpotifyOAuth

#Setup API Information
sp_client_id= '*********'
sp_client_secret= '*******'
sp_scope = 'user-read-currently-playing streaming user-modify-playback-state user-read-playback-state'
sp_redirect_url= 'google.com/callback'

#setup spotipy connection and rfid reader
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope = sp_scope ,client_id = sp_client_id, client_secret = sp_client_secret, redirect_uri = sp_redirect_url))
reader = SimpleMFRC522()

#starter fields
currentAlbum = ""
nextAlbum = ""
id = ""
text = ""

while 1 == 1:
    try:
        id, text = reader.read()
        nextAlbum = 'https://open.spotify.com/' + str(text).strip()
        time.sleep(1)
        if currentAlbum != nextAlbum:
            try:
                sp.start_playback('6b65de863672452bbf099ee1807619b057cc5cac', nextAlbum)
            except Exception:
                print("invalid album")
                continue
            currentAlbum = nextAlbum 
    except:
        continue
