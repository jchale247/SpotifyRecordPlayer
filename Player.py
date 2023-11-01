import spotipy
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from spotipy.oauth2 import SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='user-read-currently-playing streaming user-modify-playback-state user-read-playback-state',client_id ='98b2d6544c44499b8bcfa1d1b95ac160', client_secret = 'f5071da8a3124517888440cfbf78e32e',redirect_uri='https://records.jchomeserver.com/callback'))
currentAlbum = ""
reader = SimpleMFRC522()

while 1 == 1:
    #print(sp.devices())
    try:
        id, text = reader.read()
        nextAlbum = text
        if currentAlbum != nextAlbum:
            try:
                sp.start_playback('6b65de863672452bbf099ee1807619b057cc5cac', nextAlbum)
            except Exception:
                print("invalid album")
                continue
            currentAlbum = nextAlbum 
    except:
        continue
