import spotipy
from spotipy.oauth2 import SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='user-read-currently-playing streaming user-modify-playback-state user-read-playback-state',client_id ='98b2d6544c44499b8bcfa1d1b95ac160', client_secret = 'f5071da8a3124517888440cfbf78e32e',redirect_uri='https://records.jchomeserver.com/callback'))
currentAlbum = ""

while 1 == 1:
    print(sp.devices())
    nextAlbum = input("Album URL: ")
    if currentAlbum != nextAlbum:
        sp.start_playback('EDA5D75C-DDFC-4BA8-8A4D-D4E5986DDC1E', nextAlbum)
        currentAlbum = nextAlbum 

#'d59d5c2b-fec0-5ce1-bb61-e8896df130d0'