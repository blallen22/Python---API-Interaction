# install spotipy to interact with Spotify's API
# pip install spotipy

# import your spotify credentials
# you receive these after setting up a Spotify Developer account
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
cid = 'XXX'
secret = 'XXX'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

# create objects to store our data in
artist_name = []
track_name = []
popularity = []
track_id = []

# simple for loop to collect 50 tracks from a particular artist
# this is pulling the respective artist name, track name, track id, and popularity into each row
for i in range(0,1):
    track_results = sp.search(q='dance gavin dance', type='track', limit=50, offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])

# now that we have called data from the Spotify API, let's put it into a dataframe with pandas
import pandas as pd
track_dataframe = pd.DataFrame({'artist_name' : artist_name, 'track_name' : track_name, 'track_id' : track_id, 'popularity' : popularity})

# here
print(track_dataframe.shape)
# track_dataframe.head()
# track_dataframe.tail()
print(track_dataframe)

# and there we have it!
# FYI, track_names may be present multiple times because they were released on different albums
# thus they have different track_id values
