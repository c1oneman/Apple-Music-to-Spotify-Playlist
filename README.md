# Apple Music -> Spotify Playlist Converter

This is a simple script to convert Apple Music playlists to Spotify playlists. It scrapes the Apple Music Website to get the songs in the playlist and the Spotify API to create a new playlist with the same\* songs.

\*The script will not be able to find all songs, but it will try to find the closest match.

## Requirements

- Python 3
- [Spotipy](https://spotipy.readthedocs.io/en/2.21.0/#installation)
- [Requests](https://requests.readthedocs.io/en/master/user/install/#install)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

## Usage

1. Create a Spotify app and get the client ID and client secret. [Here](https://developer.spotify.com/documentation/general/guides/app-settings/) is a guide on how to do that.
2. Create a file called '.env' in the same directory as the script and add the following lines:

```
CLIENT_ID=paste_your_client_id_here
CLIENT_SECRET=paste_your_client_secret_here
```

3. Run the script with `python index.py`
4. Enter the Apple Music playlist URL
5. Enter the new Spotify playlist name

## Limitations

- The script will not be able to find all songs, but it will try to find the closest match.
- The script will not be able to find songs that are not available in the user's country.
- The script will not be able to find songs that are not available on Spotify.

## Troubleshooting

- This script is fragile and will break if Apple Music changes their website. If you find a bug, please open an issue. (Or even better, fix it and open a pull request.)

## License

MIT License
We are using the MIT License for this project. You can find the full license text in the LICENSE file.

### Credits

This project was built by [loneman.dev](https://loneman.dev) and GitHub Copilot.

## Contributing

Contributions are welcome! Please open an issue or pull request if you find a bug or want to add a feature.
