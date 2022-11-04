# Webscrape Apple Music playlist URL and return a list of songs

import requests
from bs4 import BeautifulSoup

def get_playlist(url):
    # Get the playlist
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Save soup to text file for logs
    # with open('soup.txt', 'w') as f:
    #     f.write(soup.prettify())
    
    artistDivs = soup.find_all('div', class_='songs-list-row__by-line')
    artists = []
    for content in artistDivs:
        txt = content.find('span', class_='svelte-x4tov2').text
        # clean up the text
        txt = txt.replace('\n', '')
        artists.append(txt)
    
    songDivs = soup.find_all('div', class_='songs-list-row__song-name')
    songs = []
    for content in songDivs:
      # Remove all text within parentheses and brackets
      txt = re.sub(r'\([^)]*\)', '', content.text)
      songs.append(txt)
    search_array = []

    for i in range(0, artists.__len__()):
        search_array.append(songs[i] + ' ' + artists[i][0:4])
    print(search_array)
    return search_array

# Authenticate with Spotify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re


# Get CLIENT_ID and CLIENT_SECRET from .env file
import os
from dotenv import load_dotenv
load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


token = spotipy.util.prompt_for_user_token(
    username='username',
    scope='playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative user-library-read user-library-modify user-top-read user-read-recently-played user-read-playback-state user-modify-playback-state user-read-currently-playing',
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri='http://localhost:8888/callback/')
sp = spotipy.Spotify(auth=token)

# Search for songs and add to playlist
def search_and_add(search_array):
    # get username
    username = sp.me()['id']
    # Prompt user for playlist name
    playlist_name = input('Enter new playlist name: ')
    playlist = sp.user_playlist_create(username,playlist_name, public=False, description='Created with Python')
    playlist_id = playlist['id']
    playlist_url = playlist['external_urls']['spotify']
    for i in range(0, search_array.__len__()):
        results = sp.search(q=search_array[i], limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            print_progress_bar(i, search_array.__len__())
            sp.user_playlist_add_tracks(username, playlist_id, [track['uri']])
        else:
            print('No results for ' + search_array[i])
    return playlist_url

def print_progress_bar(iteration, total):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filledLength = int(25 * iteration // total)
    bar = '█' * filledLength + '-' * (25 - filledLength)
    print('\r%s |%s| %s%% %s' % ('Progress:', bar, percent, 'Complete'), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


# Prompt user for playlist URL
url = input('Apple Music playlist URL: ')
result = search_and_add(get_playlist(url))
print(result)
