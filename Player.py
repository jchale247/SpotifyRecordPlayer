import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id ='98b2d6544c44499b8bcfa1d1b95ac160', client_secret = 'f5071da8a3124517888440cfbf78e32e')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

sp.start_playback('39a80c53edbd60f116ffb6e75d8bb994ac3c77e9', 'https://open.spotify.com/album/2yI4m5Yu2tl8v0It5P9WVz')

'd59d5c2b-fec0-5ce1-bb61-e8896df130d0'